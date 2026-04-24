import json
import os
import sys

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|remove] ...")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "add" and len(sys.argv) > 2:
        task_text = " ".join(sys.argv[2:])
        tasks.append({"id": len(tasks)+1, "task": task_text, "done": False})
        save_tasks(tasks)
        print(f"✅ Task added: {task_text}")
    
    elif cmd == "list":
        if not tasks:
            print("No tasks yet!")
            return
        for t in tasks:
            status = "✅" if t["done"] else "⬜"
            print(f"{t['id']}. {status} {t['task']}")
    
    elif cmd == "remove" and len(sys.argv) > 2:
        try:
            task_id = int(sys.argv[2])
            tasks = [t for t in tasks if t["id"] != task_id]
            save_tasks(tasks)
            print(f"🗑️ Task {task_id} removed!")
        except:
            print("Please enter a valid task number")

if __name__ == "__main__":
    main()
