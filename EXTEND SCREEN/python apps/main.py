

import tkinter as tk  
from tkinter import ttk 
valid_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}
def is_valid(username,password ) : 
    if username is is_valid and valid_credentials == password : 
        return  True 
    else : 
        return False 
    def login( ) : 
        username = username_entry.get() 
        password = password_entery.get()

        if is_valid(username, password ) :
            result_label.config(text="login sucses welcome, " + username  )
        else :
               result_label.config(text="incalid password or username "
        window = tk.Tk()
         window.title("password test  Login App")
         window.configure(bg="#5A5252")
         style = ttk.Style()
         style.configure("TFrame", background="#5A5252")
         window.mainloop()

         import sqlite3

conn = sqlite3.connect('mydatabase.db')  


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("john_doe", "secret123"))

conn.commit()
conn.close()


