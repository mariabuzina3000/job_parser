from abc import ABC, abstractmethod


class AbstractApi(ABC):
    "Абстрактный класс для API и получения вакансий"

    @abstractmethod
    "Функция для отправки запроса"
    def get_requests(self):
        pass

    @abstractmethod
    "Функция для получения вакансий"
    def get_vacancies(self):
        pass


class AbstractVacancies(ABC):
    "Абстрактный класс для обработки списка вакансий"

    def add_vac(self):
        "Функция для добавления вакансий"
        pass

    def get_data(self):
        "Функция для получения данных из файла по указанным критериям"
        pass

    def del_info(self):
        "Функция для удаления информации о вакансиях"
        pass
