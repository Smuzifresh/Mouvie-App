from . import authblp
from flask import render_template, redirect
from flask_login import login_user, login_required, logout_user

@authblp.route("/profile/sign-up", methods=["GET", "POST"])
def sign_up():
    from flask import current_app
    from database import db
    from .form import Sign_up_form
    from database import User
    from werkzeug.utils import secure_filename
    import os
    
    form = Sign_up_form()
    if form.validate_on_submit():
        
        user = User( firstname = form.firstname.data,
                lastname = form.lastname.data, 
                password = form.password.data,
                email = form.email.data )
        
        file = form.photo.data
        if file:
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            print(file)
            user.avatar=filename
        
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect("/")
    return render_template("sign_up.html",form = form)

@authblp.route("/profile/log-in", methods=["GET", "POST"])
def log_in():
    from .form import Log_in_form
    from database import User

    form = Log_in_form()
    
    if form.validate_on_submit():
        user = {
                "password": form.password.data,
                "email": form.email.data}
        
        jouer = User.query.filter_by(email=user["email"]).first()
        if not jouer or jouer.password != user["password"]:
            return render_template("log_in.html", form = form, error = "UserNotFound, check your email or password!")
        
        login_user(jouer)
        return redirect("/")
                
    return render_template("log_in.html", form = form)

@authblp.route("/profile/log_out")
@login_required
def log_out():
    logout_user()
    return redirect("/")