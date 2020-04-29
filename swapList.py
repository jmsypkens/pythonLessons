# swapping banana with microsoft in list

b = ["banana", "apple", "microsoft"]
temp = b[0]
b[0] = b[2]   # banana is now in b[2]
b[2] = temp
print(b)

# shortcut is to use tuple
# lets reverse list back to original using tuple

b[0], b[2] = b[2], b[0] # using tuple to swap vales in list
print(b)
