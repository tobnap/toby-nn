import web
import random

render = web.template.render('html/')

# load into memory
def load(filename):
	#open the file as read only
	file = open(filename, 'r')
	#read all text
	text = file.read()
	#close the file
	file.close()
	return text

class runface:
        def GET(self):
                links = load("face/links.txt")
                links = links.split('\n')
                randlink = str(links[(random.randint(0,len(links)))-1])
                return render.face(randlink)
