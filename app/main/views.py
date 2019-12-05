from flask import render_template,url_for,redirect
from . import main
from app import db
from flask_login import login_required,current_user
from .forms import updateForm
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
    user = User.query.filter_by(username=uname).first()
    return render_template('profile/profile.html')

@main.route('/profile/<uname>/edit', methods=['GET', 'POST'])
def update(uname):

    form = updateForm()
    if form.validate_on_submit():
        qualities = Quality(age=form.age.data, gender=form.gender.data, complexion=form.complexion.data, personality=form.personality.data)
        db.session.add(qualities)
        db.session.commit()
        return redirect(url_for('main.profile', uname=uname))

    title = 'Update profile'
    return render_template('profile/update.html',form=form, uname=uname, title=title)

