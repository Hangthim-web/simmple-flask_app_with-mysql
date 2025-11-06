from flask import Blueprint, render_template,session,request,redirect,url_for,flash
from app.models.blogs import db,Blog 
blog_bp = Blueprint('blogs',__name__)



@blog_bp.route('/create-blog',methods=["GET","POST"])
def create_blog():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        new_blog = Blog(
            title = title ,
            description = description
        )
        db.session.add(new_blog)
        db.session.commit()

        flash("Successfully added new blog",'success')
        return redirect(url_for('blogs.create_blog'))
    return render_template('blog.html')