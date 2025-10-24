from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def ajustar_llave(key, lenght):
    key_bytes = key.encode()
    if len(key_bytes) < lenght:
        key_bytes += get_random_bytes(lenght - len(key_bytes))
    elif len(key_bytes) > lenght:
        key_bytes = key_bytes[:lenght]
    return key_bytes


def cifrar(algoritmo, key, iv, texto):
    if algoritmo == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError("algoritmo no soportado")

    cifrado = cipher.encrypt(pad(texto.encode(), block_size))
    return cifrado


def descifrar(algoritmo, key, iv, texto_cifrado):
    if algoritmo == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError("algoritmo no soportado")

    descifrado = unpad(cipher.decrypt(texto_cifrado), block_size)
    return descifrado.decode()


def ejecutar_algoritmo(algoritmo):
    print(f"\n--- {algoritmo} ---")
    texto = input("texto a cifrar: ")

    if algoritmo == "DES":
        key_len = 8
        iv_len = 8
    elif algoritmo == "3DES":
        key_len = 24
        iv_len = 8
    elif algoritmo == "AES":
        key_len = 32
        iv_len = 16

    key_input = input(f"Llave ({key_len} bytes): ")
    key = ajustar_llave(key_input, key_len)
    print(f"→ Llave final ({len(key)} bytes): {key}")

    iv_input = input(f"Vector de inicialización ({iv_len} bytes): ").encode()
    if len(iv_input) != iv_len:
        raise ValueError(f"El IV debe tener {iv_len} bytes.")

    texto_cifrado = cifrar(algoritmo, key, iv_input, texto)
    print(f"Texto cifrado (bytes): {texto_cifrado}")
    print(f"Texto cifrado (hex): {texto_cifrado.hex()}")

    texto_descifrado = descifrar(algoritmo, key, iv_input, texto_cifrado)
    print(f"Texto descifrado: {texto_descifrado}")


# main
if __name__ == "__main__":
    print("Seleccione algoritmo:")
    print("1. DES")
    print("2. AES-256")
    print("3. 3DES")

    opcion = input("Opción: ")

    if opcion == "1":
        ejecutar_algoritmo("DES")
    elif opcion == "2":
        ejecutar_algoritmo("AES")
    elif opcion == "3":
        ejecutar_algoritmo("3DES")
    else:
        print("opción no válida.")
