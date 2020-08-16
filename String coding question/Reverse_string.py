# write a program to reverse given string.

#This is a first method
s=input("Enter the string")
output = s[::-1]
print(output)

#This is a second method
s=input("Enter the string")
r=reversed(s)
output=''.join(r)
print(output)

#This is a third method
s=input("Enter any string")
output=''
i = len(s)-1
while i>=0:
	output+=s[i]
	i=i-1
print(output)
