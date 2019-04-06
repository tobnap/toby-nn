import web
import os

urls = ('/', 'home',
        '/grid', 'grid',
        '/run', 'diy.rundiy.rundiy',
        '/text', 'text.runtext.runtext',
        '/face', 'face.runface.runface',
        '/music', 'music.runmusic.runmusic',
        '/save', 'save.save',
        '/list', 'listFiles',
        '/favicon.ico', 'icon')

app = web.application(urls, globals(), True)

render = web.template.render('html/')

def notfound():
        return web.notfound(render.dino())

app.notfound = notfound

class home:
    def GET(self):
        return render.home()

class grid:
    def GET(self):
        return render.grid()

class listFiles:
    def GET(self):
        files = os.listdir(".")
        return render.list(files)

if __name__ == "__main__":
    app.run()
