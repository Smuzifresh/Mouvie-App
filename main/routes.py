from flask import render_template, request, current_app
from .api import get_popular_mouvies, top_rated, get_details, get_videos, get_similar_films, get_upcoming_films, search_films
from . import mainblp
from flask_login import login_required

@mainblp.route("/")
@mainblp.route("/home")
def index():
    mouvies = get_popular_mouvies()
    pmouvies = top_rated()
    upcoming_mouvies = get_upcoming_films()

    return render_template("index.html", mouvies=mouvies[0:5], apmouvies=pmouvies[0:5],upcoming_mouvies=upcoming_mouvies)
    

@mainblp.route("/films/search", methods=["POST"])
def searcher_film():
    if request.method == "POST":
        query = request.form.get("query")
        searcher = search_films(query)
        print(searcher)

        return render_template("mouvie_list.html", pmouvies=searcher)

@mainblp.route("/films/top-rated")
def top_rated_page():
    page = request.args.get("page",1)
    pmouvies = top_rated(page)
    return render_template("mouvie_list.html", pmouvies=pmouvies)

@mainblp.route("/films/popular")
def pop_mouvies():
    page = request.args.get("page",1)
    mouvies = get_popular_mouvies(page)
    return render_template("mouvie_list.html", pmouvies=mouvies)



@mainblp.route("/films/details/<int:id>", methods=["GET", "POST"])
@login_required
def mouvis_details(id):
    from .forms import CommentForm
    from data.comment import Comment
    from data.liked_films import Liked_Films
    from sqlalchemy import desc
    from app.extensions import db

    from flask_login import current_user
    dmouvies = get_details(id)
    videos = get_videos(id)
    similar_videos = get_similar_films(id)

    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(user_id = current_user.id, message = form.message.data, film_id = id, user=current_user)
        db.session.add(comment)
        db.session.commit()

    coments = Comment.query.filter_by(film_id = id,).order_by(desc(Comment.date)).all()
    liked = Liked_Films.query.filter_by(film_id = id, user_id = current_user.id).first() is not None

    return render_template("details.html",data=dmouvies, video = videos[0], similar_videos = similar_videos[0:4], form=form, comments = coments, liked = liked)



@mainblp.route("/films/upcoming-films")
def upcoming_films():
    page = request.args.get("page",1)
    mouvies = get_upcoming_films(page)
    return render_template("mouvie_list.html", pmouvies=mouvies)
    

@mainblp.route("/profile", methods=["GET", "POST"])
@login_required
def prf():
    from .forms import Update
    from werkzeug.utils import secure_filename
    import os
    from flask_login import current_user

    liked_films = current_user.liked_films
    print(liked_films)

    upd=Update()

    if upd.validate_on_submit():
        print(upd.photo.data)

        print("print")

        file = upd.photo.data
        filename = secure_filename(file.filename)

        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        current_user.avatar=filename
        
    return render_template("profile.html", upd=upd, l_f=liked_films)

@mainblp.route("/films/like/<int:id>")
@login_required
def liked(id):
    from flask import jsonify
    from data.liked_films import Liked_Films
    from flask_login import current_user
    from app.extensions import db
 
    print(id)
    film = get_details(id)
    if id and current_user:
        film_local = Liked_Films.query.filter_by(film_id=id,user_id=current_user.id).first()
        print(film_local)
        if film_local :
            db.session.delete(film_local)
            db.session.commit()
            print("deleted")
        else:
            mouvie = Liked_Films(film_id = id, title = film.get("title"), release_date = film.get("release_date"),
                                vote_average = film.get("vote_average"), poster_path = film.get("poster_path"),
                                user_id = current_user.id )
            
            db.session.add(mouvie)
            db.session.commit()
            print("saved")

        print("film saved")
    return jsonify({"status":"success"})
