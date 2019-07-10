#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverseFib(n):
    a = [0] * n 
    a[0] = 0 
    a[1] = 1 
    for i in range(2, n):  
        a[i] = a[i - 2] + a[i - 1] 
    for i in range(n - 1, -1 , -1):  
        print(a[i],end=" ") 
        
n = 5 
reverseFib(n)


# In[2]:


#10
def seriesGen2(n):
   i=1
   while i<=n:
       print(i,end="  ")
       i=i*2
   return
seriesGen2(100)


# In[3]:


# term of geometric progression  
import math  
 
def Nth_of_GP(a, r, N):  
   return( a * (int)(math.pow(r, N - 1)) )  
a = 2
r = 3 
N = 5   
print("The", N, "th term of the series is :",  
                           Nth_of_GP(a, r, N))


# In[4]:


# Series Generation

def seriesgeneration(n):
   i=1
   while i<=n:
       print(i,end=" ")
       i=i*3
   return
seriesgeneration(100)
  


# In[5]:


#8. Your Program has to read one string as well as one character and you need to remove the all the occurance of the character.

#HebeonTech,e -- HbonTch
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[6]:





# In[7]:


# 9. Your Program need to accept two strings and generate the output in merging of both strings.
def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[9]:


# 12. Series Generations:-  1 3 4 8 15 27 50 92 169 311
def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[10]:


# 14. Series Generations:-  1! + 2! + 3! + 4! + 5! + ... + n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[1]:


def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                     c+=1
        if c==0:
            s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[5]:


def Q3(a,b):
   if len(a)<=len(b):
       n=len(a)
       k=len(b)
   else:
       n=len(b)
       k=len(a)
   for i in range(n):
       print(a[i],b[i])
   for j in range(n,k):
       if(len(a)<=len(b)):
           print(b[j],'*')
       else:
           print(a[j],'*')
   return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[6]:


def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else: 
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[8]:


def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[9]:


def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




