import sys
S = sys.stdin.readline().strip()

sign = []
isSign = False
blank = []
a = []
arr = []

for i in range(len(S)):
  
  if isSign:
    a.append(S[i])

  if S[i] == "<":
    # sign.append(i)
    if a:
      arr.append("".join(a))
      a=[]
      sign.append("blank")

    a.append(S[i])
    isSign = True

  elif S[i] == ">":
    # sign.append(i) 
    isSign = False
    arr.append("".join(a))
    a = []
    sign.append("sign")

  elif S[i] == " " and not isSign:
    # blank.append(i)
    arr.append("".join(a))
    arr.append(" ")

    sign.append("blank")
    sign.append("blank")
    
    a=[]
  
  elif not isSign:
    a.append(S[i])

if a:
  arr.append("".join(a))
  a=[]
  sign.append("blank")

for idx in range(len(sign)):
  if sign[idx] == "blank":
    # print(idx)
    arr[idx] = arr[idx][::-1]

# print(sign)
print("".join(arr))