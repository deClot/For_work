f=open('test.dat', 'r')

while (True):
    str1=f.readline()
    print (str1)
    print (str1.isdigit())
    if len (str1)==0:
        break
