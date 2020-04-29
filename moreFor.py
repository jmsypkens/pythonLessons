a =["<--->", "<----->", "<-------->"]
b =[">---<", ">-----<", ">--------<"]
c = ["***System Failure***", "***System Failure***"]
d = 0

while True:
    if d < 2 ** 10:
        for element in a:
            print("")
            print(element)
            print("")
        for element in b:
            print("")
            print(element)
            print("")
        for element in c:
            print("")
            print(element)
            print(element)
            print("")
        d += 1
    else:
        break

# prints a number the same amount of times as its value
z = range(1, 11)
for i in range(len(z)):
    for j in range(i + 1):
        # i = 0 -> j = 0
        print(z[i]) # 1 , 2, 2, 3, 3, 3, 4, 4, 4, 4...


total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total) #2318

# if you want to get the sum of numbers at the end of a given_list

given_list = [7,5,4,4,3,1,-2,-3,-5,-7]

total2 = 0
j = len(given_list) - 1

while given_list[j] < 0:
    total2 += given_list[j]
    j -= 1
print(total2)
