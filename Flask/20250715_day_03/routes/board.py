from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from .db import db
from orm_models import Board

board_blp = Blueprint('Boards', 'boards', description='operations on boards', url_prefix='/board')

# API List
# /board
# 전체 게시글을 불러오기 (GET)
# 게시글 작성 (POST)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        # 게시글 목록을 불러오기
        if not boards:
            return jsonify({"msg": "No boards found"}), 404
        return jsonify([{"user_id": board.user_id,
                         "id": board.id,
                         "title": board.title, "content": board.content, "author": board.author.name} for board in boards])
        
        # pass

    def post(self):
        data = request.json
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        print(new_board)

        db.session.add(new_board)
        db.session.commit()
        
        return jsonify({'msg': 'success create board'}), 201


# /board/<int: board_id>
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)

        return jsonify({'id': board.id,
                        'title':board.title, 
                        'content': board.content,
                        'user_id': board.author.id,
                        'author': board.author.name
                        })

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return jsonify({"msg": "Successfully updated board data"}), 201

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"msg": "Successfully deleted board data"}), 204


board_blp.add_url_rule('/<int:board_id>', view_func=BoardResource.as_view('board_resource'))