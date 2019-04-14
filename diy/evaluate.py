#import numpy to do math like squares and absolute values
import numpy as np
import web

w0 = np.loadtxt('diy/w0',delimiter=',')
w1 = np.loadtxt('diy/w1',delimiter=',')

#mycursor.execute("SELECT w0, w1 FROM weights")
#myresult = mycursor.fetchall()
#
#w0 = myresult[0]
#w1 = myresult[1]
#print(w0)

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

def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)

	return 1/(1+np.exp(-x))
    
class evaluate:
    def POST(self):
        user_data = web.input()
        message = user_data.message
        message_array = message.split(',')
        message_int = [int(x) for x in message_array]
        x = np.array([message_int])
        # input layer
        l0 = x
        # hidden layer
        l1 = nonlin(np.dot(l0, w0))
        # output layer
        l2 = nonlin(np.dot(l1, w1))
        l2 = l2.ravel()
        answer = str
        if np.array_equal(np.around(l2), [1,0,0]):
            answer = 'Tree'
            
        elif np.array_equal(np.around(l2), [0,1,0]):
            answer = 'Square'
            
        elif np.array_equal(np.around(l2), [0,0,1]):
            answer = 'Smile Face'
            
        else:
            answer = "I don't know"
            
        return render.diy(answer,l2[0]*100,l2[1]*100,l2[2]*100)
