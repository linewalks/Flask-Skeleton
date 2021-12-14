# run init_db.sh 
flask db init

python migrate.py

flask db upgrade
