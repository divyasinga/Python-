# str = "If monkeys like bananas, then I must be a monkey"
# x = str.find('monkey')
# print x
# y = str.replace('monkey','alligator')
# print y

# x = [2,54,-2,7,12,98]
# print min(x)

# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:len(x)/2]
z = x[len(x)/2:]

print y , z
z.insert(0,y)
print z
