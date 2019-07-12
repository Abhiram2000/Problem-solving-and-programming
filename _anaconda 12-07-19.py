#!/usr/bin/env python
# coding: utf-8

# ## Regular Expression
# - Pattern Matching
# - Patterns(re) package
# - [0-9]--> Any digit matching
# - Two digit number (^[0-9]{2}$)-Five Digit number(^[0-9]{5}$)
# 

# 
#  Regular Expression for characters
# - a-z]--> Any lower case characters
# - [A-Z]--> Any upper case characters
# - ^[a-z]{5}−−>𝐼𝑡𝑎𝑎𝑐𝑒𝑝𝑡5𝑙𝑜𝑤𝑒𝑟𝑐𝑎𝑠𝑒𝑐ℎ𝑎𝑟𝑎𝑐𝑡𝑒𝑟𝑠−[𝑎−𝑧𝐴−𝑍]8−−>Itaacept5lowercasecharacters  ----------------- [a−zA−Z]8--> Accept 8 characters can be anything lower and upper
# - ^[a-zA-Z0-9]{8}$--> Accept 8 characters can be anything lower,upper and digit

# In[ ]:


import re
def twoDigitMatching(n):
    pattern = '[0-9]{2}$'
    n = str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12))
print(twoDigitMatching(123))


# In[ ]:


#Function to define to test username having 8 characters
#Upper case and lower
import re
def testUsername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# ### Regular Expression to match the India Mobile Number
# - 10 Digits
# - (First digit will be [6-9]) and remaining 9 digits will be [0-9]
# - Example:- 9535152553
# - Re- ^[6-9][0-9]{9}$
# - Example:- 09988774455   
# 

# In[ ]:


def phonenumberValidation(phone):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phonenumberValidation('+919988774455')


# 
# -- Regular Expression to Validate the RollNumber
#  - Example : 1521A0501
#  - Example : 1521A0109
#  - Example : 1521A0499
# - Regular Expression to validate the password
#  - Parameters : Len min of 6 characters and Max of 15 characters
#  - Accept lower case, upper case, Digits spl char(@,#,!)

# In[ ]:


def rollnumbervalidation(rollnumber):
    pattern = '^[1][5][2][1][A][0-9]{4}$'
    rollnumber = str(rollnumber)
    if re.match(pattern,rollnumber):
        return True
    return False
rollnumbervalidation('1521A0501')


# In[ ]:


def password(s):
    pattern = '^[!-~]{6,15}$'
    if re.match(pattern,s):
        return True
    return False
print(password("Ap@18151925"))


# ### Email ID validation using Regular Expression
# - Example : Username@DomainName.extension
# - Username :-
#             - Length will be [6-15]
#             - No Spls characters apart from Underscore(_)
#             - Should not begin and ends with Underscore(_)
#             - Characters Set : All digits and lower case
# - DomainName :- 
#              - Length will be [3-18]
#              - No spls characters
#              - Character Set : All digits and lower case
# - Extension :-
#              - Length will be [2-4]
#              - No spl characters
#              - Character Set : Lower case characters
# 

# In[ ]:


def emailIdValidation(email):
    pattern = '^[0-9a-z_.][0-9a-z_.]{6,15}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailIdValidation('avulaabhiram2586@gmail.com')


# In[ ]:


#Line draw in reverse direction
import turtle as tt
a1 = tt.Turtle
tt.backward(100)
tt.done()


# In[ ]:





# In[ ]:


# Step 1 : Make all the turtle package to be imported
import turtle
# Turtle method creates and returns a new object
a1= turtle.Turtle()
# forward() method moves 100 pixels
turtle.forward(250)
#we are done
turtle.done()


# In[ ]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done


# In[1]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
tt.done()


# In[1]:


# Draw pentagon
import turtle as tt
a1 = tt.Turtle()
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
tt.done()


# In[1]:


# Star
import turtle as t
a1 = t.Turtle()
for i in range(40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[1]:


# Spiraling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:




