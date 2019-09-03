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