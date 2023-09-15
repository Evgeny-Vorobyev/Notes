
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



def list_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
        print()



def edit_note():
    note_id = int(input("Enter the ID of the note you want to edit: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Enter the new title: ")
            new_body = input("Enter the new body: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print("Note successfully updated!")
            return
    print("Note not found.")



def delete_note():
    note_id = int(input("Enter the ID of the note you want to delete: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note successfully deleted!")
            return
    print("Note not found.")



notes = load_notes()
while True:
    print("\nNote Management System")
    print("1. Add a new note")
    print("2. List all notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_note()
    elif choice == '2':
        list_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")




