from .base import *
import dj_database_url

DATABASES['default']['NAME'] = os.path.join('/Users/tiao/Desktop', 'db.sqlite3')

# temporary
DATABASES['default'] = dj_database_url.config()