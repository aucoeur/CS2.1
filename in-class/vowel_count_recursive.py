'''Write a recursive function called vowel_count() to count the number of vowels in a given string, for example:
If you give vowel_count() the string “makeschool” it will return 4
'''

def vowel_count(word, count=0):
  # print(word[1:])
  
  #   if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    # count +=1
  
  # cleaner way
  vowels = "aeiou"
  if word[0] in vowels:
      count += 1

  # base case
  if len(word) == 1:
    return count
  # recursive case
  else:    
    return vowel_count(word[1:], count)

print(vowel_count("makeschool"))#should print 4
print(vowel_count("dsfgh"))#should print 0
print(vowel_count("a"))#should print 0