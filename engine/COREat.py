# Импорт необходимых библиотек
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional

# Загрузка данных и предобработка
# Здесь мы загружаем данные из CELEST1A, C2GB и N4M7C и преобразуем их в формат, пригодный для обучения нейросети

# Определение модели нейросети
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length))
model.add(Bidirectional(LSTM(64)))
model.add(Dense(vocab_size, activation='softmax'))

# Компиляция модели
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Функция для генерации ответа на запрос пользователя
def generate_response(input_text):
    # Преобразование текста в последовательность чисел
    input_sequence = tokenizer.texts_to_sequences([input_text])
    padded_input_sequence = pad_sequences(input_sequence, maxlen=max_length, padding='post')
    
    # Предсказание следующего слова
    predicted_index = np.argmax(model.predict(padded_input_sequence), axis=-1)
    
    # Получение слова по индексу из словаря
    predicted_word = reverse_word_index[predicted_index[0]]
    
    return predicted_word

# Пример использования функции для генерации ответа
input_text = "What brings you to life?"
response = generate_response(input_text)
print(response)
