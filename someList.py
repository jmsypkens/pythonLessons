a = [3, 10, -1]
print(a)
a.append(1) # adds 1 to list
print(a)
a.append("hello") # you can mix data types in list
print(a)
a.append([1, 2]) # you can append a list with a list
print(a)
a.pop()          # removes the last item of list
print(a)         # will remove list inside list

print(a[0])             # access items in list based on index
print(a[2])             # will print -1

a[0] = 100              # way to change value of item in list
print(a)
