from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
