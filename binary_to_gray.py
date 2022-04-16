def flip_num(num):
    if(num == '0'):
        return '1'
    else:
        return '0'

binary = "10001"
gray = ""
gray += binary[0]
for i in range(1,len(binary)):
    if(binary[i] == '0'):
         gray += binary[i-1]
    else:
        gray += flip_num(binary[i-1])

print("gray : ",gray)
