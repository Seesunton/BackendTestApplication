# เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4]
# ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข


arr = [12, 32, 1, 3, 99, 11, 84]

max_value = arr[0]  # เริ่มต้นโดยตั้งค่าค่ามากที่สุดเป็นค่าแรกใน Array
max_index = 0  # เริ่มต้นโดยตั้งค่า index ของค่ามากที่สุดเป็น 0

for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i

print("ตำแหน่ง index ของตัวเลขที่มีค่ามากที่สุดคือ : ", max_index)
