a='2 / 2 x 2'
a=a.split(" ")
b=[a[0],a[1],a[2]]
t=int((len(a)-1)/2)-1
# print(t)




if b[1]=='x':
    c=str(int(b[0])*int(b[2]))
elif b[1]=='/':
    c=str(int(b[0])/int(b[2]))
    c=int(c)
del(a[0],a[0],a[0])
for i in range(t):
    b=[a[0],a[1]]
    if b[0]=='x':
        c=str(int(c)*int(b[1]))
    elif b[0]=='/':
        c=str(int(c)/int(b[1]))
    del(a[0], a[0])

print(c)
# 
# 
# U1=3
# U2=5
# U3=7
# U4=9
# 
# Un=1+2n
# len(a)=1+2n
# (len(a)-1)/2=n
# 
# 
# 
#


a='1 / 2 / 2 / 2'
a=a.split(" ")
c=a[0]
del(a[0])
for i in range(int((len(a)-1)/2)+1):
    b=[a[0],a[1]]
    if b[0]=='x':
        c=float(c)*int(b[1])
    elif b[0]=='/':
        c=float(c)/int(b[1])
    del(a[0], a[0])
print(c)

