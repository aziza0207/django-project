
1. Скопируйте проект набрав команду git clone <ссылка на проект>
2. Для запуска приложения переименуйте файл example.env в .env, где находятся переменные среды
3. В терминале наберите команду для создания образов docker build .
4. Для миграций наберите в терминале команду  docker-compose run --rm django sh -c "python3 manage.py makemigrations" и
docker-compose run --rm django sh -c "python3 manage.py migrate"
5. Для запуска запуска контейнеров наберите команду "docker-compose up"
