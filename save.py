#import numpy to do math like squares and absolute values
import web
import os

render = web.template.render('html/')

# save file
def saveFile(filename, data):
	#open the file as write
        filepath = '/saves/' + filename
	file = open(filename, 'w')
	#write all data
	file.write(data)
	#close the file
	file.close()

class save:
        def POST(self):
             user_data = web.input()
             name = str(user_data.name)
             array = str(user_data.array)
             filename = name+'.txt'
             saveFile(filename, array)
             files = os.listdir(".")
             return render.save(files)
