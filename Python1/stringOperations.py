#string operations
name = "hello world"
print(len(name))

print(name[0])
#include from 0th but exclude index 3
print(name[0:3])

#include from 0th but exclude index 10 jump 2 positions
print(name[0:10:2])

# get last char of string
print(name[-1])

# reverse string
print(name[-1 :: -1])

# capitalize first letter of string
print(name.capitalize())

# making title
print(name.title())

# check if digit
print(name.isdigit())