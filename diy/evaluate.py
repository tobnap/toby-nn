import web
import mysql.connector
from cleardb import mydb

render = web.template.render('html/')

class evaluate:
    def GET(self):
        from web import form
        mycursor = mydb.cursor()
        mycursor.execute("SELECT `index`, name1, name2 FROM weights")
        names = mycursor.fetchall()
        models = []
        for row in names :
            models.append((row[0], row[1] + row[2]))
            print(row[0], row[1], row[2])

        print(models)
        myform = form.Form( 
            form.Dropdown('Models', models))

        form = myform()
        return render.evaluate(form)
    
    #def GET(self):
    #    modelsList = [[22,"name 1", "name 2"] ,[25, "name 3", "name 4"]]
    #    return render.evaluate(modelsList)
