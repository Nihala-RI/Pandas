print("welcome to python")
print(123)

#variables

num=123 #number
print(num)

numfloat=12.34 #float
print(numfloat)

numcomplex=1+2j #complex number
print(numcomplex)

name="python" # string
print(name)

nameboolean=False# boolean
print(nameboolean)

li=[1,"python",True,4.6,5+3j] # list
print(li)

tu=(1,"python",True,4.6,5+3j) # tuple
print(tu)

di={"name":"python","version":3.10,"downloaded":True} # dictionary
print(di)

set1={1,2,3,4,5} # set
print(set1)

a="hello world"
print(a[0]) #indexing

print(a[4])

print(a[0:5]) #slicing

print(a[-1]) #negative indexing

print(a[-2]) #negative indexing

print(a[-5:]) #negative slicing

#a[0]="H" # strings are immutable, this will raise an error
# print(a)

print(a)

print(a.upper()) # converting to uppercase
print(a.lower()) # converting to lowercase
print(a.title()) # converting to title case
print(a.replace("world", "Python")) # replacing substring
print(a.split()) # splitting the string into a list
print(a.find("world")) # finding substring index
print(a.count("l")) # counting occurrences of a character

li=[1, 2, 3, 4, 5] # list
print(li[0])
print(li[-1])
print(li[1:4]) # slicing
print(li[-3:]) # negative slicing
li[0]=10
print(li) # modified list
li.append(6) # adding an element
print(li)
li.extend([7, 8]) # extending the list
print(li)

li.remove(3) # removing an element
print(li)

li.pop(0) # popping the last element
print(li)

li.sort() # sorting the list
print(li)
li.reverse() # reversing the list
print(li)   
li.clear() # clearing the list
print(li)
li=[1,2,3,45,5] # reinitializing the list
print(len(li))
print(max(li)) # maximum value
print(min(li)) # minimum value
print(sum(li)) # sum of elements
print(sorted(li)) # sorted list




