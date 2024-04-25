import tensorflow as tf
import numpy as np

# Задаем вопросы и ответы для обучения
questions = [
    "Как тебя зовут?",
    "Как дела?",
    "Что ты умеешь?",
    "Какая твоя любимая книга?",
    "Какой твой любимый фильм?"
]

answers = [
    "Меня зовут ChatGPT. Чем могу помочь?",
    "Дела отлично, спасибо! А у вас?",
    "Я умею отвечать на вопросы, задавайте что-нибудь :)",
    "Моя любимая книга - 'Война и мир' Льва Толстого.",
    "Мой любимый фильм - 'Матрица'."
]

# Преобразуем тексты в числовые векторы
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(questions)
tokenizer.fit_on_texts(answers)

question_sequences = tokenizer.texts_to_sequences(questions)
answer_sequences = tokenizer.texts_to_sequences(answers)

question_sequences = tf.keras.preprocessing.sequence.pad_sequences(question_sequences, padding='post')
answer_sequences = tf.keras.preprocessing.sequence.pad_sequences(answer_sequences, padding='post')

# Создаем и обучаем модель
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(tokenizer.word_index) + 1, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(len(tokenizer.word_index) + 1, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(question_sequences, answer_sequences, epochs=500)

# Функция для генерации ответа
def generate_response(question):
    question_seq = tokenizer.texts_to_sequences([question])
    question_seq = tf.keras.preprocessing.sequence.pad_sequences(question_seq, padding='post', maxlen=question_sequences.shape[1])
    predicted_answer = model.predict(question_seq)
    predicted_answer = np.argmax(predicted_answer, axis=-1)
    return tokenizer.sequences_to_texts(predicted_answer)[0]

# Диалог с пользователем
while True:
    user_question = input("Вы: ")
    if user_question.lower() == 'выход':
        print("До свидания!")
        break
    response = generate_response(user_question)
    print("Нейросеть:", response)
