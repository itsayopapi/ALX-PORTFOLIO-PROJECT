from flask import Blueprint, jsonify, request
from models import db, Conditions, Strategies, User, YoutubeContent, SpotifyContent

api_db = Blueprint('api', __name__)

# Get Requests


@api_db.route('/api/conditions', methods=['GET'])
def get_conditions():
    conditions = Conditions.query.all()
    condition_list = []
    for condition in conditions:
        condition_data = {
            'id': condition.id,
            'created_on': condition.created_on,
            'updated_on': condition.updated_on,
            'condition_name': condition.condition_name,
            'user_id ': condition.user_id
        }
        condition_list.append(condition_data)
    return jsonify(condition_list), 200


@api_db.route('/api/strategies', methods=['GET'])
def get_strategy():
    strategies = Strategies.query.all()
    strategy_list = []
    for strategy in strategies:
        strategy_data = {
            'id': strategy.id,
            'created_on': strategy.created_on,
            'updated_on': strategy.updated_on,
            'strategy_name': strategy.strategy_name,
            'strategy_text': strategy.strategy_text,
            'condition_id': strategy.condition_id
        }
        strategy_list.append(strategy_data)
    return jsonify(strategy_list), 200


@api_db.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'created_on': user.created_on,
            'updated_on': user.updated_on,
            'name': user.name,
            'surname': user.surname,
            'username': user.username,
            'password': user.password,
            'email': user.email
        }
        user_list.append(user_data)
    return jsonify(user_list), 200

# Post requests


@api_db.route('/api/conditions', methods=['GET', 'POST'])
def conditions():
    if request.method == 'POST':
        data = request.get_json()
        new_condition = Conditions(
            condition_name=data['condition_name'],
            user_id=data['user_id']
        )
        db.session.add(new_condition)
        db.session.commit()
        return jsonify({'message': 'Condition created successfully'}), 201
    else:
        conditions = conditions.query.all()
        condition_list = []
        for condition in conditions:
            condition_data = {
                'id': condition.id,
                'created_on': condition.created_on,
                'updated_on': condition.updated_on,
                'condition_name': condition.condition_name,
                'user_id': condition.user_id
            }
        condition_list.append(condition_data)
    return jsonify(condition_list), 200


@api_db.route('/api/strategies', methods=['GET', 'POST'])
def strategies():
    if request.method == 'POST':
        data = request.get_json()
        new_strategy = Strategies(
            strategy_name=data['strategy_name'],
            strategy_text=data['strategy_text'],
            condition_id=data['condition_id']
        )
        db.session.add(new_strategy)
        db.session.commit()
        return jsonify({'message': 'Strategy created successfully'}), 201
    else:
        strategies = strategies.query.all()
        strategy_list = []
        for strategy in strategies:
            strategy_data = {
                'id': strategy.id,
                'created_on': strategy.created_on,
                'updated_on': strategy.updated_on,
                'strategy_name': strategy.strategy_name,
                'strategy_text': strategy.strategy_text,
                'condition_id': strategy.condition_id
            }
            strategy_list.append(strategy_data)
        return jsonify(strategy_list), 200


@api_db.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        new_user = User(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'user created successfully'}), 201
    else:
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'created_on': user.created_on,
                'updated_on': user.updated_on,
                'name': user.name,
                'surname': user.surname,
                'email': user.email,
                'password': user.password,
            }
            user_list.append(user_data)
        return jsonify(user_list), 200

# The Put


@api_db.route('/api/condition/<int:condition_id>', methods=['PUT'])
def update_condition(condition_id):
    condition = Conditions.query.get_or_404(condition_id)
    if request.method == 'PUT':
        data = request.get_json()
        condition.condition_name = data['condition_name']
        condition.user_id = data['user_id']
        db.session.commit()
        return jsonify({'message': 'condition updated successfully'}), 200


@api_db.route('/api/strategies/<int:strategy_id>', methods=['PUT'])
def update_strategy(strategy_id):
    strategy = Strategies.query.get_or_404(strategy_id)
    if request.method == 'PUT':
        data = request.get_json()
        strategy.strategy_name = data['strategy_name']
        strategy.strategy_text = data['strategy_text']
        strategy.condition_id = data['condition_id']
        db.session.commit()
        return jsonify({'message': 'strategy updated successfully'}), 200


@api_db.route('/api/user/<int:user_id>', methods=['GET'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'GET':
        data = request.get_json()
        user.name = data['name']
        user.surname = data['surname']
        user.email = data['email']
        user.password = data['password']
        db.session.commit()
        return jsonify({'message': 'user updated successfully'}), 200

# Delete Request


@api_db.route('/api/conditions/<int:condition_id>', methods=['DELETE'])
def delete_condition(condition_id):
    condition = Conditions.query.get_or_404(condition_id)
    if request.method == 'DELETE':
        db.session.delete(condition)
        db.session.commit()
        return jsonify({'message': 'Condition deleted successfully'}), 200


@api_db.route('/api/strategies/<int:strategy_id>', methods=['DELETE'])
def delete_strategy(strategy_id):
    strategy = Strategies.query.get_or_404(strategy_id)
    if request.method == 'DELETE':
        db.session.delete(strategy)
        db.session.commit()
        return jsonify({'message': 'strategy deleleted successfully'}), 200


@api_db.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200


@api_db.route('/api/youtube_content/<int:content_id>', methods=['GET'])
def get_youtube_content(content_id):
    content = YoutubeContent.query.get_or_404(content_id)
    if request.method == 'GET':
        content_data = {
            'id': content.id,
            'created_on': content.created_on,
            'updated_on': content.video_title,
            'youtube_content': content.youtube_content,
            'strategy_id': content.strategy_id
        }
        return jsonify(content_data), 200


@api_db.route('/api/spotify_content/<int:content_id>', methods=['GET'])
def get_spotify_content(content_id):
    content = SpotifyContent.query.get_or_404(content_id)
    if request.method == 'GET':
        content_date = {
            'id': content.id,
            'created_on': content.created_on,
            'updated_on': content.updated_on,
            'podcast_title': content.podcast_title,
            'podcast_content': content.podcast_content,
            'strategy_id': content.strategy_id
        }
        return jsonify(content_date), 200


@api_db.route('/api/youtube_content/', methods=['POST'])
def create_youtube_content():
    data = request.get_json()
    video_title = data.get('video_title')
    youtube_content = data.get('youtube_content')
    strategy_id = data.get('strategy_id')

    content = YoutubeContent(
        video_title=video_title,
        youtube_content=youtube_content,
        strategy_id=strategy_id
    )

    db.session.add(content)
    db.session.commit()

    response_data = {
        'id': content. id,
        'created_on': content.created_on,
        'video_title': content.video_title,
        'youtube_content': content.youtube_content,
        'strategy_id': content.strategy_id
    }
    return jsonify(response_data), 201


@api_db.route('/api/spotify_content', methods=['POST'])
def create_spotify_content():
    data = request.get_json()
    podcast_title = data.get('podcast_title')
    podcast_content = data.get('podcast_content')
    strategy_id = data.get('strategy_id')

    content = SpotifyContent(
        podcast_title=podcast_title,
        podcast_content=podcast_content,
        strategy_id=strategy_id
    )
    db.session.add(content)
    db.session.commit()

    response_data = {
        'id': content.id,
        'created_on': content.created_on,
        'updated_on': content.updated_on,
        'podcast_title': content.podcast_title,
        'podcast_content': content.podcast_content,
        'strategy_id': content.strategy_id
    }

    return jsonify(response_data), 201
