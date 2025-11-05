from flask import Blueprint,render_template,session,request,redirect,url_for,flash
from user import db,User
from werkzeug.security import generate_password_hash
user_bp = Blueprint('auth',__name__)

@user_bp.route('create-user',methods=['GET','POST'])
def create_user():
    if request.method=="POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        age = request.form.get('age')
        is_active = request.form.get('is_active')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email Already Registered !","danger")
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)

        new_user = User(
            first_name = first_name ,
            last_name = last_name,
            email = email, 
            password = hashed_password,
            age = age, 
            is_active = is_active 
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful",'success')
        return redirect(url_for('register'))
    return render_template('register.html')

