
cook=''
cook=cook.replace(' ','')
cookies=cook.split(';')
file=open('input.txt','w')
for var in cookies:
    file.write(var)
    file.write('\n')
file.close()

file=open('input.txt','r')
file_output = open("output.txt", "w")
list = {}
temp_list = file.readlines()
for var in temp_list:
    list[var.split('=')[0]] = var.split('=')[1].replace('\n','')
for key in list.keys():
    str = "'%s':'%s', \n"% (key,list[key])
    file_output.write(str)
file.close()
file_output.close()

file.close()


