from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user

UPLOAD_FOLDER = './received/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "sfdjkafnk"

# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.init_app(app)

user_id = 12
choices = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_data = request.form['user_id']
        user_id = form_data
        if form_data:
            # User input logic
            return render_template('user_choices.html', user_id=user_id, selected_items = choices)

    return render_template('index.html')


@app.route('/user-choices' , methods=['GET', 'POST'])
def user_choices():
    if request.method == 'POST':
        choices = request.form['selections_array']
        return redirect(url_for('output', user_id=user_id, selected_items = choices))
    return render_template('user_choices.html', user_id=user_id, selected_items = choices)

@app.route('/user-genre/<selected_items>')
def output(selected_items):
    # output logic
    return render_template('user_genre.html', user_id=user_id, selected_items = selected_items)

if __name__ == '__main__':
    app.run(debug=True)