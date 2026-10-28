"""
    该案例演示了一个整数的阶乘
"""

# 使用递归求阶乘

def get_factorial(n):
    # 递归的收敛条件
    if n == 1:
        return 1
    return n*get_factorial(n-1)

print(get_factorial(5))

