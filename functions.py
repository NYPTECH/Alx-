#function that adds 2 numbers

def addnumbers(num1,num2) :
    total=num1+num2
    return(total)

val1=int(input('enter first number \t'))
val2=int(input('Enter second number \t'))

print ('sum of the numbers is' , addnumbers(val1,val2))


#example of a function

def my_func() :
    intx=10
print("value inside function:", x)
x=20
my_func()
print ("value outside function :",x)


