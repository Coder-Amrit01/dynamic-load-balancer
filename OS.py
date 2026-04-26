import tkinter as tk
import random

cpu_load = {}

# ------------------ TASK GENERATION ------------------
def generate_tasks():
    global cpu_load
#update1
    try:
        num_cpus = int(cpu_entry.get())
        num_tasks = int(task_entry.get())
    except:
        display("Error: Enter valid numbers!", {})
        return

    cpu_load = {i: [] for i in range(num_cpus)}

    tasks = [random.randint(1, 10) for _ in range(num_tasks)]

    for task in tasks:
        cpu = random.randint(0, num_cpus - 1)
        cpu_load[cpu].append(task)

    display("Before Balancing", cpu_load)

# ------------------ LOAD FUNCTION ------------------
def get_load(tasks):
    return sum(tasks)

# ------------------ BALANCING LOGIC (SAFE + FAST) ------------------
def balance_load():
    global cpu_load

    if not cpu_load:
        display("Generate tasks first!", {})
        return

    # Collect all tasks
    all_tasks = []
    for tasks in cpu_load.values():
        all_tasks.extend(tasks)

    # Sort tasks (largest first)
    all_tasks.sort(reverse=True)

    # Reset CPU loads
    new_cpu_load = {i: [] for i in cpu_load}

    # Distribute evenly
    for i, task in enumerate(all_tasks):
        cpu = i % len(new_cpu_load)
        new_cpu_load[cpu].append(task)

    cpu_load = new_cpu_load

    display("After Balancing", cpu_load)

# ------------------ DISPLAY FUNCTION ------------------
def display(title, data):
    output.delete("1.0", tk.END)
    output.insert(tk.END, title + "\n\n")

    for cpu, tasks in data.items():
        output.insert(
            tk.END,
            f"CPU {cpu}: {tasks} | Load = {get_load(tasks)}\n"
        )

# ------------------ UI ------------------
root = tk.Tk()
root.title("Dynamic Load Balancer")

tk.Label(root, text="Number of CPUs").pack()
cpu_entry = tk.Entry(root)
cpu_entry.pack()

tk.Label(root, text="Number of Tasks").pack()
task_entry = tk.Entry(root)
task_entry.pack()

tk.Button(root, text="Generate Tasks", command=generate_tasks).pack(pady=5)
tk.Button(root, text="Balance Load", command=balance_load).pack(pady=5)

output = tk.Text(root, height=15, width=50)
output.pack()

root.mainloop()
