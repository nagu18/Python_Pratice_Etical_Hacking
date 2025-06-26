import os
x = input('enter upgrade or update linux:- ')
if (x == 'update'):
    os.system('apt update -y  && echo done') 
elif  (x == 'update'):
    os.system('apt upgrade -y  && echo done') 
elif (x == 'exit'):
    print('exit from this program..')

