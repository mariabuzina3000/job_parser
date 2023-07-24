from src.api_classes import HeadHunterAPI, SuperJobAPI
from src.json_class import WorkFile


def job_selection():
    vacancy = input(f'Выберите нужную вакансию: ').lower()
    return vacancy


def data_search(vacancy):
    """Загрузка информации с сайтов для поиска работы """

    user_input = input(f'Выберите нужный ресурс:\n'
                       f'1 - поиск на сайте hh.ru\n'
                       f'2 - поиск на сайте superjob.ru\n'
                       f'3 - поиск на hh.ru и superjob.ru\n'
                       f'Ваш выбор: '
                       )

    if user_input == '1':
        hh = HeadHunterAPI(vacancy)
        converted_vacancies = hh.validate_vacancies()
    elif user_input == '2':
        sj = SuperJobAPI(vacancy)
        converted_vacancies = sj.validate_vacancies()
    else:
        hh = HeadHunterAPI(vacancy)
        sj = SuperJobAPI(vacancy)
        converted_vacancies = hh.validate_vacancies()
        converted_vacancies.extend(sj.validate_vacancies())

    return converted_vacancies


def main():
    print("Привет!")
    vacancy = job_selection()
    converted_vacancies = data_search(vacancy)
    print(f'Найдено: {len(converted_vacancies)} вакансий \n\n')

    wf = WorkFile(vacancy, converted_vacancies)

    choise_filtred = input(f'Вы можете фильтровать вакансии, выбрав одно из значений:\n'
                           f'1 - по городу\n'
                           f'2 - по работодателю\n'
                           f'3 - не фильтровать\n'
                           f'Ваш выбор: '
                           )

    if choise_filtred == '1':
        filter_field = 'area'
        filter_value = input('Введите название города: ').lower()
        vacancies = wf.filtred_vacancies(filter_field, filter_value)
    elif choise_filtred == '2':
        filter_field = 'employer'
        filter_value = input('Введите название работодателя: ').lower()
        vacancies = wf.filtred_vacancies(filter_field, filter_value)
    else:
        vacancies = wf.not_filtred_vacancies()

    choise_sorted = input(f'Вы можете сортировать вакансии, выбрав одно из значений:\n'
                          f'1 - по минимальной зарплате по убыванию\n'
                          f'2 - по максимальной зарплате по убыванию\n'
                          f'3 - не сортировать')

    if choise_sorted == '1':
        vacancies = sorted(vacancies, reverse=True)
    elif choise_sorted == '2':
        vacancies = sorted(vacancies, key=lambda x: x.salary_to if x.salary_to else 0, reverse=True)

    for vacs in vacancies:
        print(vacs, end='\n\n')

    print(f'Подобрано вакансий: {len(vacancies)}')


if __name__ == '__main__':
    main()