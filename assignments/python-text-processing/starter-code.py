# Starter code for Python Text Processing assignment

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
        return []

def count_lines_and_words(lines):
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

def replace_words(lines, search, replace):
    return [line.replace(search, replace) for line in lines]

if __name__ == "__main__":
    # 1. Leer y mostrar el contenido de input.txt
    lines = read_file('input.txt')
    for line in lines:
        print(line, end='')

    # 2. Contar líneas y palabras
    num_lines, num_words = count_lines_and_words(lines)
    print(f"\nLíneas: {num_lines}, Palabras: {num_words}")

    # 3. Buscar y reemplazar palabras
    search = input("Palabra a buscar: ")
    replace = input("Palabra de reemplazo: ")
    new_lines = replace_words(lines, search, replace)
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Archivo output.txt guardado.")
