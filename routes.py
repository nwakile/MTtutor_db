from flask import Flask, request, jsonify
from app import User, Qb, Subject, Performance
from flask_cors import CORS
import sqlite3


Qb.dbpath = "data/Qb.db"
app = Flask(__name__)
CORS(app)

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
    print(email, password)
    # return jsonify({"email":email, "password is": password})

    account = User.login(email, password)
    print(account)
    if account:
        account.set_token()
        account.save()
        return jsonify({"token": account.token})
    return jsonify({"token":""})

# @app.route("/app/userlogin", methods=["GET"])
# def loginId():
#     loginId = User.login()
#     return jsonify({"email":email, "password":password})

@app.route('/app/fresh_subject', methods=['POST'])
def create_subject():
    data=request.get_json()
    print(data)
    if data:
        new_subject=Subjects(name=data.get('name'), image_path= data.get('image_path'), price=data.get('price'))
        new_subject.save()
        return jsonify({'status':'subject saved. Enjoy!'})
    return jsonify({"error":"invalid data"})

@app.route('/app/new_questions', methods=['POST'])
def create_question():
    data=request.get_json()
    print(data)
    if data:
        new_question=Qb(subject_id=data.get('subject_id'),  topic=data.get('topic'),
        question_no=data.get('question_no'), question_name= data.get('question_name'), answer_a=data.get('answer_a'),
        answer_b=data.get('answer_b'), answer_c= data.get('answer_c'), 
        answer_d=data.get('answer_d'), answer_e=data.get('answer_e'),
        true_answer_1=data.get('true_answer_1'), true_answer_2=data.get('true_answer_2')
        )
        new_question.save()
        return jsonify({'status':'new question saved. Happy studies!'})
    return jsonify({"error":"invalid data"})


@app.route("/app/view_subjects", methods=["POST"])
def view_subjects():
    data=request.get_json()
    name = data.get('name')
    image_path = data.get('image_path')
    price = data.get('price')
    return jsonify({"name":math, "image_path is": image, "price": 99.99})



@app.route("/app/subjects", methods=["GET"])
def get_subjects():
    subjects = Subject.view_subjects()
    return jsonify({"subjects":subjects})

@app.route("/app/questions/<name>", methods=["GET"])
def get_questions(name):
    with sqlite3.connect("data/qb.db") as conn: 
        cursor=conn.cursor()
        sql = """SELECT qb.subject_id, qb.topic, qb.question_no, qb.question_name, qb.answer_a, qb.answer_b, 
                qb.answer_c, qb.answer_d, qb.answer_e, qb.true_answer_1, qb.true_answer_2, subjects.subject
                FROM qb 
                INNER JOIN subjects
                ON qb.subject_id = subjects.pk
                WHERE subjects.subject = ?
            """
        cursor.execute(sql,(name,))
        results=cursor.fetchall()
        return jsonify({"questions":results})


@app.route("/app/test_qs", methods=["GET"])
def get_test(question_no):
    with sqlite3.connect("data/qb.db") as conn: 
        cursor=conn.cursor()
        sql = """SELECT qb.Subject_ID, qb.Topic, qb.Question_No, qb.Question_Name, qb.Answer_A, qb.Answer_B, 
                qb.Answer_C, qb.Answer_D, qb.Answer_E, qb.True_Answer_1, qb.True_Answer_2, Subjects.subject, 
                Performance.user_id, Performance.qb_id Performance.testdate, Performance.success
                FROM qb 
                INNER JOIN Subjects
                ON qb.subject_id = Subjects.pk 
                INNER JOIN Performance
                ON qb.Question_No = Performance.qb_id
                WHERE Qb.question_No =?
                
            """
        cursor.execute(sql,(name,))
        results=cursor.fetchall()
        return jsonify({"test_qs":results})

@app.route("/app/total_qs", methods=["GET"])
def get_allqs(user_id):
    with sqlite3.connect("data/qb.db") as conn: 
        cursor=conn.cursor()
        sql = """SELECT qb.Subject_ID, qb.Topic, qb.Question_No, qb.Question_Name, qb.Answer_A, qb.Answer_B, 
                qb.Answer_C, qb.Answer_D, qb.Answer_E, qb.True_Answer_1, qb.True_Answer_2, Subjects.subject, 
                Performance.user_id, Performance.qb_id Performance.testdate, Performance.success
                FROM qb 
                INNER JOIN Subjects
                ON qb.subject_id = Subjects.pk 
                INNER JOIN Performance
                ON qb.Question_No = Performance.qb_id
                WHERE Performance.user_id=?
                
            """
        cursor.execute(sql,(name,))
        results=cursor.fetchall()
        return jsonify({"total_qs":results})

@app.route("/app/qb", methods=["GET"])
def get_qb():
    qb = Qb.all_questions()
    return jsonify({"qb":qb})



# @app.route("/app/qb", methods=["GET"])
# def get_qb():
#     qb = Qb.questions_for_subject()
#     return jsonify({"qb":qb})

@app.route("/app/performance", methods=["GET"])
def get_performance():
    performance = Performance.view_performance()
    return jsonify({"performance":performance})

if __name__ == "__main__":
    app.run(debug=True, port=5000)