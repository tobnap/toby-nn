#import numpy to do math like squares and absolute values
import numpy as np
import web
from diy.nn import w0
from diy.nn import w1

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

class rundiy:
        def POST(self):
                user_data = web.input()
                message = user_data.message
                message_array = message.split(',')
                message_int = [int(x) for x in message_array]
                # message_int = map(int, message_array)
                print("message:" + str(message))
                print("message_array:" + str(message_array))
                print("message_int:" + str(message_int))
                x = np.array([message_int])
                print("x:" + str(x))
                # input layer
                l0 = x
                # hidden layer
                l1 = nonlin(np.dot(l0, w0))
                # output layer
                l2 = nonlin(np.dot(l1, w1))
                return render.diy(l2)
