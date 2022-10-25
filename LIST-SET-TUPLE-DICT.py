#!/usr/bin/env python
# coding: utf-8

# ### LIST

# List are coma seprated within [].
# 
# List are mutable(can be changed)
# 
# List can be indexed and slicing can also be done
# 
# List allows all type of datatypes
# 
# Llist allows duplicate elements in the input list

# In[1]:


l=[12,13.6, "sai", 1+2j, "priya",12]
print(l)
print(type(l))
print(len(l))


# In[2]:


#converting the set to LIST
s=(100,"abcd",13.5)
print(type(s))
l2=list(s)
print(l2)
print(type(l2))


# In[3]:


#Indexing or Slicing in list
print(l)
print(l[1:4])#it will show the first 4 elemnts in the list
print(l[:]) #it will show all elements in the list
print(l[2:])# it will show elements from 2nd element to last
print(l[:-1])#it will show all the elements from back except the last one
print(l[2])# to get the 2nd position element
print(l[::-1]) # to get all the elements in reverse order


# In[4]:


l=[12,13.6, "sai", 1+2j, "priya",12,200]
l


# In[5]:


l=[12,13.6, "sai", 1+2j, "priya",12,200]
l.insert(3,"sri")#select the location & give what to be inserted
l


# In[6]:


l=[12,13.6, "sai", 1+2j, "priya", 12, 200]
l.append("amma")
l


# In[7]:


l=[12,13.6, "sai", 1+2j, "priya", 12, 200]
l1=["june",123,13.6,"sai",500]
l.append(l1)
l


# #### both extend and +(addition) will be the same output

# In[8]:


l=[12,13.6, "sai", 1+2j, "priya",12,200]
l1=["june",123,13.6,"sai",500]
l.extend(l1)
l


# In[9]:


l=[12,13.6, "sai", 1+2j, "priya",12,200]
l1=["june",123,13.6,"sai",500]
print(l+l1)


# In[10]:


l3=[12,13.6, "sai", 1+2j, "priya",12.3,1200,"mmm"]
l3


# In[11]:


l3=[12,13.6, "sai", 1+2j, "priya",12.3,1200,"mmm"]
l3.remove("mmm")
l3


# In[12]:


l3=[12,13.6, "sai", 1+2j, "priya",12.3,1200,"mmm"]
l3.remove(12.3) #remove by the element & only one can be done
l3


# In[13]:


l3=[12,13.6, "sai", 1+2j, "priya",12.3,1200,"mmm"]
l3.pop(3) # remove the element by position & only one can be removed
l3


# In[14]:


l3=[12,13.6, "sai", 1+2j, "priya",12.3,1200,"mmm"]
l3.clear()
l3


# In[15]:


x=[64,10,12,15,88,76,200,150,88]
x1=set((x))  #list converted to set
x1


# In[16]:


x2=list((x1)) 
# sets are converted to list
# to remove the duplicates we can convert from one form to other
x2


# In[17]:


x=[64,10,12,15,88,76,200,150,88]
y=[12,88,15,150]
for n in y:
   while n in x:
       x.remove(n)
print(x)


# In[18]:


a=[x for x in range(20) if x<5]
a


# In[19]:


b=range(20)
b


# In[20]:


c=[x for x in range(20) if x<10]
c


# #### to get the ascending & descending order of numeric & string individually
# 
# the ist should not contain both number & string for the sorting
# 
# by default the sorting will be in ascending order.
# 
# to get in desending order we must give reverse=True

# In[21]:


# to get the ascending order of numerics
a1=[1,53,46,80.6,2.56,23.8]
a1.sort()
a1


# In[22]:


#to get the ascending order of string
a2=["air","volume","desity","mass","flow","capacity"]
a2.sort()
a2


# In[23]:


#to get the descending order of numeric
a1=[1,53,46,80.6,2.56,23.8]
a1.sort(reverse=True)
a1


# In[24]:


#to get the descending order of string
a2=["air","volume","desity","mass","flow","capacity"]
a2.sort(reverse=True)
a2


# In[25]:


# to get the reverse order of the given list
a2=["air","volume","desity","mass","flow","capacity"]
a2.reverse()
a2


# In[26]:


a1=[1,53,46,80.6,2.56,23.8]
a1.reverse()
a1


# In[27]:


a3=[12.5,80.6,"air","water","mass",56]
print(a3.index(80.6))
print(a3.index("mass"))


# In[28]:


#to get the number of elements in the list
len(a3)


# ### TUPLE
# 
# Tuple are coma seperated with ().
# 
# Tuples does not support item assignment i,e they are immutable.
# 
# Indexing can be done for the tuple.
# 
# Tuple supports multiple datasets.

# In[29]:


a=(1,2,3,"abc",5.6)
print(type(a))


# In[30]:


#we can convert list to tuple
l=[1,3,5,"abb",20.6,5]
print(type(l))
d=tuple(l)
print(type(d))
d


# In[31]:


d[1:] #indexing can be done


# In[32]:


d[::-1] # to get reverse order


# In[33]:


a[2]=50 # they are immutable so we cant change the elements


# In[34]:


a.append(100)


# ### SETS
# sets are one dimensional.
# 
# Sets allow mixed datatypes.
# 
# Sets are coma seperated and encosed by {}.
# 
# Sets is unordered, it will define its ow order.
# 
# Sets will have unique elements( they dont allow duplicates).
# 
# Sets does not support assignmnet
# 

# In[35]:


a={'mom',123,'dad',66.22,'son'}
type(a)


# In[36]:


b=['abc',22,30.6,100,'forest',True, 5.4]
print(type(b))
b1=set((b))
print(type(b1))


# In[37]:


#Sets does not support assignmnets
print(b[5])
print(b1[4])


# In[38]:


for i in b:
    print(i)


# In[39]:


#to check weather it is present in the given set.
print(100 in b1)


# In[40]:


print(b1)
b1.add("pune")
b1


# In[41]:


print(b1)
print(a)
b1.update(a)
b1


# ##### remove & dicard will remove the element given but discard will not show any error if the given element is not present

# In[42]:


b1.remove("pune")
b1


# In[43]:


b1.remove(123)


# In[44]:


b1


# In[45]:


b1.discard("forest")
b1


# In[47]:


b1.discard("apple") #since the apple element is not present in the given set it wil not show any error
b1


# In[48]:


b1.remove("apple") #it wil show an error if it is not in the given set
b1


# In[50]:


b1.pop()
b1


# In[51]:


b3=['abc',22,30.6,100,'forest',True, 5.4]
b3.pop() #remove the last element
b3


# In[52]:


b3=['abc',22,30.6,100,'forest',True, 5.4]
b3.clear() #it will remove content in the given 
b3


# In[53]:


b3=['abc',22,30.6,100,'forest',True, 5.4]
del b3 #it willl remove the b3 itself so it shows the error
b3


# ##### We can do Union & Intersection with the Sets

# In[54]:


#to perform the UNION operation
s1={'a','b','c','d'}
s2={1,2,4,5,6}
s=s1.union(s2)
s


# In[55]:


#To perform the INTERSECTION operation
x1={'a','b','c','d',1,5}
x2={1,2,4,5,6}
x=x1.intersection(x2)
x


# In[56]:


type(x1)


# In[57]:


a = set('abracadabra')
b = set('alacazam')


# In[58]:


a # we get the unique eements


# In[59]:


b


# In[60]:


print(a-b) #get letters in a but not in b
print(a&b) #to get letters in both a and b
print(a|b) #get letters in a or b or both
print(a^b) # letters in a or b but not both


# In[ ]:





# ### DICTIONARY
# These are enclosed with in {}.
# 
# These come with a KEY:VALUE as a pair.
# 
# We can search the value by its key.
# 
# key must be always unique(no duplicates) and cant be changed.
# 
# Indexing is not possible.
# 
# It allows the mixed datatypes.
# 
# Follows the order which we have given.
# 

# In[61]:


d={"name":"sai","age":27,"gender":"Female","place":"India"}
d


# In[62]:


print(d)
print(len(d))
print(d["place"])
print(d.keys()) #to get the key 
print(d.values())# to get the values


# In[63]:


d["age"]=19 # we can update the values using the keys
d


# ##### We can add and modify using the UPDATE 

# In[64]:


d.update({"gender":"F"}) # we can modify the existing values
d


# In[65]:


d.update({"year":1994}) # we can add a new key:value pair
d


# In[66]:


d.popitem() # to remove the last item
d


# In[67]:


d.pop("gender")# rwmove the sepcific key mentioned
d


# In[68]:


del d["name"] #To remove 
d


# In[69]:


d1={"name":"sai","age":27,"gender":"Female","place":"India"}
del d1 #To remove 
d1


# In[70]:


d1={"name":"sai","age":27,"gender":"Female","place":"India"}
d1.clear() #To remove 
d1


# In[71]:


x={"name":"sai","age":27,"gender":"Female","place":"India","year":1994,"height":156}


# In[72]:


if "year" in x:
    print("yes")
else:
    print("no")


# In[73]:


#by default only the keys will be displayed
for i in d:
    print(i)


# In[74]:


for i,j in d.items():
    print(i,j)


# In[75]:


x={"name":"sai","age":27,"gender":"Female","place":"India","year":1994,"height":156}


# In[76]:


sorted(x)


# In[77]:


list(x)


# In[78]:


dict(age=25, place='delhi', name='aaa')


# In[79]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[80]:


{x: x**2 for x in (2, 4, 6,8)}


# In[81]:


{x: x**2 for x in range(0,20,2)}


# In[82]:


dd={'info1':{'name':"aaaa",'age':13,'city':"delhi"},
   'info2':{'name':"bbb",'age':15,'city':"gujarth"},
   'info3':{'name':"ccc",'age':27,'city':"chennai"}}
dd


# In[83]:


dd['info1']['name']

