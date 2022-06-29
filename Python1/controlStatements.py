# control statement
n = 45
if n > 40:
    print(n)

n = input("ENTER YOUR NUMBER")
x = int(n)
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("value is zero")

# loops . 1 is included 6 is excluded
for i in range(1, 6):
    print(i)

# move in opposite direction for loop . 10 included 0 excluded. -1 means j--
print("moving in opposite direction")
for j in range(10, 0, -1):
    print(j)

# sum of elements in list
print("sum of all values in list is ", end='')
list = [1, 2, 3, 4]
s = 0
for x in list:
    s = s + x

print(s)

# while loop
print("beginning while loop")
i = 0
while (i <= 10) :
    print(i)
    i += 1
