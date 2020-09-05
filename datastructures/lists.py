l = []
print(l)

print("append 4 and 9")
l.append(4)
l.append(9)
print(l)

print("extend with itsself")
l.extend(l)
print(l)

print("insert 16 at index 1")
l.insert(1, 16)
print(l)

print("remove first element with value 9")
l.remove(9)
print(l)

print("remove last element with list.pop()")
l.pop()
print(l)

print("remove element with index 1 using list.pop(index)")
l.pop(1)
print(l)

print("count elements with value 4")
print(l.count(4))

print("append elements")
l.append(2)
l.append(9)
l.append(6)
l.append(10)
l.append(12)
print(l)

print("sort list in reverse")
l.sort(reverse=True)
print(l)

print("reverse the list")
l.reverse()
print(l)

print("return index of first 4 in list")
print(l.index(4))

print("extend list")
l.extend(l)
print(l)

print("return index of first 4 after 5th element in list")
print(l.index(4, 6))

print("copy list l to list l_2")
l_2 = l.copy()
print(l)
print(l_2)

print("clear list l")
l.clear()
print(l)






