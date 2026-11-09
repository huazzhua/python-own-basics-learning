from distutils.core import setup

setup(
    name="graphic",# x需要打包的名字
    version= "1.0",  # 打包的版本
    py_modules = ["graphic.circle","graphic.rectangle"]  # 需要打包的模块
)