daysofweek = {1:'monday', 2:'tuesday',3:'friday'}
Groceries = {"cucumber":43, "rice":12}
#dictionary uses uses {} 
# dict = {key:value, key2:value2, key3:value3} key can't be repeated and must be immutable. Unchangeable. 
# While Value can take the form of any data type and can be duplicated. 
print(Groceries)
daysofweek[4] = 'thursday'
daysofweek[3] = 'wednesday'
daysofweek[5] = "FRIDAY"

print(daysofweek)
print(daysofweek[4]) #use the key 4, to bring out the value from a dictionary. That is how to retrieve a value from a dictionary.
print(Groceries["rice"])

# Dictionary Methods

print(daysofweek.keys())
print(Groceries.keys())
print(Groceries.values())
print(Groceries.clear()) #this clears all the entries, both keys and values in the Groceries Variable.
print(Groceries)
print(daysofweek.get(3)) #get the value of key 3.
print(daysofweek.pop(2)) #it pop out the key(it removes the key and value) while also printing out the value.
print(daysofweek)
