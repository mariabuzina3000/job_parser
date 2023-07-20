from src.abstract_classes import AbstractVacancies

class Vacancy(AbstractVacancies):
    """Класс для обработки и сравнения вакансий"""
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description



    def