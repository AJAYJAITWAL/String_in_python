# write a program to print the character present at even index and odd index seperatly for the given string.

s = input("Enter the string")
print("Character present at Even Index:")
i=0
while i<len(s):
	print(s[i])
	i=i+2
print("Character present at Odd Index:")
i=1
while i<len(s):
	print(s[i])
	i=i+2