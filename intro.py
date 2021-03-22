from pywinauto.application import Application


app = Application().start("notepad.exe")

app.notepad.Edit.type_keys("Someething")