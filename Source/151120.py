# #z = 2+3j  #Kieu so thuc, 2 la phan thuc 3 la phan ao
# z = complex(2,3)
# print(z.real)
# print(z.imag)

##Khai bao bien o day ko can khai bao kieu du lieu
#vd: 
# x = 5
# #Kiem tra kieu du lieu cua 5 la gi su dung TYPE()
# print(type(x)) #Console: <class 'int'>

##Xoa bien su dung DEL 
# x = 5
# del x
# print(type(x)) #name 'x' is not defined

##Kiem tra vung du lieu import sys
# import sys
# print(sys.int_info)

##Toan tu
# print(9/2) #=> 4.5
# print(9//2) #=> 4

##Nhap tu ban phim su dung input()
# print("Nhap x:")
# x = input()
# print(x)
# print(type(x)) ##Khai bao kieu nay se ra la kieu chuoi <class 'str'>
# print("Nhap x:")
# x = int(input())
# print(type(x)) ##Dung kieu so nguyen <Int>

##Dua ve kieu bool
# def strBool(s):
#     return s.lower() in ("true", "t", "1", "yes")

# print("Nhap bool")
# x = strBool(input())
# print(x)

##Kieu xuat du lieu
# print('*' * 15)
# print('{0} {1}'.format(7, 10**7))