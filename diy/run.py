import web
import mysql.connector
import numpy as np
import simplejson as json
from cleardb import mydb

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
    
class run:
    def POST(self):
        user_data = web.input()
        message = user_data.message
        message_array = message.split(',')
        message_int = [int(x) for x in message_array]
        index = user_data.Models
        mycursor = mydb.cursor()
        mycursor.execute("SELECT w0, w1 FROM weights where `index` = " + str(index))
        weights = mycursor.fetchall()
        mycursor.close()
        w0 = None
        w1 = None
        for row in weights :
            w0 = np.array(json.loads(row[0]))
            w1 = np.array(json.loads(row[1]))
            #print(row[0])
            #print(row[1])
        print(w0)
        print(w1)
        x = np.array([message_int])
        print(x)
        # input layer
        l0 = x
        # hidden layer
        l1 = nonlin(np.dot(l0, w0))
        # output layer
        l2 = nonlin(np.dot(l1, w1))
        l2 = l2.ravel()
        answer = str
        if np.array_equal(np.around(l2), [1,0]):
            answer = 'Tree'
            
        elif np.array_equal(np.around(l2), [0,1]):
            answer = 'Square'
            
        else:
            answer = "I don't know"
            
        return render.diy(answer,l2[0]*100,l2[1]*100)
