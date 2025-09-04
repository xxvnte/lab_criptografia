from scapy.all import rdpcap, ICMP
from colorama import Fore, Style, init
import sys

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - base - desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def es_probable(texto):
    palabras = ["criptografia", "seguridad", "redes", "mensaje", "claro"]
    return any(palabra in texto.lower() for palabra in palabras)

def extraer_mensaje(pcap_file):
    paquetes = rdpcap(pcap_file)
    chars = []
    for pkt in paquetes:
        if ICMP in pkt and pkt.haslayer('Raw'):
            data = pkt['Raw'].load
            try:
                chars.append(data[:1].decode())
            except:
                continue
    return "".join(chars)

def eliminar_duplicados(texto):
    resultado = ""
    anterior = ""
    for char in texto:
        if char != anterior:
            resultado += char
        anterior = char
    return resultado

if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) != 2:
        print("Uso: python readv2.py archivo.pcapng")
        sys.exit(1)
    archivo = sys.argv[1]
    mensaje = extraer_mensaje(archivo)
    mensaje = eliminar_duplicados(mensaje)
    print("Posibles combinaciones:")
    for desplazamiento in range(1, 26):
        texto = descifrar_cesar(mensaje, desplazamiento)
        if es_probable(texto):
            print(Fore.GREEN + f"{desplazamiento}: {texto}" + Style.RESET_ALL)
        else:
            print(f"{desplazamiento}: {texto}")