t_str = input()
dic = {}

for c in t_str :
   if c in dic :
      dic[c] += 1
   else :
      dic[c] = 1
 
for item in dic.items():
   print(item[0]," : ", item[1],"번")
