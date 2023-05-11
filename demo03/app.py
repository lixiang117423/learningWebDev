from flask import Flask, render_template

app = Flask(__name__)


# 现在是静态的模板
@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html") # 从模板文件夹中自动寻找文件

# 动态渲染示例
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html",
                           username="小蓝哥",
                           blog_id=blog_id) # 第一个blog_id是传入前段html文件的，第二个是后端的这个blog_id

if __name__ == '__main__':
    app.run()
