# 导入Flask类
from flask import Flask

# __name__表示当前的app.py这个模块
# 出现bug可以快速定位
# 寻找模板文件有相对路径
app = Flask(__name__)

# 创建路由和视图函数映射
# /表示根路由
@app.route('/')
def hello_world():
    return 'Hello 中国!'

# 1. debug模式
# 1.1只要开启debug模式，修改代码后不用再次运行，保存后就会重新加载，不用重启
# 1.2 如果出现报错，浏览器会显示报错信息

# 2. 修改host
# 让其他电脑可以访问该项目

# 3.修改port
# 指定端口避免被占用等

if __name__ == '__main__':
    app.run()