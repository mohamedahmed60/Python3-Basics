'''
username = 'mahmoud'

if username == 'mahmoud':
    print('welcom')


elif username == 'ali':
    print('welcom ali')


elif username == 'hassan':
    print('welcome hassan')

else:
    print('you have to reset your password')
'''

#condition
'''
x = 100

if x < 200:
    print('x < 200')

    if x < 50:
        print('x > 50')

    else:
        print('x > 50')
else:
    print('___________________')
'''

'and  ,   or'
'''
username = 'mohamed'
password = 12345

#يجب ان يحقق جميع الشروط

if username == 'mohamed' and password == 123456:
    print('welcom')
#اذ تحقق شرط واحد
    
elif username == 'mohamed' or password == 123456:

    print('welcom')
else:
    print('your have to reset your pass')
'''
# if all(تاخذ قيمة واحده فقط )
# all تكون بديل لا and ولاتاخذ الاقمية واحده

'''
x = 2
y = 3
z = 4

if any([x == 2 , y == 3 , z == 4]):
    print('Done')

# any تكون بديل الا or اذا تحقق شرط واحد فقط فانها تنفذ

'''

'''
x = 100
if x == 100:
    print('Done')
else:
    print('not done')

# Ternary Operator
# True Condition False  

print('Done') if x == 100 else print('not done')

'''











