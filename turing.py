def listSkills(val, list=[]):
    list.append(val)
    return list
list1=listSkills('NodeJS')
list2=listSkills('Java',[])
list3=listSkills('ReactJS')
print("%s"%list1)
print("%s"%list2)
print("%s"%list3)
print("Welcome to TURING".capitalize())
class h:
    def __init__(s,a='Welcome to '):
        s.a=a
    
    def w(s,x):
        print(s.a+x)
hi=h()
hi.w('Turing')

d={}
d={1:2,3:4}
print(d[1],d[3])

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)

l1=[1,2,6,12]
l2=[12,6,2,1]
print(l1==l2)
print(set(l1)==set(l2))

l=[1,2,3,4,5]
m=map(lambda x: 2**x,l)
print(list(m))

class W:
    def __init__(s,n):
        s.n=n
    def h(s):
        print("wt",s.n)

c=W('T')
c.h()

data = [10,20,30,40,50]
data.pop()
print(data)
data.pop(2)
print(data)

z=set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)
'''
'''
a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)
try:
    pass
except:
    pass
finally:
    pass
#a=['w','t','T']
#print('-'.join(a))
#'T{}s{1}{2}'.format('b','o','l')
l=[1,2,3,4]
p=[5,6,7]
result=l+p

result.insert(3,'J')

#result.add(3,'J')

#result.insert(2,'J')

#result.append(3,'J')
print(result)
x='abcdef'
i='a'
print(i)

i=['n','r','v']
print(i)
#for x in i:
#    i.append(x.upper())
#print(i)

#print([i.lower() for i in "TURING"])
