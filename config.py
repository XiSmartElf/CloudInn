import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'lancancook'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '777362452368392',
        'secret': '7156e16528d4c549133e8619e116202a'
    }
}
