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

# Actualización función list_notes
def list_notes():
    notes = load_notes()
    if not notes:
        print("\nNo hay notas disponibles. ¡Empieza a añadir las tuyas!")
    else:
        print("\n--- Lista de Notas ---")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")
        print("---------------------")


# Actualiza la función add_note
def add_note():
    new_note = input("\nEscribe tu nueva nota: ").strip()
    if not new_note:
        print("La nota no puede estar vacía. Inténtalo de nuevo.")
        return
    confirm = input(f"¿Deseas guardar esta nota? (S/N): {new_note} ").lower()
    if confirm == 's':
        notes = load_notes()
        notes.append(new_note)
        save_notes(notes)
        print("Nota añadida correctamente.")
    else:
        print("La nota no fue guardada.")


# Actualiza la función delete_note
def delete_note():
    list_notes()
    notes = load_notes()
    if notes:
        try:
            note_index = int(input("\nIntroduce el número de la nota que deseas eliminar: "))
            if 0 < note_index <= len(notes):
                confirm = input(f"¿Estás seguro de eliminar la nota '{notes[note_index - 1]}'? (S/N): ").lower()
                if confirm == 's':
                    removed_note = notes.pop(note_index - 1)
                    save_notes(notes)
                    print(f"Nota '{removed_note}' eliminada correctamente.")
                else:
                    print("La nota no fue eliminada.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, introduce un número válido.")
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
