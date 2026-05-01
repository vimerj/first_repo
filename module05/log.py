import os
from pathlib import Path

LOGS_PATH = Path(__file__).parent / 'file.txt'

print(f'Logs will be saved to: {LOGS_PATH}')

with open(LOGS_PATH, 'w') as f:
    f.write('This is a log file.\n')