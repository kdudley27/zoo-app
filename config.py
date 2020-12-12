import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('zoo-app.database.windows.net') or '[zoo-app.database.windows.net]'
    SQL_DATABASE = os.environ.get('zoo-app') or '[zoo-app]'
    SQL_USER_NAME = os.environ.get('kevin') or '[kevin]'
    SQL_PASSWORD = os.environ.get('Dudley123') or '[Dudley123]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('zooapp') or '[zooapp]'
    BLOB_STORAGE_KEY = os.environ.get('gzuIGFBudDAoNnsYDZUC21fFMpe6FrZiO7cCZYHltuwvbW0J6z7d1C++au8k9CnK6ME/7Qi6p37Fsn3vvzuCTw==') or '[gzuIGFBudDAoNnsYDZUC21fFMpe6FrZiO7cCZYHltuwvbW0J6z7d1C++au8k9CnK6ME/7Qi6p37Fsn3vvzuCTw==]'
    BLOB_CONTAINER = os.environ.get('images') or '[images]'
