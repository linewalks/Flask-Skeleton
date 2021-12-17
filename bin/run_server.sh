flask db upgrade

gunicorn -w 1 -b "0.0.0.0:$1" "main:create_app()"
