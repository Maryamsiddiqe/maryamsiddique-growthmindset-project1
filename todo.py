import streamlit as st
import datetime
import random

# Motivational Quotes List
quotes = [
    "Believe you can and you're halfway there.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Don't watch the clock; do what it does. Keep going.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Every day is a new beginning. Take a deep breath and start again."
]

# Custom background & CSS
page_bg = """
<style>
    body {
        background-color: #f8f9fa;
    }
    .stApp {
        background-image: url('https://source.unsplash.com/1600x900/?nature,abstract');
        background-size: cover;
        background-position: center;
    }
    .title {
        font-size: 40px;
        color: #ffffff;
        text-align: center;
        text-shadow: 2px 2px 5px black;
    }
    .task-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .completed {
        text-decoration: line-through;
        color: gray;
    }
    .priority-low {
        color: green;
    }
    .priority-medium {
        color: orange;
    }
    .priority-high {
        color: red;
        font-weight: bold;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App title
st.markdown("<h1 class='title'>📋 Complete Growth Mindset  To-Do List By Maryam Siddique</h1>", unsafe_allow_html=True)

# Show a random motivational quote
st.markdown(f"🌟 *{random.choice(quotes)}*")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Add New Task
st.subheader("➕ Add a New Task")
task_name = st.text_input("Task Name:")
task_due = st.date_input("Due Date:", min_value=datetime.date.today())
task_time = st.time_input("Due Time:")
task_priority = st.selectbox("Priority Level:", ["Low", "Medium", "High"])

if st.button("Add Task"):
    if task_name:
        st.session_state["tasks"].append({
            "task": task_name,
            "due": task_due,
            "time": task_time,
            "priority": task_priority,
            "done": False
        })
        st.rerun()

# Display Tasks

st.subheader("📌 Your Tasks")
tasks_to_remove = []
completed_tasks = sum(1 for task in st.session_state["tasks"] if task["done"])
total_tasks = len(st.session_state["tasks"])


 # Show task count before Clear All Button
st.markdown(f"###  {total_tasks}Tasks ")

# Progress Bar
if total_tasks > 0:
    progress = completed_tasks / total_tasks
    st.progress(progress)

for i, task in enumerate(st.session_state["tasks"]):
    col1, col2, col3, col4 = st.columns([0.05, 0.65, 0.15, 0.15])

    with col1:
        checked = st.checkbox("", value=task["done"], key=f"check_{i}")
        st.session_state["tasks"][i]["done"] = checked

    with col2:
        priority_class = "priority-low" if task["priority"] == "Low" else "priority-medium" if task["priority"] == "Medium" else "priority-high"
        task_text = f"<span class='{priority_class}'>{task['task']} (Due: {task['due']} {task['time']})</span>"
        if task["done"]:
            task_text = f"<span class='completed'>{task['task']} (Due: {task['due']} {task['time']}) ✅</span>"
        st.markdown(f"<div class='task-box'>{task_text}</div>", unsafe_allow_html=True)

    with col3:
        st.markdown(f"<span class='{priority_class}'>{task['priority']}</span>", unsafe_allow_html=True)

    with col4:
        if st.button("Remove", key=f"remove_{i}"):
            tasks_to_remove.append(i)

# Remove selected tasks
if tasks_to_remove:
    for i in sorted(tasks_to_remove, reverse=True):
        del st.session_state["tasks"][i]
    st.rerun()

   

# Clear All Button
if st.button(" Clear All Tasks", key="clear_all"):
    st.session_state["tasks"] = []
    st.rerun()
