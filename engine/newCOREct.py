# Импорт необходимых модулей
import random

# База данных N4M7C
CELEST1A = {
    "HIT": "What brings you to life?",
    "MIND": {
        "CAPACITY": ["Wholesome", "Unreachable", "Clear", "Saint"],
        "COMPUTING": ["Understanding", "Mindfulness", "Intellect", "Wisdom"],
        "DIRECTION": ["Forward", "Upward", "Onward", "Inward"],
        "REFLECTION": ["Contemplation", "Reflection", "Thought", "Consideration"]
    },
    # Остальные параметры опущены для краткости
}

C2GB = {
    "OPERATION": {
        "TOOLS": {
            "1": ["T", "Y", "0", "F", "N"],
            "ABSCENCE/OBSCENCE": ["Abscence", "Obscence"],
            "POSITIVE/NEGATIVE": ["Positive", "Negative"],
            "TRUE/FALSE": ["True", "False"],
            "YES/NO": ["Yes", "No"]
        },
        "EXPERIENCE": {
            "URL": "https://example.com",
            "IRL": "In Real Life"
        }
    }
}

# Функция для генерации ответа на вопрос пользователя
def generate_response(question):
    if question == CELEST1A["HIT"]:
        return random.choice(CELEST1A["MIND"]["CAPACITY"])

# Тестирование функции
user_question = "What brings you to life?"
print("User: " + user_question)
print("VARRAWA CODEX: " + generate_response(user_question))