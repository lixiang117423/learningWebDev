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
    return 'Hello China!'

if __name__ == '__main__':
    app.run()