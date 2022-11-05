#class list in python


x = 'ali'
x.upper()ا#اعلى
print(x)

h = [1,2,3,4]
h.append(5)#اضافة
print(h)



class Calculator:

    def sum(self,x,y):
        print(x+y)


    def mul(self,x,y):
        print(x*y)

    #constructor المنشى

    def __init__(self):#عنداخذ قيمة من الكلاس تشتغل هذه الدالة
        print('Welcom')

cl = Calculator()
#cl.sum(3,5)
#cl.mul(4,4)



#inheritance class in python

class Calculator:
    
    def sum(self,x,y):
        print(x+y)


    def mul(self,x,y):
        print(x*y)


class SciCalculator(Calculator):
    
    def power(self,x,y):
        print(x**y)

s1 = SciCalculator()
s1.sum(2,3)
s1.mul(4,5)
s1.power(2,3)



class A:
    def do(self):
        print('in A')


class B(A):
    pass



class C:
    def do(self):
        print('in C')

class D(B,C):
    pass

o1 = D()
print(D.mro())#طريقة عمل الميثود 
o1.do()



class Student:

    def __init__(self):
        self.marks =[]
        
    def print_marks(self):
        print(self.marks)

    def add_mark(self,mark):
        self.marks.append(mark)

s = Student()
s.add_mark(20)
s.add_mark(30)
s.add_mark(40)
s.add_mark(50)
s.add_mark(60)
s.print_marks()

d = Student()
d.add_mark(50)
d.add_mark(70)
d.add_mark(80)
d.add_mark(90)
d.add_mark(10)
d.print_marks()



'''  loop while  '''
print("Select Opreation: ")

print("1: Addition")
print("2: Subtract")
print("3: Multiply")
print("4: Dividu")


while True:
    choice = int(input('Enter Choice (1/2/3/4): '))

    if choice in (1,2,3,4):
       number1 = int(input("Enter First Number: "))
       number2 = int(input("Enter Second Number: "))
       if choice == 1:
           resulte = number1 + number2
           print(f"{number1} + {number2} = {resulte}")
       elif choice == 2:
            resulte = number1 - number2
            print(f"{number1} - {number2} = {resulte}")
       elif choice == 3:
            resulte = number1 * number2
            print(f"{number1} * {number2} ={resulte}")
       elif choice == 4:
            resulte = number1 / number2
            print(f"{number1} / {number2} = {resulte}")
       else:
            print("Error, Enter choice 1,2,3,4: ")
       nextcaculation = input("Let's do next caculation (yes/no)")
       if nextcaculation == "no":
            break
    else:
        print("Error")
      
