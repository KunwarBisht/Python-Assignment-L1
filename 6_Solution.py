'''
6.	Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
         a) Create Maxlist by taking 2 maximum elements from each list.
         b) Find average value from all the elements of Maxlist.
         c) Create a MinlIst by taking 2 minimum elements from each list 
         d) Find the average value from all the elements of Minlist

'''

import heapq

list1=[1,2,44,67,88,92,100]

list2=[10,20,41,6,8,9,10]

list3=[11,12,40,60,33,9,1]


lists=[list1,list2,list3]

maxlist=[]

minlist=[]



def max_num (listmax):

  val=heapq.nlargest(2, listmax)

  for v in val:

    maxlist.append(v)




def min_num (listmin):

  val=heapq.nsmallest(2, listmin)

  for v in val:

    minlist.append(v)

  


def average_val(avg):

  return sum(avg)/len(avg)




for  maxL in lists:

  max_num(maxL)




for  minL in lists:

  min_num(minL)




print("Maxlist :",maxlist)

print("MinlIst :",minlist)
print("avegage of max :{0}".format(average_val(maxlist)))

print("avegage of Min :{0}".format(average_val(minlist)))
  
