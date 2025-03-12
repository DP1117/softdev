# routes.py

from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, StoryForm, ContributionForm
from app.models import User, Story, Contribution
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
@login_required
def home():
    user_stories = Story.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', stories=user_stories)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/new_story", methods=['GET', 'POST'])
@login_required
def new_story():
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(title=form.title.data, user_id=current_user.id)
        contribution = Contribution(content=form.content.data, user_id=current_user.id, story=story)
        db.session.add(story)
        db.session.add(contribution)
        db.session.commit()
        flash('Your story has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('new_story.html', title='New Story', form=form)

@app.route("/story/<int:story_id>", methods=['GET', 'POST'])
@login_required
def story(story_id):
    story = Story.query.get_or_404(story_id)
    latest_contribution = Contribution.query.filter_by(story_id=story.id).order_by(Contribution.date_posted.desc()).first()
    form = ContributionForm()
    if form.validate_on_submit():
        contribution = Contribution(content=form.content.data, user_id=current_user.id, story_id=story.id)
        db.session.add(contribution)
        db.session.commit()
        flash('Your contribution has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('add_to_story.html', title=story.title, form=form, latest_contribution=latest_contribution)
