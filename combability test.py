xt = int(input("unique elements of the 1st vector, X: "))
a = int(input("total elements of the 1st vector, A: "))
yt = int(input("unique elements of the 2nd vector, Y: "))
b = int(input("total elements of the 2nd vector, B: "))
lst = [x for x in (xt, yt, a, b) if x <= 0] # lst = []
# LIST comprehension
print (lst)
if lst:
    print('one of the vectors length < 0, stopping')
    exit()
else:
    print('continuing')
if xt*b != yt*a:
    print('vectors wont combine into an array while keeping the average')
    exit()
else:
    print('vectors will combine into an array while keeping the average')

v1,v2 = [],[]

m1 = [0] * (xt + 1)
m2 = [0] * (yt + 1)
#############################

def hurrdurr():
    for i in range(xt+1):
        m1.append(0)
    x = int(input("number to start 1st vector from: "))
    print("1st vector:")
    for i in range(xt):
        m1[i] = int(input("how many times element {} is encountered in the vector: ".format(x)))
        if m1[i] < 1:
            raise RuntimeError("multiplier < 1, stopping!!")
        else:
            v1.extend([x] * m1[i])
    #        for j in range(m1[i]):
    #            v1.append(x)
        x = x+1
    l1 = len(v1)
    print("2nd vector real length is {}".format(l1))
    print("2nd vector length was {}".format(a))
    if a != l1:
        print("incorrect multipliers!!")
        exit()
    print("all ok")
    print("first array")
    print(v1)

#############################

for i in range(yt+1):
    m2.append(0)
y = int(input("number to start 2nd vector from: "))
print("2nd vector:")
for i in range(yt):
    m2[i] = int(input("how many times element {} is encountered in the vector: ".format(y)))
    if m2[i] < 1:
        print("multiplier < 1, stopping!!")
        exit()
    else:
        for j in range(m2[i]):
            v2.append(y)
            j = j+1
    i, y = i+1, y+1
l2 = len(v2)
print("2nd vector real length is {}".format(l2))
print("2nd vector length was {}".format(b))
if b != l2:
    print("incorrect multipliers!!")
    exit()
print("all ok")
print("second array")
print(v2)

#############################

print('2d array')

for i in range(l1):
    for j in range(l2):
        print(v1[i],v2[j])


