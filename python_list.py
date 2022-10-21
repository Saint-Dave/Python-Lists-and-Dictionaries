daysofweek = ['monday', 'tuesday','friday'] #list uses [] 
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[5])  # index
print(numbers[-5]) # negative indexing
# built in List functions
print(len(daysofweek)) #length
print(sum(numbers)) #sum/total of list
print(max(numbers)) # max number of list
print(min(numbers)) #minimum number 
#list slicing 
print(numbers[0:3])
print(numbers[1:7])
print(numbers[:3])
print(numbers[4:])
print(numbers[:])
print(numbers[::-1])
#list comprehension
for x in numbers :
    if x > 7:
      print(x)

Days = ['fine '+ x for x in daysofweek]
print(Days)
listComp = [x for x in numbers if x<3]
print (listComp)
# list methods
daysofweek.append('saturday')
numbers.insert(6,17) # numbers.insert(index,object) shifts and put object at index of list
print(daysofweek)
print(numbers)
numbers.insert(0,13)
numbers.insert(3,58)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse() # . is used to access the list method
print(numbers)
numbers.insert(2,7) 
numbers.insert(9,7)
numbers.insert(7,7)
numbers.insert(11,17)
print(numbers)
numbers.sort()
print(numbers)
print(numbers.count(7)) #count the no of times 7 appears in the list
numbers.insert(12,13)
print(numbers.count(17))