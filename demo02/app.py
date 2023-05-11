from flask import Flask, request

app = Flask(__name__)

# http 默认80端口，https默认443端口
# URL与视图的本质是path与视图，就是www.my.com/path

@app.route('/') # 这行代码是装饰器
def hello_world():  # put application's code here
    return 'Hello World!'

# 假设需要个人中心
@app.route('/profile') # 这种类型的url是无参的，固定的
def profile():
    return "我是个人中心！~"

# 定义带参数的视图
@app.route('/blog/<blog_id>')
# 如果定义参数类型为整型，可以写成：
# @app.route('/blog/<int:blog_id>')

def blog_detail(blog_id):
    return "您访问的博客是：%s" % blog_id

# 一种特殊的情况，如requst?page=2，这是查询字符串的方式传参
@app.route('/book/list')
def book_list():
    # request.args()是类字典类型
    page = request.args.get("page",default=1,type=int) # 默认是第一页
    return f"您获取的是第{page}页的图书列表！" # {page}表示当前环境中的变量

if __name__ == '__main__':
    app.run()
