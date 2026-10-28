# 演示函数嵌套

def fun_a():
    print(f"fun_a开始执行")
    fun_b()
    print(f"fun_a执行结束")
def fun_b():
    print(f"fun_b开始执行")
    print(f"fun_b执行结束")

fun_a()