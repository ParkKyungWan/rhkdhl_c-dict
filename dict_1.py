dic = { "홍길동": "010-1111-1111",
        "이순신": "010-1111-2222",
        "강감찬": "010-1111-3333"}

print("아래 학생들의 전화번호를 조회할 수 있습니다.\n")
for key in dic.keys():
   print(" - ",key)
   
print("\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")

name = input()
if name in dic:
   print(name, "의 전화번호는",dic[name],"입니다.")
else :
   print("목록에 없는 이름입니다.")
