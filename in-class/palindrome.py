# write recursive function for ispalindrome

def ispalindrome(my_string):
  # base case
  if len(my_string) < 2:
    return True
  if my_string[0] != my_string[-1]:
    return False
  # recursive
  return ispalindrome(my_string[1:-1])

print(ispalindrome("tacocat")) #should print True
print(ispalindrome("hello"))#should print False