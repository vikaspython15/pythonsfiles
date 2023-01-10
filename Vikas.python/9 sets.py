#repeated item nahi hote hai
#creating an empty sets  b = set()
#sets ke andar list ko add nhi kar skte
#sets ke andar dictionary ko bhi add nahi kar skte
#sets me index nhi hote(indexing nhi batata hai)
#there is no way to change iteam im sets
#set can't contain duplicate value
# sets ke ander unique umber aate hai # like (10,"10",10.0) tino ko print karega/n
#kyoki isme int,float,string sab hai


#   coaching notes



# set is a data structure used to store multipul valuse in a singal variable
#set is a mutable/changeable
#set can't contain duplicate values 
# set is an unorderd collection of data elements
# set can contain different data types 
#set is an iterable

#fruits = {"apple","banana","mango","orange"}
#print(fruits)
#print(type(fruits))

#set methods
#fruits.add("pineapple")
#print(fruits)

#fruits.clear()
#print(fruits)

#x = fruits.copy()
#print(x)

#fruits1 = {"apple","banana","mango","orange"}
#fruits2 = {"apple","banana","date","pineapple"}
#x = fruits1.difference(fruits2)
#print(x)

#fruits1 = {"apple","banana","mango","orange"}
#fruits2 = {"apple","banana","date","pineapple"}
#x = fruits1.symmetric_difference(fruits2)
#print(x)

#fruits1 = {"apple","banana","mango","orange"}
#fruits2 = {"apple","banana","date","pineapple"}
#fruits1.difference_update(fruits2)
#print(fruits1)

#fruits1 = {"apple", "banana", "mango", "orange"}
#fruits2 = {"apple", "banana", "date", "pineapple"}
#x = fruits1.intersection(fruits2)
#print(x)


#fruits1 = {"apple", "banana", "mango", "orange"}
#fruits2 = {"apple", "banana", "date", "pineapple"}
#fruits1.intersection_update(fruits2)
#print(fruits1)

#fruits = {"apple", "banana", "mango", "orange"}
#fruits.remove("apple")
#print(fruits)

#fruits = {"apple", "banana", "mango", "orange"}
#fruits.pop()
#print(fruits)

#fruits = {"apple", "banana", "mango", "orange"}
#fruits.discard("pineapple")
#print(fruits)

#fruits1 = {"apple", "banana", "mango", "orange"}
#fruits2 = {"apple", "banana", "date", "pineapple"}
#x = fruits1.union(fruits2)
#print(x)

#fruits1 = {"apple", "banana", "mango", "orange"}
#fruits2 = {"apple", "banana", "date", "pineapple"}
#fruits1.update(fruits2)
#print(fruits1)

