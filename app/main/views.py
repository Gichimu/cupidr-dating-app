from flask import render_template,url_for,redirect,request
from . import main
from app import db, photos
from sqlalchemy import and_
from flask_login import login_required,current_user
from .forms import updateForm, findMatches, photoForm
from ..models import Quality, User
from werkzeug.utils import secure_filename


#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """

    title = 'Home | cupidR'
    return render_template('index.html', title = title)

@main.route('/profile/<uname>', methods=['GET', 'POST'])
def profile(uname):
    """ View function that returns profile page """
    users=None
    form = findMatches()
    user = User.query.filter_by(username=uname).first()
    if form.validate_on_submit():
        matches = Quality.query.filter_by(gender=form.gender.data, complexion=form.complexion.data, personality=form.personality.data).all()
        for match in matches:
            users = User.query.filter_by(id=match.user_id).all()
        # return redirect(url_for('main.profile', uname=uname, users=users))
    
    return render_template('profile/profile.html', form=form, users=users)

@main.route('/profile/<uname>/edit', methods=['GET', 'POST'])
def update(uname):

    form = updateForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=uname).first()
        qualities = Quality(age=form.age.data, gender=form.gender.data, complexion=form.complexion.data, personality=form.personality.data, height=form.height.data, user_id=user.id)
        db.session.add(qualities)
        db.session.commit()
        return redirect(url_for('main.profile', uname=uname))

    title = 'Update profile'
    return render_template('profile/update.html',form=form, uname=uname, title=title)


@main.route('/profile/<uname>/find', methods=['GET', 'POST'])
def find(uname):

    
    title='Find matches'
    return render_template('profile/find.html', form=form, title=title)


@main.route('/user/<uname>/update_photo', methods=['POST'])
@login_required
def update_photo(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))





