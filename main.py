print("hello")
#print(input("Enter name"))
#comments
'''
more comments
'''
print("value is {}".format(5))

a = 5
if a < 4:
    print("Yes")
elif a == 5:
    print("Equals")
else:
    print("No")


while a >= 1:
    if a == 3:
        a = a-1
        continue
    print(a)
    a = a-1