import random


class PersonData:
    user_name = 'Евгения Смирнова'
    login = 'evgenya@test.ru'
    password = '12345tesT_'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@gmail.com"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"