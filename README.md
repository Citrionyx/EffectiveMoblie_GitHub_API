# GitHub API Test

## Описание
Этот проект предназначен для автоматического тестирования работы с GitHub API на Python. Скрипт создает публичный репозиторий, проверяет его наличие и удаляет его.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Citrionyx/EffectiveMoblie_GitHub_API
    cd EffectiveMoblie_GitHub_API
2. Создайте и активируйте виртуальное окружение (опционально):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate+
3. Установите зависимости:
    ```bash
   pip install -r requirements.txt

4. Переименуйте файл .env.example в .env и заполните его:
   ```bash
   mv .env.example .env
   ```
   - GITHUB_USERNAME: ваш GitHub username.
   - GITHUB_TOKEN: ваш GitHub персональный токен (с правами на создание и удаление репозиториев).
   - REPO_NAME: имя репозитория для тестирования (например, test-repo).

## Запуск теста
Запустите скрипт test_api.py:
   ```bash
   python test_api.py
   ```
После запуска скрипт создаст новый репозиторий на GitHub, проверит его наличие и удалит его.

## Важные замечания

- Не забудьте удалить созданные репозитории вручную, если тест завершился неудачно.
- Токен GitHub должен иметь права на создание и удаление репозиториев.
