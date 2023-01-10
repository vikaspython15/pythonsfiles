# dictionary use {} (curly braces)
# dictionary is a collection of key value pairs.
# syntex
# a= {"key":"value","harry":"code","marks":"100","list":[1,2,39]}
# a= [key]  #print karega value
# ["list"]  # print [1,2,9]
# properties of dictonary
# it is unorded
# it is mutable
# it is index
# can not contain duplicate keys

#     coaching notes

#dictionary is a data structuer used to store multiple value in a singal variable
# dictionary store data n key: valur pair 
# dictionary is a mutable/changeable
# dictonary can't contain duplicate keys but values can be duplicate
# dictonary is an unorderd collection of a data elements
#dictonary can cintain different data types
# dictonary is an iterable

#prices = {"shirt":800,"shoes":1000}
#print(prices)
#print(type(prices))
#print(prices["shirt"])     # print value of a perticular key#

#prices["shirt"] = 1200
#print(prices)
#prices=["wallet"] = 1200   # change the value of a key
#print(prices)

#nested dictionary

#prices = {"shirt":800,"shoes":1000,"phones":{"android":8000,"iphone":20000,"windows":12000}}
#print(prices)
#print(prices["shirt"])
#print(prices["phones"])
#print(prices["phones"]["android"])

#prices["phones"]["android"] =10000
#print(prices)

# dictionary methods

#prices = {"shirt":800,"shoes":1000,"phones":12000}
#prices.clear()
#print(prices)

#new_prices = prices.copy()
#print(new_prices)

#print(prices.get("shirt"))
#print(prices.items())
#print(prices.values())
#print(prices.keys())

#prices.popitem()
#print(prices)

#prices.pop("shirt")
#print(prices)

# the setdefault()# method returns the value if the iteam with the specified key.

#prices.setdefault("bracelat",00)
#print(prices)

# the fromkeys() method returns a dictionary with the specified keys and the specified value

#x = ['wallet','braclet']
#y = 0
#prices = dict.fromkeys(x,y)
# print(prices)

# the update method insert the specified items to the dictionary.

#prices.update({"wallet":300,"barcelet":500,"shirt":1000})
#print(prices)




