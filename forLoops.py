a = ["banana", "apple", "pear", "blueberry", "cherry", "pineapple"]

for e in a: # is the elements of the list
    print(e)

b = [20, 30, 40, 50, 60]
total = 0

for e in b:
    total = total + e # gets sum of list
print(total)

range(1, 5) # represents a range of numbers 1-4
c = list(range(1, 5)) # converts range into list
print(c) # prints list [1, 2, 3, 4]

total_range = 0
for i in range(1, 5):
    total_range += i
print(total_range) # prints 10

print(list(range(1, 8))) # prints 1-7

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:      # if the remainder of i / 3 is 0 then continue
        total3 += i
print(total3) # 9

# compute all the multiples of 3, 5
# that are less than 100?
total4 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total4 += i
print(total4)
