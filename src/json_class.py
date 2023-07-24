import json
from src.abstract_classes import AbstractJson
from src.vacancy_class import Vacancy


class WorkFile(AbstractJson):
    """Класс для обработки инфорации о вакансиях"""
    def __init__(self, vacancy, many_vacancies):
        self.__filename = f'{vacancy.title()}.json'
        self.many_vacancies = many_vacancies
        self.create_file()

    def create_file(self):
        """Сохранение в файл списка вакансий"""

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(self.many_vacancies, file, ensure_ascii=False, indent=4)

    def load_file(self):
        """Загрузка из файла списка вакансий"""

        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


    def filtred_vacancies(self, filter_field, filter_value):
        """Фильтрация списка вакансий"""

        data = self.load_file()
        vacancies = [Vacancy(x['title'], x['employer'], x['url'], x['area'], x['experience'], x['employment'],
                             x['salary'], x['salary_from'], x['salary_to'], x['currency'], x['portal'])
                     for x in data
                     if filter_value in x[filter_field].lower()
                     ]
        return vacancies

    def not_filtred_vacancies(self):
        """Фильтрация не включена в список вакансий"""

        data = self.load_file()
        vacancies = [Vacancy(x['title'], x['employer'], x['url'], x['area'], x['experience'], x['employment'],
                             x['salary'], x['salary_from'], x['salary_to'], x['currency'], x['portal'])
                     for x in data]
        return vacancies