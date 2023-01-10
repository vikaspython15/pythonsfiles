#import time 

#locationtime = time.time()
#location = time.location(time.time())
#location = time.asctime(time.location(time.time()))
#print(localtime)

import datetime
#a = datetime.datetime.now()
#print(a)
#print(a.year)
#print(a.month)
#print(a.day)

#print(a.strftime("%a"))

today = datetime.date.today()
#print(today)

#yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
