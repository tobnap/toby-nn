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

class runtext:
        def GET(self):
                text = load("text/text.txt")
                text = text.split('\n')
                randtext = str(text[(random.randint(0,len(text)))-1])
                randtext = randtext.split('|')
                red_text = randtext[0]+' '
                green_text = randtext[1]
                print(randtext)
                return render.text(red_text,green_text)
