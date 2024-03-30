# เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
# โดยห้ามใช้ math.factorial เช่น 7! = 5040 
# มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว



# ขขขขขขขขขขขขขขขข

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

user_input = input("กรุณากรอกตัวอักษร: ")

if '!' in user_input:
    num_string = user_input.replace('!', '')
    try:
        number = int(num_string)
        print("ตัวเลขที่ได้: ", number)
        
        # คำนวณค่า factorial
        result = factorial(number)
        number_str = str(result)
        
        print(user_input," = ",number_str)
        # นับจำนวน '0' ที่ต่อท้าย
        ans = 0
        for char in number_str[::-1]:
            if char == '0':
                ans += 1
            else:
                break
        
        print("จำนวน '0' ที่ต่อท้าย:", ans)
        
    except ValueError:
        print("กรุณากรอกข้อมูลที่ถูกต้อง")
else:
    print("กรุณากรอกข้อมูลที่ถูกต้อง")
