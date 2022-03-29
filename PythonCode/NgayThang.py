import calendar
print("Mời bạn nhập năm: ")
x=int(input())
print("Mời bạn nhập tháng: ")
y=int(input())
       
       
print ("Tháng hiện tại:");
lich = calendar.month(x, y)
print (lich)

print ("Lịch hiện tại:");
z= calendar.prmonth(x,y)
print (z)