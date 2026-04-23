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

log_lines = [
    "INFO: User logged in",
    "ERROR: Failed to load resource",
    "WARNING: Low disk space",
    "CRITICAL: System crash detected",
    "ERROR: Database connection lost"
]

for line in log_lines:
    if "CRITICAL" in line:
        print("Shutting down server")
        break


sites = [
    {"name": "Google", "status": "active"},
    {"name": "Facebook", "status": "inactive"},
    {"name": "Twitter", "status": "active"},
]

for site in sites:
    if site["status"] == "inactive":
        print(f"{site['name']} is currently inactive.")