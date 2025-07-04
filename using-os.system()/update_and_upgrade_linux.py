import os
x = input('enter upgrade or update linux:- ').strip().lower()
if (x == 'update'):
    os.system('apt update -y  && echo done') 
elif  (x == 'upgrade'):
    os.system('apt upgrade -y  && echo done') 
elif (x == 'exit'):
    print('exit from this program..')
else:
    print('invalid error')
