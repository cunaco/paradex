from flask import request, jsonify
from app import app, db
from models import User, Record

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password_hash=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password_hash == data['password']:
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/records', methods=['GET', 'POST'])
def records():
    if request.method == 'POST':
        data = request.get_json()
        new_record = Record(user_id=data['user_id'], category=data['category'], content=data['content'])
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Record created successfully'})
    records = Record.query.all()
    return jsonify([record.to_dict() for record in records])
