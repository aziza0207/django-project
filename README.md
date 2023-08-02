
1.Скопируйте проект набрав команду git clone <ссылка на проект>
2.В терминале наберите команду для создания образов docker build .
3. Для миграций наберите в терминале команду  docker-compose run --rm django sh -c "python3 manage.py makemigrations" и
docker-compose run --rm django sh -c "python3 manage.py migrate"
