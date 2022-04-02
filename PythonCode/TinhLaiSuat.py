# Viết chương trình giúp người dùng tính một khoản tiền gửi cố định, 
# theo lãi suất đã nhập, tổng gốc và lãi của khoản tiền gửi cố định trong một đến ba năm, 
# và sử dụng phương pháp lãi kép để tính
# Biết số tiền gửi ban đầu là 10000 và lãi suất 1.5 mỗi năm

#Công thức lãi kép Fn=P(1+i/m)^n*m
print("Nhập số tiền vốn ban đầu")
P = float(input())
print("Nhập lãi suất hằng năm")
i = float(input())
print("Nhập số năm")
n = float(input())
print("Tổng tiền: ")
print(P*(1+i/100)**n)