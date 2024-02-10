import time
import random
import login_script
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            comments_text.delete(1.0, tk.END)
            comments_text.insert(tk.END, file.read())


def generateTimes(intervals):
    times = list()
    for min, duration in intervals:
        num_of_comments = int(int(duration)/int(min))
        for _ in range(num_of_comments):
            times.append(min)
    times.reverse()
    return times

def start_job():
    global link_entry
    global comments_text
    global email_entry
    global password_entry 
    global interval_minutes_entries
    global interval_duration_entries
    global label_var

    link = link_entry.get()
    input_comments = comments_text.get(1.0, tk.END).splitlines()
    email = email_entry.get()
    password = password_entry.get()
    
    comments = list()
    for comment in input_comments:
        comments.append(comment)
    
    intervals = list()
    for minutes, duration in zip(interval_minutes_entries, interval_duration_entries):
        intervals.append((minutes.get(), duration.get()))
    
    times = generateTimes(intervals)
    
    label_var.set("Starting")
    time.sleep(1)
    comments.reverse()
    print("Starting")
    while comments and times:
        next_comment = comments.pop()
        print(f"Working on comment: {next_comment}")
        time_to_wait = times.pop()
        print(f"Time to wait till posting next comment: {time_to_wait}")
        try:
            login_script.run_job(link, next_comment, email, password)
        except:
            print("Failed to run job.")
        label_var.set(next_comment)
        if comments and times:
            time.sleep((int(time_to_wait)*60)+random.randint(0, 15))
    print("done")
    label_var.set("Done")

root = tk.Tk()
root.title("Comment  Automation Shekel Bot")
label_var = tk.StringVar()


start_job_button = tk.Button(root, text="Start Job", command=start_job)
start_job_button.grid(row=0, column=0, padx=10, pady=5)

job_log = tk.Label(root, text="Working on current comment: ")
job_log.grid(row=0, column=3, padx=5, pady=5)


job_log_progress = tk.Label(root, textvariable=label_var)
job_log_progress.grid(row=0, column=4, padx=5, pady=5)

link_label = tk.Label(root, text="Enter Link:")
link_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

link_entry = tk.Entry(root, width=50)
link_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Enter Email (Upvote.biz):")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

email_entry = tk.Entry(root, width=50)
email_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Enter Password (Upvote.biz):")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

password_entry = tk.Entry(root, width=50, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

browse_button = tk.Button(root, text="Browse Comment File", command=browse_file)
browse_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

comments_label = tk.Label(root, text="Comments:")
comments_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

comments_text = tk.Text(root, width=50, height=10)
comments_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# add_button = tk.Button(root, text="Add Another Interval", command=add_interval_field)
# add_button.grid(row=6, column=0, padx=10, pady=5)

interval_minutes_entries = []
interval_duration_entries = []

for i, default_value in enumerate([(2,10), (3,20), (4,30), (5,150)]):
    label = tk.Label(root, text=f"Comment Interval {i + 1}:")
    label.grid(row=i + 1+6, column=0, padx=10, pady=5)

    label = tk.Label(root, text=f"Make 1 comment every:")
    label.grid(row=i + 1+6, column=1, padx=10, pady=5)

    interval_minutes_entry = tk.Entry(root, width=10)
    interval_minutes_entry.grid(row=i + 1+6, column=2, padx=10, pady=5)
    interval_minutes_entry.insert(tk.END, default_value[0])
    interval_minutes_entries.append(interval_minutes_entry)

    label = tk.Label(root, text=f"minutes for duration of")
    label.grid(row=i + 1+6, column=3, padx=10, pady=5)


    interval_duration_entry = tk.Entry(root, width=10)
    interval_duration_entry.grid(row=i + 1+6, column=4, padx=10, pady=5)
    interval_duration_entry.insert(tk.END, default_value[1])
    interval_duration_entries.append(interval_duration_entry)

    label = tk.Label(root, text=f"minutes.")
    label.grid(row=i + 1+6, column=5, padx=10, pady=5)

root.mainloop()