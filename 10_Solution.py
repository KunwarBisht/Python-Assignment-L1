##Create a suitable object type to eliminate the duplicate elements

def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
       if number not in newlist:
           newlist.append(number)
    return newlist
    
newlist=remove_duplicates([1,2,3,4,5,5,5,6,3,2])
print( newlist)
