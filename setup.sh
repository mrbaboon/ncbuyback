docker-compose build
docker-compose up -d mariadb redis mailcatcher

docker-compose run --rm ncbuyback python manage.py migrate

docker-compose up -d ncbuyback worker beat
