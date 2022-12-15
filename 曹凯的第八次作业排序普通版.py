#===========载入库===========
import math

#=========数据驱动========

m=0
ls=[12,0,8,9,6,7,21,46]

#=====主程序----=======

for j in range( len(ls)-1 ):
    for i in range(len(ls)-1-j):
        if(ls[j]>ls[i+1+j]):
            ls[j],ls[i+1+j]=ls[i+1+j],ls[j]
            m+=1
print(ls,m)
