print("my name is Nihala")
print("I am a software engineer")
a=lambda x:x+1
print(a(5))

a=lambda x: x**2
print(a(10))

def age_group(age):
    if age>25:
        return "Adult"
    else:
        return "Young"
    
print(age_group(30))

b=lambda age:"Young" if age<25 else "Adult"
print(b(22))

a=[]
for i in range(5):
    a.append(i**2)
print(a)

print([i**2 for i in range(5)])

a=[]
for i in range(11):
    if i%2==0:
        a.append('even')
    else:
        a.append('odd')
print(a)

print(['even' for i in range(11) if i%2==0])
print(['even' if i%2==0 else 'odd' for i in range(11)])

[(1,5),(2,7),(3,2)]

print(list(zip([1,2,3],[5,7,2])))

print([i for i in zip([1,2,3],[5,7,2])])

a=[]
for i in zip([1,2,3],[5,7,2]):
    a.append(i)


print([(i,z) for i in [1,2,3] for z in [5,7,2]])

a=[]
for i in [1,2,3]:
    for j in [5,7,2]:
        a.append((i,j))
print({'even' for i in range(11) if i%2==0})

print({i:i**2 for i in range(1,20)})







