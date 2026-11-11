"""
    该案例演示了send向生成器函数发送值
"""
def gen():
    task_id = 0
    int_value = 0
    char_value = "A"
    while True:
        match task_id:
            case 0:
                # send函数发送的数据，会作为yield表达式的返回值 赋值给task_id
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                char_value = chr(ord(char_value) + 1)
            case _:
                task_id = yield

g = gen()
# 注意：如果通过send启动生成器，第一次传递的值必须是None，因为这个时候还没有yield表达式能接收你传递的值
print(g.send(None))
print(g.send(0))
print(g.send(1))
print(g.send(1))
print(g.send(0))
print(g.send(1))