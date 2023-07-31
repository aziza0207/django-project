
1. Склонирйте проект набрав команду "git clone <ссылка на репозиторий>"
2. Установите зависимости набрав команду "pip install -r requiremets.txt"
3. Создайте образы набрав команду в терминале "docker-compose build"
4. Проведите миграции набрав в терминале "docker-compose run --rm django sh -c "python3 manage.py makemigrations"
5. После наберите команду "docker-compose run --rm django sh -c "python3 manage.py migrate"
6. Для запуска приложения наберите команду "docker-compose run --rm django sh -c "python3 manage.py runserver"

