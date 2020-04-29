#example of while loop

total = 0
j = 1
while j < 5:
    total += j
    j += 1
print(total) # prints 10

# while loops are great for when you dont
# know how many loops you need to use

given_list = [5, 4, 4, 3, 1, -2, -3, -5] # find sum of only positive nums
total2 = 0
i = 0  # sets the index

while given_list[i] > 0:
    total2 += given_list[i] # total2 = total2 + given_list[i]
    i += 1
print(total2)  # prints the sum of all the positive numbers in given_list
               # the sum is 17


# what happens if the list is only positive numbers?

given_list2 = [5, 4, 4, 3, 1] # find sum of only positive nums
total3 = 0
f = 0  # sets the index

# you have to add a condition to the while loop so you dont
# get a list indedx out of range error
while f < len(given_list2) and given_list2[f] > 0: #len() gives length of a list
    total3 += given_list2[f] # total2 = total2 + given_list[i]
    f += 1
print(total3)  # prints the sum of all the positive numbers in given_list
               # the sum is 17

# doing the same thing above with a for loop
given_list3 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list3:
    if element <= 0:
        break
    total4 += element
print(element) # -2

given_list5 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True: # True / False statments can be used
    total5 += given_list5[i]
    i += 1
    if given_list5[i] <= 0:
        break
print(total5)
