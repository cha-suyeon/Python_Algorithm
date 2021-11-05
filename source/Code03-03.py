katok = ['다현', '정연', '쯔위', '사나', '지효']


def delete_data(position) :
        
	if position < 0 or position > len(katok) :
		print("데이터를 삭제할 범위를 벗어났습니다.")
		return

	kLen = len(katok)
	katok[position] = None	# 데이터 삭제
    
	for i in range(position+1, kLen) :
		katok[i-1] = katok[i]
		katok[i] = None	# 배열의 맨 마지막 위치 삭제

	del(katok[kLen-1])


delete_data(1)
print(katok)
delete_data(3)
print(katok)
