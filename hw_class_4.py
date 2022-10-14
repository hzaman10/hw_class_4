'''
#  5 (Five) Functions
print('Assignment -1')

def my_fun():
    print ('I am in function')
   
my_fun()  

#---------------------------------------------
print('Assignment -2')

def fun_add(a,b):
    return a+b
x=int(input('Please enter the value of x : '))
y=int(input('Please enter the value of y : '))
print ('Sum of ' + str(x) + ' and ' + str(y) + ' : ' + str(fun_add(x,y)) )

#---------------------------------------------
print('Assignment -3')
def my_sq(a):
    return a*a

print(my_sq(3))

#---------------------------------------------
print('Assignment -4')
def my_sq(a):
    return a*a

for i in range(1,10,1):
    result=my_sq(i)
    print(result)

#---------------------------------------------

print('Assignment -5')
def fun_recursion(i):
    if(i > 0):
        r=i+fun_recursion(i-1)
        print(r)
    else:
        r = 0
    return r
fun_recursion(6)   
#---------------------------------------------
'''

print('Assignment -6')
def sum_total(*ar):
    sum=0
    for i in ar:
        sum=sum+int(i)
    return sum

print(sum_total(4,6,7,8,4))  
#---------------------------------------------

print('Assignment -7')

def my_name(**name):
    print("Har first name is : " + name["f_name"])
    print("Har last name is : " + name["l_name"])

my_name(f_name = "Shaira", l_name = "Tahsin")
    
#---------------------------------------------

print('Assignment -8')

def my_add(**arg):
    s = 0
    for i in arg:
        s = s + arg[i]
    return s

total = my_add(a=54,b=67,c=23,d=46,e=10,f=50)
print('Sum is : ',total)

#----------------------Calculator using Function-----------------------

print('Assignment -9')

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multiplication(a,b):
    return a*b  

def division(a,b):
    if b!=0:
        return a/b
    else:
        return 0
    
x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(add(x,y))
    
  elif(z=='-'):
    print(sub(x,y))
  
  elif(z=='*'):
    print(multiplication(x,y))
  
  elif(z=='/'):
    print(division(x,y))
  
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")



