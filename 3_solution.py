'''Question 
Write a program to receive a string from keybord and check if the string has two 'e' in the characters. 
   If yes return True else False.
'''

def check_char(char):
  count=0
  if len(char) < 2:
    print("False")
    return
  else:
    for i in string:
      if i =='e':
        count +=1
    if count==2:
      print("True")
    else:
      print("False")
  
string=input("Enter the String : ")
check_char(string)
