
import json
import os
from datetime import datetime
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            notes_data = json.load(file)
        return notes_data
    return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def create_note():
    title = input("Enter the title of the note: ")
    body = input("Enter the body of the note: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Note successfully saved!")
