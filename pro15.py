'''
num1 = int(input("Input The Number 1 : "))
num2 = int(input("Input The Number 2 : "))

for x in range(0,1):
    x=num1%num2
    print( x )
    
'''

'''    
#طباعة من 0 الى القيمة التي يدخلها المستخدم 

num = int(input("Input The Number : "))

for i in range(0,num +1):
    print(i)

'''

#ادخال المستخدم الجملة بدون تكرار
'''
word = input("Enter the world: ")
x = word.split()
print(len(set(word)))
print(len(set(x)))
'''




'''

#Number to words

import num2word

num = int(input("Enter a number: "))
word_number = num2word.word(num)
print(word_number)

'''
