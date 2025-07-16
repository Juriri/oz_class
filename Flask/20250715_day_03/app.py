from flask import Flask, render_template
from flask_smorest import Api
from flask_cors import CORS

from routes.db import db
from routes.user import user_blp
from routes.board import board_blp
from models import User, Board

app = Flask(__name__)
CORS(app)  # CORS 설정
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["API_TITLE"] = "User & Board API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

db.init_app(app)

# API 관리용 Flask-Smorest 객체 생성
api = Api(app)
api.register_blueprint(user_blp)
api.register_blueprint(board_blp)

@app.route("/")
def home():
    return render_template("home.html")     # 메인 페이지

@app.route("/users")
def user_page():
    return render_template("users.html")    # 사용자 관리

@app.route("/boards")
def board_page():
    return render_template("boards.html")   # 게시판 관리

# 앱 실행
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
