all_files = ["main.py", "utils.py", "config.yaml", "README.md", "requirements.txt"]
python_files = []
for file in all_files:
    if file.endswith('.py'):
        python_files.append(file)
print(python_files)

history = ["Tue", "Wed", "Wed", "Thu", "Thu", "Fri", "Sat", "Sun"]
visits = {}
for entry in history:
    if entry not in visits:
        visits[entry] = 0
    visits[entry] += 1
    print(visits)