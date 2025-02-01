# 1. here myfiles are in same folder as of main.py
# when main.py and alpha.txt is in different folder then ?

# f = open('alpha.txt')
# content = f.read()
# print(content)
# f.close()
#If we use the above method then everytime we need to close the file
# so we use context managers, when we are inside the block thenfile is open and when we are outside withopen block then file is closed
#but we can still use the f variable outside  block
# print(f) will not return the content of file,  instead use print(f.read())
# f.readlines() will make a list having itmes as lines. and we can iterate over the list.
# f.readline() will give 1st line, if we use f.readline() again it will give 2nd line and so on...


reader_amount =  15
with open('alpha.txt','r') as f:
    # print(f.read())
    # lines = f.readlines()
    # # print(lines)
    # for line in lines:
    #     print(line, end ='')
    f.read()
    content =  f.read(reader_amount)
    print(content)
    content2= f.read(reader_amount)
    print(content2)
    #nothing prints because f.read() has already read entire file so nothing is left to read further hence no print
    # to take the pointer on 0th index use f.seek(index)
    f.seek(0)
    content3 = f.read(reader_amount)
    print(content3)




# print(f.closed) #true or false
# print(f.mode)
# print(f.name)


# TO READ MULTIPLE FILES AT ONES
# In order to check dir and bring files from directory import os library
import os
print(os.curdir) #print(os.curdir) will only print . (which represents the current directory) rather than the actual directory name.
print(os.getcwd()) #will print the complete directory name
dir_name = os.getcwd()
files_list =  os.listdir(dir_name)
print(files_list)
# os.listdir will give the files present inside the directory given to it
# we can pass the link or curdir for current folder
for single_file in files_list:
    if single_file.endswith('.txt'):
        with open(single_file) as f:
            print(f.read())

# TO WIRTE TO A FILE
## 'w' will over write the file
## 'a' will append the text at end of the previously written file.
# it will create a file if not existing before
with open('echo.txt' , 'w') as f:
    f.write("hello again")

with open('echo.txt') as f_1:
    print(f_1.read())

with open('echo.txt' , 'a') as f:
    f.write('\n')
    f.write('jump to new line and write hi!')

with open('echo.txt') as f_1:
    print(f_1.read())

with open('alpha.txt') as alpha:
    print(alpha.read())
    #we want to append the 5 th bullenting in the file
with open('alpha.txt' ,'a') as f:
    f.write('\n')
    f.write('5) fifth line here')
with open('alpha.txt') as a:
    print(a.read())

But here we are hardcoding to add the point what to do so that we dont hard code ?




