friends = ["apple", "orange", "banana", 6, 3443.93, False]

print(friends[0])

friends[0] = "changed list"
#unlike strings lists are mutable
print(friends[0])

friends.append("new element at the end")
print(friends)


list  = [6,3,1,33,67,70]
list.sort()
print(list)