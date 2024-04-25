# backend.py

# Здесь мы импортируем необходимые модули
import tensorflow as tf
import numpy as np
import pylance as pl
import data as d

# Создаем класс сервиса, который будет обрабатывать запросы пользователя, в даном случае это класс Celest1a, которая в нашей программе отвечает за общение по вопросам биокинетики человека
class CELEST1A:
    def __init__(body):
        # Здесь мы инициализируем переменные и данные, связанные с параметрами тела 
        body.data = {
        "AGILITY": ["Привет""Давай поговорим обо мне""Давай поговорим о тебе""Помоги мне"]
        }

    # Метод для получения вопроса
    def get__question(body):
        return (body.data["AGILITY"])
    
    # Метод для получения ответа 
    def get_answer(body):
        return (body.data["AGILITY"])

# Создаем экземпляр сервиса
service = VARRAWA()
