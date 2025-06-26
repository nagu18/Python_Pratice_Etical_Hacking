import os
os.system('''who | awk '{print $1}' | grep '^nagu$' | uniq''')
