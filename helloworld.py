print("Hello, World! 1");
print("Hello, World! 2");
print("Hello, World! 3");


if 5 > 2: print("Five is greater than two!")


# 에러남 반드시 공백이 필요함
"""
코멘트블럭
"""
if 5 > 2: 
    print("Five is greater than two!...")

##--------------------------------------------------
x = 5
y = "John"
print(10 + x)  # 10 + 5 = 15
print("y >"+y)

xx = 4 # x is of type int
xx = "Sally" # x is now of type str
print("xx >"+xx)

str_x = "Python is "
str_y = "awesome"
str_z = str_x + str_y
print("String concate ...>" + str_z)

i_x = 5
s_y = "John"
#print(i_x + s_y)  #This case will error, TypeError: unsupported operand type(s) for +: 'int' and 'str'


#-----------------------------------------------------
x_01 = 1    # int
y_01 = 2.8  # float
z_01 = 1j   # complex
print(type(x_01))
print(type(y_01))
print(type(z_01))


#---------------------------------------------------------
#PYTHON Casting

x_02 = int(1)   # x will be 1
y_02 = int(2.8) # y will be 2
z_02 = int("3") # z will be 3

x_03 = float(1)     # x will be 1.0
y_03 = float(2.8)   # y will be 2.8
z_03 = float("3")   # z will be 3.0
w_03 = float("4.2") # w will be 4.2

x_04 = str("s1") # x will be 's1'
y_04 = str(2)    # y will be '2'
z_04 = str(3.0)  # z will be '3.0'

print(x_02)
print(y_02)
print(z_02)
print("------------------------------------")
print(x_03)
print(y_03)
print(z_03)
print(w_03)
print("------------------------------------")
print(x_04)
print(y_04)
print(z_04)
print("------------------------------------")


#============================================================================================================================

#Example
#Get the character at position 1 (remember that the first character has the position 0):
a_05 = "Hello, World!"
print(a_05[0])
print(a_05[1])
print(a_05[2])

#Example
#Substring. Get the characters from position 2 to position 5 (not included):
b_06 = "Hello, World!"
print(b_06[2:5])

#Example
#The strip() method removes any whitespace from the beginning or the end:

a_07 = " Hello, World!     000         "
print("["+a_07.strip()+"]") # returns "Hello, World!"

#Example
#The len() method returns the length of a string:
a_08 = "Hello, World!"
print(len(a_08))

#Example
#The lower() method returns the string in lower case:
a_09 = "Hello, World!"
print(a_09.lower())

#Example
#The upper() method returns the string in upper case:
a_10 = "Hello, World!"
print(a_10.upper())

#Example
#The replace() method replaces a string with another string:
a_11 = "Hello, World!"
print(a_11.replace("H", "J"))

#Example
#The split() method splits the string into substrings if it finds instances of the separator:

a_12 = "Hello, World!,split, test, is workedt..., hahahah"
print(a_12.split(",")) # returns ['Hello', ' World!']

#===========================================================================================
#Python allows for command line input.
print("Enter your name:")
x_13 = input()
print("Hello, ", x_13)


#==========================================================================================
#
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1]) #banana
print(thislist[2]) #cherry

#Chage item value
thislist[1] = "blackcurrant"
print(thislist)

#Print all items in the list, one by one:
for x_14 in thislist:
  print(x_14)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Print the number of items in the list:
thislist_15 = ["apple", "banana", "cherry","asdf","asdf"]
print(len(thislist_15))

#Add Items
#Using the append() method to append an item:
thislist.append("orange")
thislist.append("watermellon")
thislist.append("ttomato")
print(thislist)

#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)  #<-- error keyword alsoe delete


#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print('----clear completely --- start')
print(thislist)
print('----clear completely --- end')

#----------------- end of file -------

#########