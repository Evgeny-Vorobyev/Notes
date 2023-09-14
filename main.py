
import json
import os
from datetime import datetime
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            notes_data = json.load(file)
        return notes_data
    return []


