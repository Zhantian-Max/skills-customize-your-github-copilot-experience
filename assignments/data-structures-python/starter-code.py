# Starter code for Data Structures in Python assignment

def list_operations():
    numbers = [5, 2, 9, 1, 7]
    print("Lista inicial:", numbers)
    # Agregar un número
    numbers.append(4)
    print("Después de agregar 4:", numbers)
    # Eliminar un número
    numbers.remove(2)
    print("Después de eliminar 2:", numbers)
    # Ordenar la lista
    numbers.sort()
    print("Lista ordenada:", numbers)
    # Buscar un número
    n = int(input("¿Qué número quieres buscar en la lista?: "))
    if n in numbers:
        print(f"{n} está en la lista.")
    else:
        print(f"{n} no está en la lista.")

def word_count():
    phrase = input("Introduce una frase: ")
    words = phrase.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print("Frecuencia de palabras:", freq)
    return freq

def sets_and_tuples(freq):
    words = list(freq.keys()) + list(freq.keys())  # Duplicados a propósito
    unique_words = set(words)
    print("Palabras únicas:", unique_words)
    tuples_list = [(word, freq[word]) for word in freq]
    print("Lista de tuplas (palabra, frecuencia):", tuples_list)

if __name__ == "__main__":
    list_operations()
    freq = word_count()
    sets_and_tuples(freq)
