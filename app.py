from flask import Flask, request, json, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def handle_form():
        return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    surname = request.form.get('surname')
    age = request.form.get('age')
    return render_template('result.html', name=name, surname=surname, age=age)

@app.route('/api') 
def yesorno():
    response = requests.get('https://yesno.wtf/api') 
    data = response.json()
    fact = data['answer']

    if fact == 'yes':
        return '<h1 style="background-color:green; color:white; text-align:center; padding:50px;">YES</h1>'
    else:
        return '<h1 style="background-color:red; color:white; text-align:center; padding:50px;">NO</h1>'



@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET'

@app.route('/batman')
def batman():
    return '<b>Because Im <span style="color: red">Batman!</span><b>'

@app.route('/pingwin')
def pingwin():
    return '<h1>Pingwiny</h1><img src=https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Penguins_Edinburgh_Zoo_2004_SMC.jpg/320px-Penguins_Edinburgh_Zoo_2004_SMC.jpg></img>'

@app.route('/modulo/<liczba>')
def modulo(liczba):
    if int(liczba)%2==0 and int(liczba)%3==0 and int(liczba)%5==0:
        return 'Liczba <b>jest podzielna</b> przez 2, 3 i 5'
    elif int(liczba)%2==0 or int(liczba)%3==0 or int(liczba)%5==0:
        if int(liczba)%2==0:
            if int(liczba)%2==0 and int(liczba)%3==0:
                return 'Liczba <b>jest podzielna</b> przez 2 i 3'
            elif int(liczba)%2==0 and int(liczba)%5==0:
                return 'Liczba <b>jest podzielna</b> przez 2 i 5'
            else:
                return 'Liczba <b>jest podzielna</b> przez 2'
        elif int(liczba)%3==0:
            if int(liczba)%2==0 and int(liczba)%3==0:
                return 'Liczba <b>jest podzielna</b> przez 2 i 3'
            elif int(liczba)%3==0 and int(liczba)%5==0:
                return 'Liczba <b>jest podzielna</b> przez 3 i 5'
            else:
                return 'Liczba <b>jest podzielna</b> przez 3'
        elif int(liczba)%5==0:
            if int(liczba)%2==0 and int(liczba)%5==0:
                return 'Liczba <b>jest podzielna</b> przez 2 i 5'
            elif int(liczba)%3==0 and int(liczba)%5==0:
                return 'Liczba <b>jest podzielna</b> przez 3 i 5'
            else:
                return 'Liczba <b>jest podzielna</b> przez 5'
    else:
        return 'Liczba <b>nie jest podzielna</b> przez 2, 3 albo 5'
    
@app.route('/about/<name>')
def about(name):
    return render_template('about.html', name = name)