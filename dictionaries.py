"""
dic1 = {'0': '10', '1': '20'}
dic1['2'] = '30'
print ("dic1['0']: ", dic1['0'])
print ("dic1['1']: ", dic1['1'])
print ("dic1['2']: ", dic1['2'])
if "0" in dic1:
    print("0 zit erin")
del dic1['1']
if "1" not in dic1:
    print("90's cranken")
"""
"""

dic7 ={'1': '10', '2': '20'}
dic8 ={'3': '30', '4': '40'}
dic9 ={'5': '50', '6': '60'}
def Merge(dic7, dic8):
    return(dic7.update(dic8))
def Merge2(dic7, dic9):
    return(dic7.update(dic9))
print(Merge(dic7, dic8))
print(Merge2(dic7, dic9))
print(dic7)
"""

"""
def groet():
    print("hallo")
groet()
groet()
groet()
groet()
groet()
groet()
groet()
groet()
groet()
groet()
def tafel5():
    print("5, 10, 15, 20, 25, 30, 35, 40, 45, 50")
tafel5()
"""
"""
def hello(n):
    for i in range(n):
        print("hello world")
hello(6)
"""
"""
def sli(n, w):
    for i in range(n):
        print(w)
sli(4, "kip")
"""
"""
def slik(w):
    t = 0
    for i in range(len(w)):
        #print (i)
        l = ("")
        for i in range(t + 1):
            l += (w[t])
        t += 1
        print (l)
slik("cocksmuts")
"""
"""
def grootste_():
    getallen = [3, 7, 18, 5, 4, 20]
    grootste = int(0)
    rane = len(getallen)
    teller = 0
    for i in range(rane):
        getal = getallen[teller]
        if getal > grootste:
            grootste = int(getal)
        teller += 1
    print(grootste)
grootste_()
"""

"""
def reverse_string(woord):
    nieuw_woord = woord[::-1]
    print(nieuw_woord)
reverse_string("teer")
"""

"""
num = 1

if num > 1:    
   for i in range(2, num//2):
       if (num % i) == 0:
           print(num, "is geen priemgetal")
           break
       else:
            print(num, "is een priemgetal")
            break
else: 
   print(num, "is geen priemgetal") 
"""

"""
def reverse_string(woord):
    nieuw_woord = woord[::-1]
    if nieuw_woord == woord:
        print("true")
    else:
        print("false")
reverse_string("teet")
"""

"""
listo = ["we", "er", "rt", "ty", "yu", "ui", "io", "op"]
print(listo[::-1])
"""


listo = ["we", "er", "rt", "ty", "yu", "ui", "io", "op"]
teller = 0
for i in listo():
    print(teller)
    teller += 1