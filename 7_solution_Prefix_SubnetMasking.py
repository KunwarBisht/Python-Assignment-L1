'''
7.	Write program to convert prefix/net mask to IP
eg: input:16  output: 255.255.0.0
'''

prefix=int(input("Enter the prefix"))#16)

def Get_SubnetMask(prefix):
  lsIP = []
  ans = 0
  CIDR =prefix
  IP = [1] * CIDR
  for i in range(len(IP)):
      iIdx = i % 8
      if iIdx == 0:
          if i >= 8:
              lsIP.append(ans)
              ans = 0
      ans += pow(2, 7 - iIdx)
  lsIP.append(ans)
  [lsIP.append(0) for i in range(4 - len(lsIP))]
  print("SubNetMask for the prefix {0} is".format(prefix),'.'.join(str(x) for x in lsIP))


Get_SubnetMask(prefix)
