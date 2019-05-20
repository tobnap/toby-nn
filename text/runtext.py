import web
import random
import linecache

render = web.template.render('html/')

class runtext:
        def GET(self):
                randtext = linecache.getline('text/text.txt', random.randint(0,100000))
                randtext = randtext.split('|')
                red_text = randtext[0]+' '
                green_text = randtext[1]
                print(randtext)
                return render.text(red_text,green_text)
