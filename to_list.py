items=""
def getexp():  #get an expression from the user
	"""return and discard the next expression,along with any nested ones in the input"""
	res=gettoken()
	if res!='(': return res
	a=[]
	while 1:
		b=getexp()
		if b==')': return a
		a.append(b)

def gettoken():
	"""return and discard the next symbol,number or special character in input"""
	while nextchar() <=' ':getchar() #skip whitespace
	a=getchar()
 	if a in ['(',')'] : return a
  	while nextchar() !=')' and nextchar()!=' 'and nextchar()!='\n':
  		a = a + getchar()
	return a

def input():
	"""get the input expression and return in the form of string"""
	global items
	items=raw_input("Enter the expression: ")+ '\n'
	return items

def  nextchar():
	""" return the next character,and get the input from the user if needed"""
	global items
	if items =="":	
		input()
	return items[0:1]

def getchar():
	""" return and discard the next character in the input stream"""
	global items
	c = nextchar()
	items = items[1:]
	return c   

