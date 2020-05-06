#Write your function here
def delete_starting_evens(lst):
  while len(lst) >= 1 :
    for num in lst:
      if num % 2 == 0:
        lst = lst[1:]
    else:
        break
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
