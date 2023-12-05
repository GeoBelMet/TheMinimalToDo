from flask import Flask, render_template, request, redirect, url_for
import uuid
app = Flask(__name__)

# Sample data to store tasks
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        id = uuid.uuid4()
        tasks.append({'id': id, 'content': task, 'complete': False})
        print(id)
        print(tasks)

    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)