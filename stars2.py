# def draw_stars(x):
#     for i in x:
#         print i
#         if isinstance(i,basestring):
#             print i[0][0].lower
#         else print x[i]
#
# k =[9,8,"tom",7]
# draw_stars(k)

def draw_stars(x):
    for i in range(0,len(x)):
        y = x[i]
        # print y
        if isinstance(x[i],basestring):
            print x[i][0].lower() * len(x[i])
        else:
            print y

k = ["foc","Tom","Jim", 9 ,8]
draw_stars(k)
