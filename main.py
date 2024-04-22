import tkinter as tk
from tkinter import ttk
import sv_ttk
import string
import random
import pyperclip


def update_parameters(event=None):
    # Поле для отображения текста "description_text"
    description_text_slider = tk.StringVar()
    # Используем аргумент ф-ции который на деле
    # нужен как привязка события length_slider.bind("<ButtonRelease-1>", update_parameters)
    if event is None:
        pass
    """ 
    Ф-ция update_parameters обновляет параметры сложности и длины пароля по слайдеру 
    * пользователь может указать сложность пароля и его длину 
    * длина пароля зависит от сложности пароля
    """
    password_length = length_slider.get()
    if int(password_length) <= 14:
        simple_indicator.config(bg="red")
        normal_indicator.config(bg="black", fg="white")
        hard_indicator.config(bg="black", fg="white")
        description_text_slider.set("Простой пароль содержит менее 15 символов.")

    elif 15 <= int(password_length) <= 20:
        simple_indicator.config(bg="black")
        normal_indicator.config(bg="yellow", fg="black")
        hard_indicator.config(bg="black", fg="white")
        description_text_slider.set("Нормальный пароль содержит 15-20 символов.")

    else:
        simple_indicator.config(bg="black", fg="white")
        normal_indicator.config(bg="black", fg="white")
        hard_indicator.config(bg="lightgreen", fg="black")
        description_text_slider.set("Сложный пароль содержит более 20 символов.")

    # Поле для отображения текста "description_text"
    description_label_slider = tk.Label(root, textvariable=description_text_slider)
    description_label_slider.grid(row=2, column=0, columnspan=3, padx=10, pady=5)


def generate_password():
    """
    Ф-ция generate_password генерирует пароль и выводит его в текстовом поле.
    """
    password_length = length_slider.get()
    """ * пароль состоит из больших и маленьких букв + цифры"""
    characters = string.ascii_letters + string.digits
    """ * в сложном пароле добавляються спецсимволы"""
    if hard_indicator.cget("bg") == 'lightgreen':
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(int(password_length)))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def copy_password():
    """
    Ф-ция copy_password копирует сгенерированный пароль из текстового поля в буфер обмена.
    """
    password = password_entry.get()
    pyperclip.copy(password)


def reset_form():
    """
    Ф-ция reset_form сбрасывает форму выбора параметров пароля и очищает текстовое поле.
    """
    length_slider.set(15)
    update_parameters()
    password_entry.delete(0, tk.END)


def disable_window_resize():
    """
    Функция блокирует возможность изменения размера окна программы вручную.
    """
    root.resizable(False, False)


# Создание окна программы
root = tk.Tk()
root.title("Генератор паролей")
sv_ttk.set_theme("dark")

# Блокировка изменения размера окна
disable_window_resize()

# Графическое отображение выбора сложности пароля

# Поле для отображения текста "description_text"
description_text = tk.StringVar()
description_label = tk.Label(root, textvariable=description_text)
description_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
description_text.set("Простой пароль содержит менее 15 символов.")

complexity_label = tk.Label(root, text="Перетащите ползунок для выбора сложности пароля:")
complexity_label.grid(row=0, columnspan=3, padx=30, pady=10)

simple_indicator = tk.Label(root, text="Простой", bg="red", width=10)
simple_indicator.grid(row=1, column=0, padx=10, pady=5)

normal_indicator = tk.Label(root, text="Нормальный", bg="black", width=10)
normal_indicator.grid(row=1, column=1, padx=10, pady=5)

hard_indicator = tk.Label(root, text="Сложный", bg="black", width=10)
hard_indicator.grid(row=1, column=2, padx=10, pady=5)


# Слайдер длины пароля
length_slider = ttk.Scale(root, from_=12, to=24, orient=tk.HORIZONTAL, length=400)
length_slider.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
length_slider.bind("<ButtonRelease-1>", update_parameters)

# Поле для отображения сгенерированного пароля
password_entry = ttk.Entry(root, font=("Helvetica", 12))
password_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=20, sticky="ew")

# Кнопка генерации пароля
generate_button = ttk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=4, column=0, padx=10, pady=5)

# Кнопка копирования пароля
copy_button = ttk.Button(root, text="Копировать пароль", command=copy_password)
copy_button.grid(row=4, column=1, padx=10, pady=5)

# Кнопка сброса формы
reset_button = ttk.Button(root, text="Сбросить пароль", command=reset_form)
reset_button.grid(row=4, column=2, padx=10, pady=5)

# Метод mainloop() обеспечивает постоянную работу главного окна и его объектов до момента, когда оно будет закрыто.
root.mainloop()
