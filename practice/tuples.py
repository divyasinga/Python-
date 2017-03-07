# tuple_data = ('physics','chemistry', 1997, 2000)
# dog = ("Canis Famiiliaris", "dog" , "carnivore" ,12)
# print dog[2]
# for data in dog:
#     print data
# dog = dog + ("domestic",)

# dog = dog[:3] + ("man's best friend",) + dog[4:]
# print dog

# value = ("Michael", "Instructor", "Coding Dojo") # tuple packing
# (name,position,company) = value
# print name
# print position
# print company

# tuple_data = ('physics','chemistry',1997,2000)
# print len(tuple_data)

# tuple_data =('physics','chemistry','x-ray','python')
# tuple_num = (67,89,31,15)
# print max(tuple_data)
# print max(tuple_num)

# tuple_data = ('physics','chemistry','x-ray','phython')
# tuple_num = (67,89,31,15)
# print min(tuple_data)
# print min(tuple_num)
# print sum(tuple_num)
# tuple_num = (67,89,31,False,0,None)
# print any(tuple_num)
# print all(tuple_num)

# num = (1,5,7,3,8)
# for index, item in enumerate(num):
#     print(str(index)+"="+str(item))

# num = (1,5,7,3,8)
# print sorted(num)

# num = (9,1,8,2,7,3)
# print tuple(reversed(num))
import math
def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    return(c,a)

x = get_circle_area(5)

print x
