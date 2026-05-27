# 基础运算函数（原代码保留）
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# ===================== 以下是新增的输入验证功能（修改部分） =====================
# 功能：获取用户输入，并确保输入是数字，不是数字就一直提示重新输入
def get_valid_number(prompt):
    while True:
        try:
            # 尝试把输入转为浮点数
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            # 如果输入不是数字，提示错误
            print("❌ 输入错误：请输入有效的数字（如 5、3.14），不要输入文字或符号！")

# 功能：安全除法，自动检查除数不能为 0
def safe_divide(a, b):
    while b == 0:
        print("❌ 错误：除数不能为 0，请重新输入除数！")
        b = get_valid_number("请输入新的除数：")
    return a / b
# ===================== 以上是新增的输入验证功能（修改部分） =====================


# 主程序
print("===== 简易计算器（带输入验证版）=====")

# 获取两个有效数字
num1 = get_valid_number("请输入第一个数字：")
num2 = get_valid_number("请输入第二个数字：")

# 计算并输出结果
print(f"\n加法结果：{num1} + {num2} = {add(num1, num2)}")
print(f"减法结果：{num1} - {num2} = {subtract(num1, num2)}")
print(f"乘法结果：{num1} × {num2} = {multiply(num1, num2)}")
print(f"除法结果：{num1} ÷ {num2} = {safe_divide(num1, num2)}")

print("\n✅ 计算完成！程序不会崩溃啦～")