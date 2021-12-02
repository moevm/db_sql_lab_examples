import sqlalchemy as sa
from flask import Blueprint, request
from flask.json import jsonify
from sqlalchemy.util.langhelpers import set_creation_order

from prac_12.config import DBConn
from prac_12.models import Shelf

__all__ = ['shelf']

shelf = Blueprint('shelf', 'shelf')


@shelf.route('/', methods=['GET'])
def get_all():
    """
    Вернуть все объекты
    ---
    consumes:
      - application/json
    responses:
      200:
        description: ОК
    """
    with DBConn.get_session() as sess:
        result = sess.execute(sa.select(Shelf))
        # marshmallow
        # marshmallow-sqlalchemy
        return jsonify([r[0].to_dict() for r in result.all()])


@shelf.route('/', methods=['POST'])
def create_one():
    """
    Создать один
    ---
    consumes:
      - application/json
    parameters:
     - in: body
       name: data
       required: true
    responses:
      200:
        description: ОК
    """
    body = request.get_json()
    with DBConn.get_session() as sess:
        row = Shelf(**body)

        sess.add(row)
        sess.flush()
        sess.commit()
        ret = row.to_dict()

    return jsonify(ret)


@shelf.route('/', methods=['DELETE'])
def delete_one():
    """
    Удалить один
    ---
    parameters:
     - in: query
       name: id
       required: true
    responses:
      200:
        description: ОК
    """
    with DBConn.get_session() as sess:
        res = sess.execute(sa.select(Shelf).where(Shelf.id == request.args.get('id')))
        res = res.all()
        if len(res) == 0:
            return jsonify({'message': 'not found'}), 404
        ret = res[0][0].to_dict()
        sess.execute(sa.delete(Shelf).where(Shelf.id == request.args.get('id')))
        sess.commit()
    return ret

@shelf.route('/', methods=['PUT'])
def update_one():
    """
    Обновить один
    ---
    consumes:
      - application/json
    parameters:
     - in: query
       name: id
       required: true
     - in: body
       name: data
       required: true
    responses:
      200:
        description: ОК
    """
    body = request.get_json()
    with DBConn.get_session() as sess:
        res = sess.execute(sa.select(Shelf).where(Shelf.id == request.args.get('id')))
        row = res.one()[0]

        for k, v in body.items():
            setattr(row, k, v)

        sess.add(row)
        sess.flush()
        sess.commit()
        ret = row.to_dict()

    return jsonify(ret)
