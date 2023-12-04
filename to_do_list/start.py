from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to store tasks
tasks = []
completed_tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'content': task, 'complete': False})
        completed_tasks.append(({'content': task, 'complete': True}))
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)