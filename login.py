from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome  %s'  % name
@app.route('/submit', methods =['POST','GET'])
def submit():
    return render_template('success')


@app.route('/login', methods =['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['form1']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('form1')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug = True)


