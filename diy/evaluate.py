import web
import mysql.connector
from cleardb import user
from cleardb import password
from cleardb import host
from cleardb import database

render = web.template.render('html/')

class evaluate:
    def GET(self):
        from web import form
        mydb = mysql.connector.connect(user=user, password=password, host=host, database=database)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT `index`, name1, name2 FROM weights")
        names = mycursor.fetchall()
        mycursor.close()
        models = []
        for row in names :
            models.append((row[0], row[1] + ' vs ' + row[2]))
            print(row[0], row[1], row[2])

        print(models)
        myform = form.Form( 
            form.Dropdown('Model', models))

        form = myform()
        return render.evaluate(form)
