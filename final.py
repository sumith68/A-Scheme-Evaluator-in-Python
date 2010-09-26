import types
from opns import *
from operator import *
import to_list 		# this "to_list" converts the input expression to list for processing

storage={}
def converter():
	""" get the input from the user convert it into list"""
	arg=to_list.getexp()
	return arg
	
def evaluator(arg):
	""" evaluation and arithmetic operations are taken place"""
	if type(arg)==types.ListType:
		f1=first(arg)
		if f1=='+':
			fun=add
		elif f1=='-':
			fun=sub
		elif f1=='*':
			fun=mul
		elif f1=='/':
			fun=div
		elif f1=='>':
			fun=gt
		elif f1=='<':
			fun=lt
		elif f1=='=':
			fun=eq
		elif f1=='>=':
			fun=ge
		elif f1=='<=':
			fun=le
		f=evaluator(arg[1])
		for each in arg[2:]:
			f=fun(f,evaluator(each))
		return f
	elif arg.isalpha():
		return int(storage[arg])
	else:
		return int(arg)
def check(arg):
	""" check the "if" condition and "if" condition with 'and' or 'or' and 
	    check if it is a method or not""" 
	
	
	if not type(arg) ==types.ListType and arg in storage:
		return int(storage[arg])	
	
	if first(arg)=='if':
		
		if arg[1][0]=='and':
			for each in arg[1][1:]:
				if not evaluator(each) :
					return evaluator(arg[-1])
			else:
			 	return evaluator(arg[-2])
		elif arg[1][0]=='or':
			for each in arg[1][1:]:
				if evaluator(each) :
					return evaluator(arg[-2])
			else:
				return evaluator(arg[-1])
		
		else:
			if not evaluator(arg[1]):
				return check(arg[3])
			else:
				return check(arg[2])
				
				
	elif first(arg)=='define':	
			storage[arg[1]]=arg[2]			
	elif first(arg) in storage:
			
			temp=storage[arg[0]]
			if temp[0]=="lambda":
				i=1
				for each in temp[1]:
					storage[each]=evaluator(arg[i])
					i=i+1
				return check(temp[2])	
			else :
				i=1
				for each in temp[0]:
					storage[each]=evaluator(arg[i])
					i=i+1
				return check(temp[1])
			
	else:
		return evaluator(arg)

def main():
	try:
		while 1:	
			arg=converter()
			c=check(arg)
			print c
	except:
		print "-----end-----"

if __name__ == "__main__":
	main()
