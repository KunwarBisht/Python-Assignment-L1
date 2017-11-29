'''
5 - 5.	Write a code to read  the data from
input file called input.txt and count the number
of characters per line, number of words per line and write these into output file called as output.txt

'''

file_name='input.txt'

def write_output(file_name):
  
  f=open(file_name,'r')
  file_out=open('output.txt','w')
  for Line_No,line in enumerate(f):
    Total_words=line.split()
    TotalChar_perLine=0
    for word in Total_words:
      TotalChar_perLine +=len(word)
    file_out.write("Total Number of Character at Line {0} is {1}\n".format(Line_No,TotalChar_perLine))
  file_out.close()
  f.close()

write_output(file_name)

