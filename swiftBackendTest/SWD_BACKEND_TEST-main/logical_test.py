
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

# List Data

def number_to_thai_text(number):
    thai_digits = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    if number == 0:
        return thai_digits[0]

    thai_text = ''
    digit_count = 0

    while number > 0:
        digit = number % 10
        number //= 10

        if digit > 0:
            if digit == 1 and digit_count == 1:
                thai_text = thai_units[digit_count] + thai_text 
            else:
                thai_text = thai_digits[digit] + thai_units[digit_count] + thai_text
        digit_count += 1

    return thai_text

# Test Function
number = int(input("กรุณาป้อนตัวเลขระหว่าง 1 ถึง 9999999: "))
if 0 < number < 10000000:
    print("ข้อความภาษาไทย:", number_to_thai_text(number))
else:
    print("กรุณาป้อนค่าตัวเลขระหว่าง 1 ถึง 9999999")