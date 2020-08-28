from collections import OrderedDict, Counter
c=Counter("aaaaaaaaaaaaaaagjhjkskskkkkkkkkkkkksh")
d=c.popitem
# print(d)
network={}
network['me']=["John", "Tom"]
network["Tom"]=["Sean", "Jim"]
new=OrderedDict(network)
print(new)
newer=new.popitem()
print(newer)
# print(new)
# for index, value in network.items():
#     print(value)
# print(network["me"][0])