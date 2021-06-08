x = 1                 #int 
y = 2.5               # float
yname = 'Collins'     #string
is_cool = True        #booleon

#multiple assignment
x, y, name, is_cool = (1, 2.5, 'Brad', True)
print (x, y, name, is_cool)

#Basic math
a = x + y 
#print(a)

# Check type
print(type(x))

# Casting
x = str(x)     #Changing it to string
y = int(y)      #change float to interger
#Check type
print(type(x))
print(y)    #it will turn into 2 from 2.5