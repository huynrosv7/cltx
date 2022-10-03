from random import randint

print("|===================GAME=CHẲNG=LẺ=TÀI=XỈU====================|")
print("|                                                          |")
print("|                        tool by huy                       |")
print("|                                                          |")
print("|                        do not reup                       |")
print("|                                                          |")
print("|                      chẳng lẻ tài xỉu                    |")
print("|                                                          |")
print("|    zalo: 0986646427                      edit: huy hoàng |")
print("|                                                          |")
print("|                            CLTX                          |")
print("|                                                          |")
print("| NHỚ NGHI NGUỒN                                           |")
print("|==========================================================|")
while True:
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
			print("-----")
	if player == "chẳng":
		if computer =="chẳng":
			print("thắng")
			print("-----")
	if player == "lẻ":
		if computer == "chẳng":
			print("thua")
			print("-----")
	if player == "chẳng":
		if computer == "lẻ":
			print("thua")
			print("-----")
	if player =="":
		print("LỖI, VUI LÒNG NHẬP LẺ HOẶC CHẲNG")
	if player=="off"or player=="bye":
		print("CÚT")
		break