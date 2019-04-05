import os
import sys
import urllib.parse as urlparse

# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')

try:

    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}

    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])

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

        print(DATABASES)
        
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'

        mydb = mysql.connector.connect(user=DATABASES['USER'], password=DATABASES['PASSWORD'],
                              host=DATABASES['HOST'],
                              database=DATABASES['NAME'])
        mycursor = mydb.cursor()

        mycursor.execute("SHOW TABLES")

        for x in mycursor:
          print(x)

        sql = "INSERT INTO weights (name, w0, w1) VALUES (%s, %s, %s)"


        mycursor.executemany(sql, val)

        mydb.commit()


                    
except Exception:
    print('Unexpected error:', sys.exc_info())
