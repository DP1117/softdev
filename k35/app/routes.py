from flask import render_template, url_for, flash, redirect, request, session
from app import app
from app.forms import RegistrationForm, LoginForm, StoryForm, ContributionForm
from app.db_functions import add_user, get_user_by_email, get_user_by_id, add_story, add_contribution, get_latest_contribution, get_user_stories, get_story_by_id
from app.auth import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route("/home")
@login_required
def home():
    user_stories = get_user_stories(current_user().id)
    return render_template('index.html', stories=user_stories)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user():
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user(form.username.data, form.email.data, form.password.data)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user():
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and user.password == form.password.data:
            login_user(user)
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
        story_id = add_story(form.title.data, current_user().id)
        add_contribution(form.content.data, current_user().id, story_id)
        flash('Your story has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('new_story.html', title='New Story', form=form)

@app.route("/story/<int:story_id>", methods=['GET', 'POST'])
@login_required
def story(story_id):
    story = get_story_by_id(story_id)
    latest_contribution = get_latest_contribution(story_id)
    form = ContributionForm()
    if form.validate_on_submit():
        add_contribution(form.content.data, current_user().id, story_id)
        flash('Your contribution has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('add_to_story.html', title=story['title'], form=form, latest_contribution=latest_contribution)
