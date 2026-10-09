import numpy as np


print('\nPHẦN A')

print('\nCâu A1:')
a1 = np.arange(1, 21)
print(a1)
b1 = np.zeros((5, 5))
print(b1)
c1 = np.eye(4)
print(c1)
d1 = np.linspace(0, 1, 5)
print(d1)


print('\nCâu A2:')
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

print('\nCâu A3:')
a_arr = arr.reshape(4, 3)
print(a_arr)

b_arr = arr.reshape(2, -1)  #-1 để Python tự suy luận sao cho tổng số phần tử không đổi
print(b_arr)

c_arr = arr.T
print(c_arr, c_arr.shape)

print('\nCâu A4:')
fl_arr = arr.flatten()
print(fl_arr, fl_arr.shape)

print('\nPHẦN B')
a = np.arange(1, 26).reshape(5, 5)
print(a)

print('\nB1: ',a[1,2])
print('\nB2: ',a[-1,:])
print('\nB3: ',a[:,0])
print('\nB4: ',a[1:4,1:4])
print('\nB5: ',a[::2,:])
print('\nB6: ',a[a%3==0])

print('\nB7:')
rows, cols = np.where(a > 20)
print("Chỉ số hàng:", rows)
print("Chỉ số cột:", cols)

print('\nB8:', a[:2, -2:])

print('\nB9:')
b = a.copy()
b[b % 2 == 0] = 0
print("Mảng b:", b)

print('\nB10:')
p = a[:2]
q = a[3:]

print("Shape khi ghép dọc:", np.vstack((p, q)).shape)
print("Shape khi ghép ngang:", np.hstack((p, q)).shape)

print('\nPHẦN C')

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(x)
print(y)

print('\nCâu C1: ')
print("x + y:", x + y)
print("x * y:", x * y)
print("y / x:", y / x)
print("x ** 2:", x ** 2)

print('\nCâu C2: ')
z = np.array([-3, 2, -1])
print(z)
print("Tích vô hướng:", np.dot(x, y))
print("Căn bậc hai:", np.round(np.sqrt(x), 2))
print("Giá trị tuyệt đối:", np.abs(z))

print('\nCâu C3: ')

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A)
print(B)
print("A * B:", A*B)

print("A @ B:", A@B)

print('\nCâu C3')

M = np.arange(12).reshape(3, 4)
v = np.array([100, 200, 300, 400])
w = np.array([1, 2, 3])

print("M:")
print(M)

print('\na',M + 5)
print("Shape của M:", M.shape)
print("Shape của v:", v.shape)
print('\nb',M + v)
#lỗi: print('\nc',M + w)

print('\nPHẦN D')
scores = np.array([
    [8.0, 7.5, 9.0, 6.5],
    [5.5, 6.0, 7.0, 4.5],
    [9.0, 9.5, 8.5, 9.0],
    [7.0, 6.5, 8.0, 7.5],
    [4.0, 5.0, 3.5, 6.0],
    [8.5, 8.0, 7.5, 9.5],
])
mon = ["Toán", "Lý", "Hóa", "Tin"]
print('\nD1: ',scores, scores.shape)
print(mon)

tb_sv = scores.mean(axis=1) #tb từng hàng
print('\nD2: ',tb_sv)

tb_mon = scores.mean(axis=0) #tb từng cột
print('\nD3: ',tb_mon)

index_sv = np.argmax(tb_sv)
print('\nD4: ',index_sv, tb_sv[index_sv])

index_mon = np.argmin(tb_mon)
print('\nD5: ',index_mon, tb_mon[index_mon])

index_max = np.argmax(scores, axis=0)
print('\nD6: ',index_max)

tb_tu_7 = tb_sv[tb_sv >= 7.0]
print('\nD7: ',tb_tu_7, tb_tu_7.size)

phan_loai = np.where(tb_sv >= 8.0, 1, 0)
print('\nD8: ',phan_loai)

hang, cot = np.where(scores < 5)
print('\nD9:', hang, cot)


print('\nPHẦN E')
np.random.seed(42)
dt = np.random.randint(50, 201, 36).reshape(12, 3)
print(dt)

print("\nE1:")
tong_chi_nhanh = np.sum(dt, axis=0)

for i in range(3):
    print(f"Chi nhánh {i + 1}: {tong_chi_nhanh[i]} triệu đồng")

print("\nE2:")
tong_thang = np.sum(dt, axis=1)

for i in range(12):
    print(f"Tháng {i + 1}: {tong_thang[i]} triệu đồng")

thang_cao_nhat = np.argmax(tong_thang)
print(f"Tháng cao nhất: tháng {thang_cao_nhat + 1}")
print(f"Tổng doanh thu: {tong_thang[thang_cao_nhat]} triệu đồng")

print("\nE3:")
cn1 = dt[:,0]
tb_cn1 = np.mean(dt)
months_e3 = np.where(cn1 > tb_cn1)[0]+1
print(f'Doanh thu trung bình cn1: {tb_cn1:.2f} triệu đồng')
print(f'Các tháng doanh thu cao hơn trung bình: {months_e3}')

print("\nE4:")
dt_months_e4 = np.sum(dt, axis=1)
thang_sau_e4 = dt_months_e4[1:12] #Tháng 2 -> 12
thang_truoc_e4 = dt_months_e4[:-1]
tang_truong_e4= (thang_sau_e4 - thang_truoc_e4) / thang_truoc_e4 * 100
for i in range(len(tang_truong_e4)):
    print(f'Tháng {i+2} tăng trưởng so với tháng {i+1}: {tang_truong_e4[i]:.2f}%')

print("\nE5:")
congdon_cn2=np.cumsum(dt[:,1])
for i in range(len(congdon_cn2)):
    print(f'Doanh thu tính đến tháng {i+1}: {congdon_cn2[i]} triệu đồng')

print('\nE6:')
dt_chuan_hoa = (dt - dt.min()) / (dt.max() - dt.min())
print(dt_chuan_hoa)
print("Bảng doanh thu sau chuẩn hóa:")
print(np.round(dt_chuan_hoa, 2))
print("Giá trị nhỏ nhất:", dt_chuan_hoa.min())
print("Giá trị lớn nhất:", dt_chuan_hoa.max())

print("\nE7:")
doanh_thu_max = dt.max()
thang, chi_nhanh = np.where(dt == doanh_thu_max)
print(f"Doanh thu cao nhất: {doanh_thu_max} triệu đồng")

for i in range(len(thang)):
    print(f"Tháng {thang[i] + 1}, chi nhánh {chi_nhanh[i] + 1}")