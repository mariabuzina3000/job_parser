from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для API и получения вакансий"""

    @abstractmethod
    def get_requests(self):
        """Функция для отправки запроса"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Функция для получения вакансий"""
        pass


class AbstractVacancies(ABC):
    """Абстрактный класс для обработки списка вакансий"""

    def add_vac(self):
        """Функция для добавления вакансий"""
        pass

    def get_data(self):
        """Функция для получения данных из файла по указанным критериям"""
        pass

    def del_info(self):
        """Функция для удаления информации о вакансиях"""
        pass
