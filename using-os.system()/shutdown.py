import os
while True:
    x=input('enter shutdown to turn of the pc or no shutdown:- ')
    if x.lower() == 'shutdown':
        os.system('shutdown /s /f /t 0')
    elif (x.lower() == 'no shutdown'):
        print('not shutdown the pc ...')
        break