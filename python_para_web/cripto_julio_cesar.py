import requests
import json
import hashlib

url_get = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=2dc6d8435e4c6c8c9cb920a74b87c62a15d5b8d0"
url_post = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2dc6d8435e4c6c8c9cb920a74b87c62a15d5b8d0"

r = requests.get(url_get)
r.status_code

js = dt = r.json()

with open("answer.json", "w") as write_file:
    json.dump(js, write_file)

n = dt['numero_casas']
TextoCifrado = dt['cifrado']
TextoDecifrado = ""

for letra in TextoCifrado:
    pos = ord(letra)
    if 97 <= pos <= 122:
        newpos = (pos-97-n)%26+97
    else:
        newpos = pos
    TextoDecifrado += chr(newpos)

hash_texto_decifrado = hashlib.sha1(TextoDecifrado.encode())

dt['resumo_criptografico'] = hash_texto_decifrado.hexdigest()
dt['decifrado'] = TextoDecifrado

with open("answer.json", "w") as write_file:
    json.dump(dt, write_file)

headers = {'Content-Type': "multipart/form-data" }
files = {"answer": open("answer.json", "rb")}
response = requests.post(url=url_post, files=files)
print(response.status_code)
print(response.json())
