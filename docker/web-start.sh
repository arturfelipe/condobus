#!/bin/bash
# web-start.sh

set -e

until PGPASSWORD=condobus psql -h "db" -U "condobus" -c '\q'; do
  >&2 echo "Postgres is not ready - sleeping"
  sleep 1
done

>&2 echo "Postgres is up"

make migrate
make run
