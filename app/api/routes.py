from lib2to3.pgen2 import token
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Canning, canning_schema, cannings_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return{'yee':'haw'}

@api.route('/cannings', methods = ['POST'])
@token_required
def create_canning(current_user_token):
    fruit_or_vegetable = request.json['fruit_or_vegetable']
    style_of_pack = request.json['style_of_pack']
    jar_size = request.json['jar_size']
    one_to_three_thousand_ft = request.json['one_to_three_thousand_ft']
    three_to_six_thousand_ft = request.json['three_to_six_thousand_ft']
    over_six_thousand_ft = request.json['over_six_thousand_ft']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    canning = Canning(fruit_or_vegetable, style_of_pack, jar_size, one_to_three_thousand_ft,three_to_six_thousand_ft,over_six_thousand_ft, user_token=user_token )

    db.session.add(canning)
    db.session.commit()

    response = canning_schema.dump(canning)
    return jsonify(response)

@api.route('/cannings', methods = ['GET'])
@token_required
def get_canning(current_user_token):
    a_user = current_user_token.token
    cannings = Canning.query.filter_by(user_token = a_user).all()
    response = cannings_schema.dump(cannings)
    return jsonify(response)

@api.route('/cannings/<id>', methods = ['POST','PUT'])
@token_required
def update_canning(current_user_token,id):
    canning = Canning.query.get(id) 
    canning.fruit_or_vegetable = request.json['fruit_or_vegetable']
    canning.style_of_pack = request.json['style_of_pack']
    canning.jar_size = request.json['jar_size']
    canning.one_to_three_thousand_ft = request.json['one_to_three_thousand_ft']
    canning.three_to_six_thousand_ft = request.json['three_to_six_thousand_ft']
    canning.over_six_thousand_ft = request.json['over_six_thousand_ft']
    canning.user_token = current_user_token.token

    db.session.commit()
    response = canning_schema.dump(canning)
    return jsonify(response)

@api.route('/cannings/<id>', methods = ['DELETE'])
@token_required
def delete_canning(current_user_token, id):
    canning = Canning.query.get(id)
    db.session.delete(canning)
    db.session.commit()
    response = canning_schema.dump(canning)
    return jsonify(response)