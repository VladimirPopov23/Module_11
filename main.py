# module_11_1.py
# 12.12.2024 Домашнее задание по теме "Обзор сторонних библиотек Python"

import requests
import json


def get_user_info(username):  # информация о пользователе GitHub.
    url = f'https://api.github.com/users/{username}'  # URL-адрес, выбранного аккаунта
    response = requests.get(url)  # отправляем GET-запрос
    if response.status_code == 200:  # если запрос успешен 2хх, возвращаем данные в формате .json()
        return response.json()  # возвращаем словарь с данными пользователя
    else:  # иначе выводим сообщение об ошибке
        print(f'Ошибка: {response.status_code}')
        return None  # ничего не возвращаем


def get_user_repos(username):  # список репозиториев аккаунта
    url = f'https://api.github.com/users/{username}/repos'  # URL-адрес репозиториев, выбранного аккаунта
    response = requests.get(url)  # отправляем GET-запрос
    if response.status_code == 200:  # если запрос успешен 2хх, возвращаем данные в формате .json()
        return response.json()  # возвращаем словарь с репозиториями пользователя
    else:  # иначе выводим сообщение об ошибке
        print(f'Ошибка: {response.status_code}')
        return None  # ничего не возвращаем


def get_repo_dates(username):  # дата создания и последнего изменения репозиториев
    repos = get_user_repos(username)  # из функции get_user_repos получаем список репозиториев пользователя
    if not repos:  # если список репозиториев пустой
        return None  # ничего не возвращаем
    repo_dates = []  # список для хранения информации о датах
    for repo in repos:  # циклом for перебираем репозитории
        repo_name = repo['name']  # имя репозитория
        url = f'https://api.github.com/repos/{username}/{repo_name}'  # URL-адрес названий репозиториев
        response = requests.get(url)  # отправляем GET-запрос
        if response.status_code == 200:  # если запрос успешен 2хх, возвращаем данные в формате .json()
            created_at = response.json().get('created_at', 'Неизвестно')  # дата создания репозитория (если ключ есть)
            updated_at = response.json().get('updated_at', 'Неизвестно')  # дата изменения репозитория (если ключ есть)
            repo_dates.append(
                {'name': repo_name, 'created_at': created_at, 'updated_at': updated_at})  # добавляем в список
        else:  # В случае ошибки пропускаем репозиторий
            print(f'Ошибка при запросе репозитория {repo_name}: {response.status_code}')
    return repo_dates  # возвращаем список для хранения информации о датах


if __name__ == '__main__':
    username = 'VladimirPopov23'  # имя пользователя GitHub (при желании можно задать другое)

    # Получение информации о пользователе
    user_info = get_user_info(username)
    if user_info:
        print('Информация о пользователе:')
        print(f'Логин: {user_info['login']}')
        print(f'Имя: {user_info.get('name', 'Не указано')}')
        print(f'Количество репозиториев: {user_info['public_repos']}')

    # Получение дат создания и последнего изменения для каждого репозитория
    repo_dates = get_repo_dates(username)
    if repo_dates:
        print('\nДаты создания и последнего изменения репозиториев:')
        for repo in repo_dates:
            print(f'Репозиторий {repo['name']}:')
            print(f'Дата создания: {repo['created_at']}')
            print(f'Последнее изменение: {repo['updated_at']}\n')
