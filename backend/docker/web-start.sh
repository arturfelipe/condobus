#!/bin/bash
# web-start.sh

set -e

until PGPASSWORD=condobus psql -h "db" -U "condobus" -c '\q'; do
  >&2 echo "Postgres is not ready! 😴"
  sleep 1
done

>&2 echo "Postgres is up! 🤓"

./manage.py migrate
./manage.py runserver 0.0.0.0:8000
