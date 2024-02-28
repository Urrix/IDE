import tkinter as tk
from tkinter import Menu, Text, StringVar

def abrir():
    print("Abrir")

def guardar():
    print("Guardar")

def guardar_como():
    print("Guardar como")

def cerrar():
    print("Cerrar")

def compilar():
    print("Compilar")

def ayuda():
    print("Ayuda")

def on_format_option_selected(option):
    global format_text
    if option == "Lexico":
        format_text.set("Análisis Léxico")
    elif option == "Sintactico":
        format_text.set("Análisis Sintáctico")
    elif option == "Semantico":
        format_text.set("Análisis Semántico")
    elif option == "Codigo intermedio":
        format_text.set("Generación de Código Intermedio")

def on_result_option_selected(option):
    global result_text
    if option == "Errores":
        result_text.set("Mostrar Errores")
    elif option == "Resultados":
        result_text.set("Mostrar Resultados")

root = tk.Tk()
root.title("Compilador")

menu_bar = Menu(root)

# Menú Archivo
archivo_menu = Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Abrir", command=abrir)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_command(label="Guardar como", command=guardar_como)
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar", command=cerrar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

# Menú Compilar
menu_bar.add_command(label="Compilar", command=compilar)

# Menú Ayuda
menu_bar.add_command(label="Ayuda", command=ayuda)

root.config(menu=menu_bar)

# Lienzo 1: Ingreso de texto
lienzo1 = tk.Frame(root)
lienzo1.pack(side=tk.LEFT, padx=10, pady=10)

text1 = Text(lienzo1, height=10, width=50)
text1.pack()

# Lienzo 2: Muestra de formato
lienzo2 = tk.Frame(root)
lienzo2.pack(side=tk.LEFT, padx=10, pady=10)

menu_bar_lienzo2 = Menu(lienzo2)
menu_bar_lienzo2.add_command(label="Lexico", command=lambda: on_format_option_selected("Lexico"))
menu_bar_lienzo2.add_command(label="Sintactico", command=lambda: on_format_option_selected("Sintactico"))
menu_bar_lienzo2.add_command(label="Semantico", command=lambda: on_format_option_selected("Semantico"))
menu_bar_lienzo2.add_command(label="Codigo intermedio", command=lambda: on_format_option_selected("Codigo intermedio"))
lienzo2.config(menu=menu_bar_lienzo2)

format_text = StringVar()
format_text.set("Seleccione una opción de formato.")
text2 = Text(lienzo2, height=10, width=50)
text2.pack()
text2.insert(tk.END, format_text.get())

# Lienzo 3: Resultados o errores de ejecución
lienzo3 = tk.Frame(root)
lienzo3.pack(side=tk.LEFT, padx=10, pady=10)

menu_bar_lienzo3 = Menu(lienzo3)
menu_bar_lienzo3.add_command(label="Errores", command=lambda: on_result_option_selected("Errores"))
menu_bar_lienzo3.add_command(label="Resultados", command=lambda: on_result_option_selected("Resultados"))
lienzo3.config(menu=menu_bar_lienzo3)

result_text = StringVar()
result_text.set("Seleccione una opción de resultados.")
text3 = Text(lienzo3, height=10, width=50)
text3.pack()
text3.insert(tk.END, result_text.get())

root.mainloop()