import os
import sys
import mysql.connector
import urllib.parse as urlparse

# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')

try:

    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}

    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'CLEARDB_DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])

        # Ensure default database exists.
        DATABASES['default'] = DATABASES.get('default', {})

        # Update with environment configuration.
        DATABASES['default'].update({
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })

        #if url.scheme == 'mysql':
        #    DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'

        mydb = mysql.connector.connect(user=DATABASES['default'].get('USER'), password=DATABASES['default'].get('PASSWORD'),
                              host=DATABASES['default'].get('HOST'),
                              database=DATABASES['default'].get('NAME'))

except Exception:
    print('Unexpected error:', sys.exc_info())
