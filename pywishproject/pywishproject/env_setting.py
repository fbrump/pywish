import os

DB_NAME = os.environ.get('DB_NAME', 'pywishdb')
DB_USER = os.environ.get('DB_USER', 'pywishuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'pywishpostgres')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5030')
