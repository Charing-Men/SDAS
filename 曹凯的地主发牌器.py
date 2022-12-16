from turtle import*
import random as r
import math

p=[]
hs=["♥","♦","♠","♣"]
q=[]
wang=['小王','大王']
n1=[]
n2=[]
dz=[]

for i in range(4):              #循环四次，取红心，方块，黑桃，梅花
    for a in range(13):         #循环十七次，a取值从0到13
        if (a==0):
            b="A"
        elif (a==10):
            b="J"
        elif (a==11):
            b="Q"
        elif (a==12):
            b="K"
        else:
            b=str(a+1)
        q.append(b)

for i in range(4):       #花色数字分开，方便最后画图
     for a in range(13):
        c=[hs[i],q[a]]
        p.append(c)
p.append(wang[0])
p.append(wang[1])


for i in range(54):
    if (p[i][1]=='10'):
        p[i][1]='E'

for i in range(54):
    if (p[i][1]=='A'):
        p[i][1]='X'

for i in range(54):
    if (p[i][1]=='K'):
        p[i][1]='R'

for i in range(54):
    if (p[i][1]=='2'):
        p[i][1]='Z'


for o in range(51):
    if (o%3==1):#用余数法轮流发牌，要明白为什么除3
        a=r.randint(0,53-o)#包括首尾
        n1.append(p[a])
        del p[a]
    if (o%3==2):
        a=r.randint(0,53-o)
        n2.append(p[a])
        del p[a]
    if (o%3==0):
        a=r.randint(0,53-o)
        dz.append(p[a])
        del p[a]

def move(x,y):
    seth(90)
    pu()
    goto(x,y)
    pd()

def pm(x,y):#编辑牌框程序
    move(x,y)
    color('black','green')
    begin_fill()
    fd(35)
    circle(-5,90)
    fd(50)
    circle(-5,90)
    fd(90)
    circle(-5,90)
    fd(50)
    circle(-5,90)
    fd(60)
    end_fill()

dz.append(p[0])
dz.append(p[1])
dz.append(p[2])

#如果想从小到大排列自然而然要做个元素排序
#记得问老师为什么这里10<1，2，3，4，5，6，7，8，9
#还有如何定义使JQKA不按字母表排序
#所以这是一个失败品,，做的出来但是太复杂了

        
    




for a in range(100):
    for i in range(len(n1)-1):
        if (n1[i][1]>n1[i+1][1]):
            n1[i],n1[i+1]=n1[i+1],n1[i]
            

for a in range(100):
    for i in range(len(n2)-1):
        if (n2[i][1]>n2[i+1][1]):
            n2[i],n2[i+1]=n2[i+1],n2[i]

for a in range(100):
    for i in range(len(dz)-1):
        if (dz[i][1]>dz[i+1][1]):
            dz[i],dz[i+1]=dz[i+1],dz[i]
        
for i in range(17):#这里用了一个元素代换可能把事情做复杂了，应该能打包但是我懒得试了，目的是正确排序
    if (n1[i][1]=='E'):
        n1[i][1]='10'

for i in range(17):
    if (n1[i][1]=='X'):
        n1[i][1]='A'

for i in range(17):
    if (n1[i][1]=='R'):
        n1[i][1]='K'

for i in range(17):
    if (n1[i][1]=='Z'):
        n1[i][1]='2'



for i in range(17):
    if (n2[i][1]=='E'):
        n2[i][1]='10'

for i in range(17):
    if (n2[i][1]=='X'):
        n2[i][1]='A'

for i in range(17):
    if (n2[i][1]=='R'):
        n2[i][1]='K'

for i in range(17):
    if (n2[i][1]=='Z'):
        n2[i][1]='2'


for i in range(20):
    if (dz[i][1]=='E'):
        dz[i][1]='10'

for i in range(20):
    if (dz[i][1]=='X'):
        dz[i][1]='A'

for i in range(20):
    if (dz[i][1]=='R'):
        dz[i][1]='K'

for i in range(20):
    if (dz[i][1]=='Z'):
        dz[i][1]='2'
print(n1)
print(n2)
print(dz)
screensize(900,600,'green')
speed(0)#三个循环来连牌带框画出#给数据二维了但是使主程序会更加复杂，其实可以编一个打包模板，那样就不需要调试了
for i in range(len(n1)):#其实可以二维双循环完成，不过构思成本会过高
    pm(-610+i*40,-200)
    move(-610+i*40,-180)
    write(n1[i][0],font=30)
    move(-595+i*40,-180)#三个顺序其实就是画牌框然后把元素一个一个的放上去，只不过不知道如何放大图像
    write(n1[i][1],font=30)
    move(-575+i*40,-260)
    write(n1[i][0],font=30)
    move(-560+i*40,-260)
    write(n1[i][1],font=30)
    move(-585+i*40,-220)
    write(n1[i][0],font=30)
    
    
for i in range(len(n2)):
    pm(-610+i*40,-80)
    move(-610+i*40,-60)
    write(n2[i][0],font=30)
    move(-595+i*40,-60)
    write(n2[i][1],font=30)
    move(-580+i*40,-140)
    write(n2[i][0],font=30)
    move(-565+i*40,-140)
    write(n2[i][1],font=30)
    move(-585+i*40,-100)
    write(n2[i][0],font=30)
    
for i in range(len(dz)):
    pm(-760+i*40,100)
    move(-760+i*40,120)
    write(dz[i][0],font=30)
    move(-745+i*40,120)
    write(dz[i][1],font=30)
    move(-725+i*40,40)
    write(dz[i][0],font=30)
    move(-710+i*40,40)
    write(dz[i][1],font=30)
    move(-735+i*40,80)
    write(dz[i][0],font=30)

