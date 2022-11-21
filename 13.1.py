from flask import Flask, request
import json

app = Flask(__name__)
@app.route("/alkuluku/<luku1>")
def alkuluku(luku1):

    luku1 =  float(luku1)
    numbers_list = [9, 8, 7, 6, 5, 4, 3, 2]
    is_prime = False

    if luku1 / luku1 == 1 and luku1 / 1 == luku1:
        is_prime = True

    for number in numbers_list:
        if luku1 % number == 0:
            is_prime = False

    if is_prime == True:
        vastaus = {
            "luku1" : luku1,
            "is_prime" : True
        }

        return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)