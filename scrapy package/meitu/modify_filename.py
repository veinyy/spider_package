import os
import sys
files = os.listdir('')

path=""
flag=True
for i ,name in enumerate(files):
    new_name = "%s.jpg" % str(i)
    old_name = "%s" % str(name)
    if flag:
        os.chdir(path)
        flag=False
    os.rename(old_name,new_name)

