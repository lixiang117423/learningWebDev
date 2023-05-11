from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 定义user的类
class User:
    def __init__(self, username, email, value):
        self.username = username
        self.email = email
        self.value = value

# 自定义过滤器
def minustoone(value):
    return value-1
app.add_template_filter(minustoone,"myfilter") # myfilter表示的是过滤器的名称

def formatetime(now_time, format="%Y-%d-%m %H:%M"):
    return now_time.strftime(format)
app.add_template_filter(formatetime, "timefilter")



# 现在是静态的模板
@app.route('/')
def hello_world():  # put application's code here
    user = User(username="xiang", email="test@qq.com")
    # 如果是字典的情况
    person = {
        "email":"123@qq.com",
        "user":"lixiang"
    }
    return render_template("index.html", user=user, person=person) # 从模板文件夹中自动寻找文件

# 动态渲染示例
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html",
                           username="小蓝哥",
                           blog_id=blog_id) # 第一个blog_id是传入前段html文件的，第二个是后端的这个blog_id

# 过滤器使用
@app.route('/filter')
def filter_demo():
    user = User(username="xiang123495", email="test@qq.com", value=100)
    time = datetime.now()
    return render_template("filter.html", user=user, time=time)

# 控制语句
@app.route('/control')
def control_stst():
    age = 18
    books = [{
        "name":"三国演义",
        "author":"罗贯中"
    },
        {
            "name": "个人专辑",
            "author": "小蓝哥"
        }
    ]
    return render_template("control.html",age=age,books=books)

# 子页面
@app.route('/child1')
def child1():
    return render_template("child1.html")

# 子页面2
@app.route('/child2')
def child2():
    return render_template("child2.html")

if __name__ == '__main__':
    app.run()
