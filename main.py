import json
from datetime import datetime

note = {}

def createNote():
    name = input("Введите название: ")
    text = input('Введите описание: ')
    date = str(datetime.today())
    return {"name":name,"text":text,"date":date}

def saveNote(userNote):
    notes = dict()
    with open("Notes.json","r",encoding='utf-8') as file:
        try:
            notes = json.load(file)
        except:
            print("Ошибка чтения файла")
    with open("Notes.json","w",encoding="utf-8") as file:
        idList = [*notes.keys()]
        id = ""
        if len(idList) > 0:
            id = max(map(lambda x: int(x),idList)) +1
        else:
            id = 0
        notes[f"{id}"] = userNote
        json.dump(notes,file,ensure_ascii=False,indent=2)
def printNotes():
    with open("Notes.json","r",encoding="utf-8") as file:
        notes = json.load(file)
        for key,values in notes.items():
            print(f'ID заметки: {key}\nНазвание заметки: {values["name"]}\nТекст заметки: {values["text"]}')
def editNote():
    with open("Notes.json",encoding="utf-8") as file:
        try:
            notes = json.load(file)
        except:
            print("Ошибка чтения файла")
    key = input("Введите ID заметки: ")
    if key in notes and key.isdigit():
        name = input("Новое имя заметки: ")
        text = input("Новое описание заметки: ")
        date = str(datetime.today())
        notes[key] = {"name":name,"text":text,"date":date}
    with open("Notes.json","w",encoding="utf-8") as file:
        json.dump(notes,file,ensure_ascii=False,indent=2)

def deleteNote():
    with open("Notes.json",encoding="utf-8") as file:
        try:
            notes = json.load(file)
        except:
            print("Ошибка чтения файла")
    key = input("Введите ID заметки: ")
    if key in notes and key.isdigit():
        notes.pop(key)
        with open("Notes.json","w",encoding='utf-8') as file:
            json.dump(notes,file,ensure_ascii=False,indent=2)
        print("Заметка удалена")


run = True
while run:
    print("Меню (введите пункт меню)")
    print("1. Создать заметку")
    print("2. Сохранить заметку")
    print("3. Показать список заметок")
    print("4. Изменить заметку")
    print("5. Удалить заметку")
    print("6. Закрыть приложение")
    command = input('Введите команду: ')
    if command == "1":
        note = createNote()
        print(note)
        input('Нажмите Enter для продолжения...')
    elif command == "2":
        saveNote(note)
        input('Заметка сохранена!\nНажмите Enter для продолжения...')
    elif command == "3":
        printNotes()
        input("\nНажмите Enter для продолжения...")
    elif command == "4":
        editNote()
        input("Нажмите Enter для продолжения...")
    elif command == "5":
        deleteNote()
        input("Нажмите Enter для продолжения...")
    elif command == "6":
        run = False
    else:
        print("Введите правильную команду")