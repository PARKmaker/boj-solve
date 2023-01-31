import sys
input = sys.stdin.readline



while True:

  text = input().rstrip("\n")

  if not text:
    break

  a = [0] * 4

  for i in text:
    if i == " ":
      a[3] += 1
    
    elif "A" <= i <= "z":
      idx = ord(i)-ord("a")
      if idx < 0:
        a[1] += 1
      else:
        a[0] += 1

    else:
      a[2] += 1
  
  print("{} {} {} {}".format(a[0],a[1],a[2],a[3]))