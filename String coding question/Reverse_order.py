# write a program to reverse order of  words.

s=input("Enter string")
l=s.split()
l1=l[::-1]
output = ' '.join(l1)
print(output)