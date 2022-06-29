#lists
marks = [2,5,9,10,12,7,"india"]
print(marks)

print(marks[0])

# deleting element at index 1
del marks[1]

print(marks)

another_list = ["india","australia","new zealand","south africa","england"]
print((another_list[0:3]))
another_list.append("pakistan")
print(another_list)
another_list.insert(0,"bangladesh")
print(another_list)

# print length
print(len(another_list))
another_list.remove("australia")

#after removing australia
print(another_list)

list = [13,57,12,89,1]
print(min(list))
print(max(list))

#looping through list
print("looping through list")
for x in list :
    print(x)

# reversing the list
list.reverse()
print(list)