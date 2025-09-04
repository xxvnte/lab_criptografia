import sys

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py \"texto a cifrar\" desplazamiento")
        sys.exit(1)
    texto = sys.argv[1]
    desplazamiento = int(sys.argv[2])
    print(cifrar_cesar(texto, desplazamiento))
    
    