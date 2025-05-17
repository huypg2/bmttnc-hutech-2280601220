#Nhap cac dong tu ngưoi dung
print("Nhap cac dong van ban (nhap 'done' đe ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
#Chuyen cac dong thanh chu in hoa và in ra man hinh
print("\nCac dong da nhap sau khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())
