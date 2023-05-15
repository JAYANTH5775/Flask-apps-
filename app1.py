from flask import Flask, render_template, request
from openpyxl import Workbook, load_workbook

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def feedback_form():
    if request.method == 'POST':

        visited = request.form['visited']
        reason = request.form['reason']
        needed = request.form['needed']
        looking_for = request.form['looking_for']
        easy = request.form['easy']
        impression = request.form['impression']

        try:
            wb = load_workbook('templates/template.xlsx')
            ws = wb.active
        except FileNotFoundError:
            wb = Workbook()
            ws = wb.active
            ws.append(['Visited', 'Primary reason', 'Found what needed', 'Looking for', 'Easy to find info', 'Overall impression'])
        ws.append([visited, reason, needed, looking_for, easy, impression])

        wb.save('template.xlsx')

        return render_template('success.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
