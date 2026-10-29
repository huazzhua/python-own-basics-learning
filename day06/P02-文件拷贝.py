"""
    该案例演示了文件的拷贝功能
"""

# def copy_file(src,dest):
#     # 打开源文件
#     src_file = open(src,'rb')
#     # 从源文件中读取数据到程序中
#     content = src_file.read()
#
#     # 打开目标文件
#     dest_file = open(dest,'wb')
#     # 将读取到的数据写到目标文件中
#     dest_file.write(content)
#
#
#     # 关闭源文件
#     src_file.close()
#
#     # 关闭目标文件
#     dest_file.close()
#
# copy_file("C:\\Users\huahua\Desktop\文件夹2\图片\DSC09493.jpg","E:\\软件项目\python大模型学习\python基础学习\day06\q.jpg")



# 优化文件拷贝

def copy_file(src,dest):
    # 打开源文件
    src_file = open(src,'rb')

    # 打开目标文件
    dest_file = open(dest,'wb')

    # 从源文件中读取数据到程序中
    while  content := src_file.read():
        # 将读取到的数据写到目标文件中
        dest_file.write(content)




    # 关闭源文件
    src_file.close()

    # 关闭目标文件
    dest_file.close()

copy_file("C:\\Users\huahua\Desktop\文件夹2\图片\DSC09493.jpg","E:\\软件项目\python大模型学习\python基础学习\day06\q.jpg")







