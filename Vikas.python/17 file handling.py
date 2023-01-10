#open()
#filemode
#x - Create File 
#a - Append File
#w - Write File
#t - Text mode (Default)
#r - Read Mode (Default)

#Creating a file 
#f = open("myfile.txt",'x')
#f.close()

#Reading a file 
#f = open("myfile.txt",'w')
#f.write("This is a file and i am writing this file.")
#f.close()

#Reading a file 
#f = open("myfile.txt",'r')
#content = f.read()
#print(content)
#f.close()

#Appending a file 
#f = open ("myfile.txt",'a')
#f.write("\nThis is a file and I am writing this file.")
#f.close()

#Ready line by line 
#f = open("myfile.txt", 'r')
#for line in f:
#    print(line)
#    f.close()

#f = open ("myfile.txt",'r')
#print(f.readline())
#print(f.readlines())
#f.close()