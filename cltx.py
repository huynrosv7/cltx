from random import randint

print("|======================CHẲNG=LẺ=TÀI=XỈU====================|")
print("|                                                          |")
print("|                        make by huy                       |")
print("|                                                          |")
print("|                        do not reup                       |")
print("|                                                          |")
print("|                    game chẳng lẻ tài xỉu                 |")
print("|                                                          |")
print("|    zalo: 0986646427                      edit: huy hoàng |")
print("|                                                          |")
print("|                            CLTX                          |")
print("|                                                          |")
print("|==========================================================|")
y=10000
print("tiền: ",y)
while True:
	def win():
		w=y+10000
		print("ăn rồi: ",w)
	def close():
		c=y-10000
		print("thua rồi chơi lại thôi: ",c)
	player = input("nhập chẳng hoặc lẻ: ")
	computer2 = int(randint(2,10000))

	if computer2 % 2 == 0:
		computer = "chẳng"
	else:
		computer = "lẻ"

	print("số may mắn: ",computer2)

	if player == "lẻ":
		if computer == "lẻ":
			print("thắng")
			print("---")
			print(win())
	if player == "chẳng":
		if computer =="chẳng":
			print("thắng")
			print("---")
			print(win())
	if player == "lẻ":
		if computer == "chẳng":
			print("thua")
			print("---")
			print(close())
	if player == "chẳng":
		if computer == "lẻ":
			print("thua")
			print("---")
			print(close())
	if y == 0:
		print("hết tiền, cút")
		break
