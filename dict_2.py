a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

c = {}

for key, value in a.items():
   if key in b:
      if value < b[key]:
         c[key] = value
      else:
         c[key] = b[key]
   else:
      c[key] = value
      
for key, value in b.items():
   if not key in c:
      c[key] = value

print(c)

for key, value in c.items():
   if value >= 3000:
      print(key, ":" , value)
