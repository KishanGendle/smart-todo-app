from flask import Blueprint, render_template, request, redirect, flash, session
from config.db import mongo
from bson.objectid import ObjectId
from datetime import datetime

task = Blueprint('task', __name__)

# Dashboard
@task.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        flash("Please Login First", "danger")
        return redirect('/login')

    search_query = request.args.get('search')

    if search_query:

        tasks = mongo.db.tasks.find({
            "user_id": session['user_id'],
            "title": {
                "$regex": search_query,
                "$options": "i"
            }
        }).sort("created_at", -1)

    else:

        tasks = mongo.db.tasks.find({
            "user_id": session['user_id']
        }).sort("created_at", -1)

    return render_template(
        'dashboard.html',
        tasks=tasks
    )


# Add Task
@task.route('/add-task', methods=['POST'])
def add_task():

    if 'user_id' not in session:
        return redirect('/login')

    title = request.form.get('title')

    mongo.db.tasks.insert_one({
        "user_id": session['user_id'],
        "title": title,
        "status": "Pending",
        "created_at": datetime.now()
    })

    flash("Task Added Successfully", "success")

    return redirect('/dashboard')


# Complete Task
@task.route('/complete-task/<task_id>')
def complete_task(task_id):

    if 'user_id' not in session:
        return redirect('/login')

    mongo.db.tasks.update_one(
        {
            "_id": ObjectId(task_id)
        },
        {
            "$set": {
                "status": "Completed"
            }
        }
    )

    flash("Task Completed", "success")

    return redirect('/dashboard')


# Delete Task
@task.route('/delete-task/<task_id>')
def delete_task(task_id):

    if 'user_id' not in session:
        return redirect('/login')

    mongo.db.tasks.delete_one({
        "_id": ObjectId(task_id)
    })

    flash("Task Deleted", "danger")

    return redirect('/dashboard')


# Edit Task
@task.route('/edit-task/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):

    if 'user_id' not in session:
        return redirect('/login')

    task_data = mongo.db.tasks.find_one({
        "_id": ObjectId(task_id)
    })

    if request.method == 'POST':

        updated_title = request.form.get('title')

        mongo.db.tasks.update_one(
            {
                "_id": ObjectId(task_id)
            },
            {
                "$set": {
                    "title": updated_title
                }
            }
        )

        flash("Task Updated Successfully", "success")

        return redirect('/dashboard')

    return render_template(
        'edit_task.html',
        task=task_data
    )