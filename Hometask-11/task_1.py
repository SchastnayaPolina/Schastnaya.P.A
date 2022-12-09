import json
from tkinter import*
import requests

root = Tk()

def function_for_do_action():
    with open("C:\\Users\\Alex\\Desktop\\11.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        slovar = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in slovar:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Файл заполнен")


root.title('Введите, пожалуйста, Ваш ГитХаб-Айди')
root.geometry('600x300')
root["bg"] = "black"
head = Label(root, bg = "black", fg = "purple", text = 'ID HERE: ', font = ('SimSun', 22))
head.pack(expand=True)
txtField = Entry(root,width=40,font=('SimSun', 18))
txtField.pack(expand=True)
button = Button(root, bg = "black", fg = "purple", text = 'TAPTAPTAP',command = function_for_do_action)
button.pack(expand=True)
root.mainloop()
