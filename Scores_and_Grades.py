import random
import math

# random_num = random.random()
print "random_nums and Grades"
def grade():
    # print random_num

    for i in range(10):
        random_num = random.random() *100
        # print random_num
        if random_num >=60 and random_num<= 69:
            print "random_num:" ,math.floor(random_num), "Your grade is D"
        elif random_num >=70 and random_num <= 79:
            print "random_num:" ,math.floor(random_num), "Your grade is C"
        elif random_num >=80 and random_num <= 89:
            print "random_num:" ,math.floor(random_num), "Your grade is B"
        elif random_num >=90 and random_num<= 100:
            print "random_num:" ,math.floor(random_num), "Your grade is A"
        elif random_num < 60:
            print "random_num" ,math.floor(random_num),"Your grade is F"

grade()
