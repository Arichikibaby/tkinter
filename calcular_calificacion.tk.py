import tkinter as tk
from tkinter import messagebox, simpledialog

# Diccionario para almacenar alumnos
alumnos = {}

# Función para calcular la calificación
def calcular_calificacion(nota):
    if nota < 5:
        return "SS"
    elif 5 <= nota < 7:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    elif nota >= 9:
        return "SB"

# Funciones de gestión
def mostrar_alumnos():
    if not alumnos:
        messagebox.showinfo("Lista de Alumnos", "No hay alumnos registrados.")
        return
    resultado = "DNI | Apellidos, Nombre | Nota | Calificación\n"
    for dni, datos in alumnos.items():
        resultado += f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}\n"
    messagebox.showinfo("Lista de Alumnos", resultado)

def introducir_alumno():
    dni = simpledialog.askstring("Introducir Alumno", "DNI:")
    if not dni or dni in alumnos:
        messagebox.showerror("Error", "DNI inválido o ya registrado.")
        return
    apellidos = simpledialog.askstring("Introducir Alumno", "Apellidos:")
    nombre = simpledialog.askstring("Introducir Alumno", "Nombre:")
    try:
        nota = float(simpledialog.askstring("Introducir Alumno", "Nota:"))
        if not (0 <= nota <= 10):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Nota inválida. Introduzca un número entre 0 y 10.")
        return
    calificacion = calcular_calificacion(nota)
    alumnos[dni] = {"apellidos": apellidos, "nombre": nombre, "nota": nota, "calificacion": calificacion}
    messagebox.showinfo("Éxito", "Alumno introducido correctamente.")

def eliminar_alumno():
    dni = simpledialog.askstring("Eliminar Alumno", "DNI del alumno a eliminar:")
    if dni in alumnos:
        del alumnos[dni]
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
    else:
        messagebox.showerror("Error", "DNI no encontrado.")

def consultar_alumno():
    dni = simpledialog.askstring("Consultar Alumno", "DNI del alumno:")
    if dni in alumnos:
        datos = alumnos[dni]
        resultado = f"DNI: {dni}\nApellidos: {datos['apellidos']}\nNombre: {datos['nombre']}\nNota: {datos['nota']}\nCalificación: {datos['calificacion']}"
        messagebox.showinfo("Información del Alumno", resultado)
    else:
        messagebox.showerror("Error", "DNI no encontrado.")

def modificar_nota():
    dni = simpledialog.askstring("Modificar Nota", "DNI del alumno:")
    if dni in alumnos:
        try:
            nueva_nota = float(simpledialog.askstring("Modificar Nota", "Nueva nota:"))
            if not (0 <= nueva_nota <= 10):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Nota inválida. Introduzca un número entre 0 y 10.")
            return
        alumnos[dni]["nota"] = nueva_nota
        alumnos[dni]["calificacion"] = calcular_calificacion(nueva_nota)
        messagebox.showinfo("Éxito", "Nota modificada correctamente.")
    else:
        messagebox.showerror("Error", "DNI no encontrado.")

def mostrar_suspensos():
    suspensos = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
                 for dni, datos in alumnos.items() if datos["nota"] < 5]
    if suspensos:
        messagebox.showinfo("Alumnos Suspensos", "\n".join(suspensos))
    else:
        messagebox.showinfo("Alumnos Suspensos", "No hay alumnos suspensos.")

def mostrar_aprobados():
    aprobados = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
                 for dni, datos in alumnos.items() if datos["nota"] >= 5]
    if aprobados:
        messagebox.showinfo("Alumnos Aprobados", "\n".join(aprobados))
    else:
        messagebox.showinfo("Alumnos Aprobados", "No hay alumnos aprobados.")

def mostrar_mh():
    mh = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
          for dni, datos in alumnos.items() if datos["nota"] == 10]
    if mh:
        messagebox.showinfo("Candidatos a MH", "\n".join(mh))
    else:
        messagebox.showinfo("Candidatos a MH", "No hay candidatos a matrícula de honor.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Calificaciones de Alumnos")
root.geometry("400x300")

menu = tk.Menu(root)
root.config(menu=menu)

# Menú de opciones
menu_alumnos = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Gestión de Alumnos", menu=menu_alumnos)
menu_alumnos.add_command(label="Mostrar Alumnos", command=mostrar_alumnos)
menu_alumnos.add_command(label="Introducir Alumno", command=introducir_alumno)
menu_alumnos.add_command(label="Eliminar Alumno", command=eliminar_alumno)
menu_alumnos.add_command(label="Consultar Alumno", command=consultar_alumno)
menu_alumnos.add_command(label="Modificar Nota", command=modificar_nota)
menu_alumnos.add_command(label="Mostrar Suspensos", command=mostrar_suspensos)
menu_alumnos.add_command(label="Mostrar Aprobados", command=mostrar_aprobados)
menu_alumnos.add_command(label="Candidatos a MH", command=mostrar_mh)

# Iniciar la aplicación
root.mainloop()
