# Python - List Methods

meyve = ["elma", "armut", "üzüm", "erik", "çilek", "karpuz"]

meyve.append("üzüm")  # Adds an element at the end of the list
print(meyve)
print(meyve.count("üzüm"))   # Returns the number of elements with the specified value
print(meyve.index("armut"))  # Returns the index of the first element with the specified value
meyve.insert(1, "kavun")
print(meyve)
meyve[3] = "kara üzüm"
print(meyve)
meyve.sort()   # Sorts the list
print(meyve)
meyve.reverse()   # Reverses the order of the list
print(meyve)
liste2 = ["şeftali", "muz"]
meyve.extend(liste2)   # Add the elements of a list (or any iterable), to the end of the current list
print(meyve)
liste3 = ["canerik", "muşmula"]
meyve.append(liste3)
print(meyve)
meyve.pop()   # Removes the element at the specified position
print(meyve)
meyve.pop(2)
print(meyve)
meyve.remove("erik")  # Removes the item with the specified value
print(meyve)
meyve.clear()   # Removes all the elements from the list
print(meyve)
del meyve
print(meyve)
