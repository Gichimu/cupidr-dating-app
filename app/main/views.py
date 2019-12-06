from flask import render_template,url_for,redirect
from . import main
from app import db
from sqlalchemy import and_
from flask_login import login_required,current_user
from .forms import updateForm, findMatches
from ..models import Quality, User


#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """

    title = 'Home | cupidR'
    return render_template('index.html', title = title)

@main.route('/profile/<uname>')
def profile(uname):
    """ View function that returns profile page """
    text = None
    users = None
    user = User.query.filter_by(username=uname).first()
    


    return render_template('profile/profile.html')

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

    form = findMatches()
    users = None
    if form.validate_on_submit():
        qualities_sets = Quality.query.filter_by(gender=form.gender.data, complexion=form.complexion.data, personality=form.personality.data).all()
        for qualities_set in qualities_sets:
            users = User.query.filter_by(id=qualities_set.user_id).all()

        return redirect(url_for('main.profile', uname=uname, users=users))

    title='Find matches'
    return render_template('profile/find.html', form=form, title=title)




