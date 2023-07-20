import requests
from src.abstract_classes import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс выгрузки информации по API с сайта hh.ru"""

    def __init__(self, vacancy: str):
        self.vacancy = vacancy
        self.__url = 'https://api.hh.ru/vacancies'
        self.__key = 'items'
        self.__param = {
            'text': self.vacancy,
            'page': 0,
            'per_page': 100
        }

    @property
    def url(self):
        return self.__url

    @property
    def key(self):
        return self.__key

    @property
    def param(self):
        return self.__param


    def get_requests(self):
        """Функция, отправляющая запрос на сайт"""
        data = requests.get(self.__url, params=self.__param)
        return data.json()[self.__key]

    def get_vacancies(self):
        """Функция для вывода списка ванаксий"""
        self.vacancies = []
        self.num_page = 3

        while self.__param['page'] <= self.num_page:
            responce = self.get_requests()
            self.vacancies.extend(responce)
            self.__param += 1

        return self.vacancies


class SuperJobAPI(AbstractAPI):
    """Класс выгрузки информации по API с сайта SuperJob.ru"""

    def __init__(self, vacancy: str):
        self.vacancy = vacancy
        self.vacancies = []
        self.__url = 'https://api.superjob.ru/2.0/vacancies'
        self.__key = 'objects'
        self.__param = {'keyword': self.vacancy,
                        'page': 0,
                        'count': 100
                        }
        self.__headers = {
            'X-Api-App-Id': 'v3.r.137688818.90d115edaa0e26db393a65fa895b7d7478ae28e7.eeead9b83794b428c71f4d92b54c1b5923da3529'
        }

    @property
    def url(self):
        return self.__url

    @property
    def key(self):
        return self.__key

    @property
    def param(self):
        return self.__param

    @property
    def headers(self):
        return self.__headers

    def get_requests(self):
        data = requests.get(self.__url, headers=self.__headers, params=self.__param)
        return data.json()[self.__key]


    def get_vacancies(self):
        """Функция для вывода списка ванаксий"""
        self.vacancies = []
        self.num_page = 3

        while self.__param['page'] <= self.num_page:
            responce = self.get_requests()
            self.vacancies.extend(responce)
            self.__param += 1

        return self.vacancies

# hh = HeadHunterAPI('python')
# hh.get_requests()

# sj = SuperJobAPI('python')
# sj.get_requests()
