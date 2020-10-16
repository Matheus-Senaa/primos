import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

limite = 100

cont = 1
m = 1
numero = 3

primos = "2, "

while m < limite:
	ehprimo = 1
	for a in range(2, numero):
		if numero % a == 0:
			ehprimo = 0
			break
	if(ehprimo):
		primos = primos + str(numero) + ","
		m += 1
		if (m % 10 == 0):
			primos = primos + "<br>"
	numero += 1

return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
