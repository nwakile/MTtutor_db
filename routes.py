from flask import Flask, request, jsonify
from app import User, Qb, Subject, Performance

app = Flask(__name__)

@app.route('/app/create', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    if data:
        # email, password, balance = views.create_account()
        
        new_user = User(email=data['email'], password= data['password'], phone=data['phone'],
        username= data['username'])
        # new_user.auth_token = generate_auth_token()
        new_user.auth_token = "token"
        new_user.save()
        return jsonify({'status':'success. Please sign-in', 'new user.auth_token': new_user.auth_token})
    return jsonify({"error":"invalid data"})

@app.route("/app/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    return jsonify({"email":email, "password is": password})

    # account = User.login(email, password)
    # if account:
    #     account.set_token()
    #     return jsonify({"token": account.token})
    # return jsonify({"token":""})
@app.route("/app/subjects", methods=["POST"])
def view_subjects():
    data=request.get_json()
    name = data.get('name')
    image_path = data.get('image_path')
    price = data.get('price')
    return jsonify({"name":math, "image_path is": image, "price": 99.99})



@app.route("/app/subjects", methods=["GET"])
def get_subjects():
    subjects = Subject.select_all()
    return jsonify({"subjects":subjects})

@app.route("/app/qb", methods=["GET"])
def get_qb():
    qb = Qb.select_all()
    return jsonify({"qb":qb})

if __name__ == "__main__":
    app.run(debug=True, port=5000)