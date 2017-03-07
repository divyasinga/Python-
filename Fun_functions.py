# def odd_even():
#     for count in range(1,2000):
#         if(count % 2 != 0):
#             print "Number is " +str(count),". "  , "This is an odd number."
#         elif(count % 2 == 0):
#             print "Number is " +str(count),". " , "This is an even number."
#         count +1
# odd_even()

# ---multiply

def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr

x=[7,3]
y = multiply(x,5)
print y
