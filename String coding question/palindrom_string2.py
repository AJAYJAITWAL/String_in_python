# Program to check if a string is palindrome or not

s = input("Enter any string")

# make it suitable for caseless comparison
s = s.casefold()

# reverse the string
rev_s = reversed(s)

# check if the string is equal to its reverse
if list(s) == list(rev_s):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")