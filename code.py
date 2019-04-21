import web
import os

urls = ('/', 'home',
        '/evaluate', 'diy.evaluate.evaluate',
        '/train', 'train',
        '/run', 'diy.run.run',
        '/nn', 'diy.nn.nn',
        '/text', 'text.runtext.runtext',
        '/face', 'face.runface.runface',
        '/music', 'music.runmusic.runmusic',
        '/save', 'save.save',
        '/list', 'listFiles')

app = web.application(urls, globals(), True)

render = web.template.render('html/')

def notfound():
        return web.notfound(render.dino())

app.notfound = notfound

class home:
    def GET(self):
        return render.home()

#class evaluate:
#    def GET(self):
#        return render.evaluate()

class train:
    def GET(self):
        return render.train()

class listFiles:
    def GET(self):
        files = os.listdir(".")
        return render.list(files)

if __name__ == "__main__":
    app.run()
