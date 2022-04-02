# Viết chương trình tính tổng số tiền dựa vào số lượng
# Biết Áo thun 300 quần 250 áo khoác 400

name1 = 'AoThun'
price1 = 300

name2 = 'Quan'
price2 = 250

name3 = 'AoKhoac'
price3 = 400

print ("SL Ao Thun")
n1 = int(input())
print("SL Quan")
n2 = int(input())
print("SL Ao Khoac")
n3 = int(input())

sumPrice = (n1 * price1) +(n2 * price2) +(n3 * price3)

myformat = "{:<14}{:<25}{:<5}{}"
print(myformat.format('S.no', 'Sản Phẩm', 'Số lượng', 'Giá'))
print(myformat.format('0', name1, n1, price1))
print(myformat.format('1', name2, n2, price2))
print(myformat.format('2', name3, n3, price3))
print(myformat.format('Tổng: ', '', '', sumPrice))

# Cách đơn giản hơn
# print ("SL Ao Thun")
# n1 = int(input())
# print("SL Quan")
# n2 = int(input())
# print("SL Ao Khoac")
# n3 = int(input())
# print((n1 * 300) +(n2 * 250) +(n3 * 400))
# print(sumPrice)
