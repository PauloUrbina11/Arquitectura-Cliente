import json
import os

# Ruta donde se guardarán las notas
NOTES_FILE = 'notas.json'

# Función para cargar las notas desde el archivo JSON
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

# Función para guardar las notas en el archivo JSON
def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

# Función para mostrar las notas
def list_notes():
    notes = load_notes()
    if not notes:
        print("\nNo hay notas disponibles.")
    else:
        print("\nLista de notas:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")

# Función para añadir una nueva nota
def add_note():
    new_note = input("\nEscribe tu nueva nota: ")
    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    print("Nota añadida correctamente.")

# Función para eliminar una nota
def delete_note():
    list_notes()
    notes = load_notes()
    if notes:
        note_index = int(input("\nIntroduce el número de la nota que deseas eliminar: "))
        if 0 < note_index <= len(notes):
            removed_note = notes.pop(note_index - 1)
            save_notes(notes)
            print(f"Nota '{removed_note}' eliminada correctamente.")
        else:
            print("Índice no válido.")
    else:
        print("No hay notas para eliminar.")

# Función principal con el menú de opciones
def main():
    while True:
        print("\nOpciones:")
        print("1. Ver notas")
        print("2. Añadir nota")
        print("3. Eliminar nota")
        print("4. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            list_notes()
        elif option == '2':
            add_note()
        elif option == '3':
            delete_note()
        elif option == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
