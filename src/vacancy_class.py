class Vacancy():
    """Класс для обработки и сравнения вакансий"""

    def __init__(self, title, employer, url, area, experience, employment, salary,
                 salary_from, salary_to, currency, portal):
        self.title = title
        self.employer = employer
        self.url = url
        self.area = area
        self.experience = experience
        self.employment = employment
        self.salary = salary
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.portal = portal

    def __gt__(self, other):
        if not other.salary_from:
            return True
        elif not self.salary_from:
            return False
        return self.salary_from >= other.salary_from

    def __str__(self):
        if self.salary is False:
            salary_from = 'не указана'
            salary_to = ''
            currency = ''

        else:
            currency = self.currency
            if self.salary_from and self.salary_from != 0:
                salary_from = f'От {self.salary_from}'
            else:
                salary_from = f''
            if self.salary_to and self.salary_to != 0:
                salary_to = f'До {self.salary_to}'
            else:
                salary_to = f''

        return f'Вакансия: {self.title}\nРаботодатель: {self.employer}\nГород: {self.area}\nURL: {self.url}\n' \
               f'Зарплата: {salary_from} {salary_to} {currency}\nОпыт: {self.experience}\n' \
               f'Занятость: {self.employment}\nВакансия с сайта: {self.portal}'


