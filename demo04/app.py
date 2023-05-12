from flask import Flask
from flask_sqlalchemy import SQLAlchemy # 加载数据库用的包
from sqlalchemy import text

app = Flask(__name__)

# 创建app.config文件
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "1288"
DATABASE = "learningwebdev"

# app.config文件配置格式
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

# 在app.confg中设置好连接数据库的信息
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中的配置信息

db = SQLAlchemy(app)

# 测试数据库连接
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone()) # 输出（1，）就说明数据库连接正常

# ORM（对象关系映射）学习
class User(db.Model): # 注意Model首字母大写
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False) # 最大长度100，不能为空
    password = db.Column(db.String(100), nullable=False)

# 定义新的表
class Article(db.Model):
    __table__name = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 添加外键
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #author = db.relationship("User", back_ref="article")

article = Article(title="一二布布旅行日记",content="1288")

# 假设注册用户写入数据库
# user = User(username = "法外狂徒长三", password = "1288")

# 将属性应用到数据库
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 创建数据
@app.route('/user/add')
def add_user():
    # 创建
    user = User(username="一二", password="12")
    # 添加
    db.session.add(user)
    # 提交
    db.session.commit()
    # 提示信息
    return "用户创建成功！"

# 查询数据
@app.route('/user/query')
def query_user():
    user = User.query.get(1)
    print(f"{user.id}:{user.username}-{user.password}")

    # filter_by查找,返回的结果的类数组
    users = User.query.filter_by(username="一二")
    for user in users:
        print(user.username)

    return "数据查找成功！"

# 更新数据
@app.route('/user/update')
def user_update():
    user = User.query.filter_by(username="一二").first()
    user.password = "8812"
    db.session.commit()
    return "数据修改成功！"

# 删除数据
@app.route('/user/del')
def user_del():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return "数据删除成功！"

if __name__ == '__main__':
    app.run()
