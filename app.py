from flask import Flask, render_template, request, abort, url_for, redirect
app = Flask(__name__)	

import requests
from datetime import datetime, timedelta

apikey="177e1059-674a-463d-89b2-634bdae94782"

#holidays= requests.get("https://holidayapi.com/v1/holidays", params={}, timeout=2.50)
#countries= requests.get("https://holidayapi.com/v1/countries", params={}, timeout=2.50)
#languages= requests.get("https://holidayapi.com/v1/languages", params={}, timeout=2.50)
#workday= requests.get("https://holidayapi.com/v1/workday", params={}, timeout=2.50)
#workdays= requests.get("https://holidayapi.com/v1/workdays", params={}, timeout=2.50)

#print(r.status_code)
#print(r.url)
#print(r.text)
#print(r.json)
#print(r.status_code)

@app.route('/', methods=['GET','POST'])
def index():
    filtrosDiasRestantes = {
    "country": "ES",
    "start": datetime.now() - timedelta(days=365),
    "end": "2022-06-01",
    "key": apikey
    }
    respuesta = requests.post("https://holidayapi.com/v1/workdays", params=filtrosDiasRestantes, timeout=2.50)
    diasrestantes=respuesta.json()
    
    recursos=['Holidays', 'Countries', 'Languages', 'Workday', 'Workdays']
    return render_template('index.html', diasrestantes=diasrestantes, recursos=recursos)

@app.route('/holidays')
def holidays():
    hoy = datetime.now() - timedelta(days=365)
    
    filtrosProximaFiesta = {
    "country": "ES",
    "language": "es",
    "year": hoy.year,
    "month": hoy.month,
    "day": hoy.day,
    "upcoming": "1",
    "key": apikey
    }

    respuesta = requests.post("https://holidayapi.com/v1/holidays", params=filtrosProximaFiesta, timeout=2.50)
    fiestas= respuesta.json()
    
    return render_template('holidays.html', fiestas=fiestas)

@app.route('/countries', methods=['GET','POST'])
def countries():
    if request.method == 'POST':
        busqueda = request.form["pais"]
    
        filtropaises = {
        "search": busqueda,
        "key": apikey,
        }
        respuesta = requests.post("https://holidayapi.com/v1/countries", params=filtropaises)
        paises = respuesta.json()
        listapaises = paises["countries"]
        
        return render_template('countries.html', listapaises=listapaises, busqueda=busqueda)
    return render_template('countrysearch.html')

@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/workdays')
def workdays():
    filtrosDiasRestantes = {
    "country": "ES",
    "start": datetime.now() - timedelta(days=365),
    "end": "2022-12-31",
    "key": apikey
    }
    respuesta = requests.post("https://holidayapi.com/v1/workdays", params=filtrosDiasRestantes, timeout=2.50)
    diasrestantes=respuesta.json()
    
    recursos=['Holidays', 'Countries', 'Languages', 'Workday', 'Workdays']
    return render_template('workdays.html', diasrestantes=diasrestantes, recursos=recursos)



@app.errorhandler(404)
def error404(error):
    return render_template ('404.html'), 404

app.run("0.0.0.0",30000,debug=True)



#codigo sobrante de la primera parte.
'''
#1
filtros1 = {
    "country": "ES",
    "start": "2022-05-14",
    "end": "2022-05-24",
    "key": apikey
}

respuesta1 = requests.post("https://holidayapi.com/v1/workdays", params=filtros1, timeout=2.50)
datos1 = respuesta1.json()

workdays = datos1["workdays"]
print("Número de días laborales:", workdays)
print()

#2
filtros2 = {
    "country": "ES",
    "year": "2022",
    "month": "12",
    "day": "15",
    "upcoming": "1",
    "key": apikey
}

respuesta2 = requests.post("https://holidayapi.com/v1/holidays", params=filtros2, timeout=2.50)
datos2 = respuesta2.json()

req = datos2["status"]
holidays = datos2["holidays"]

if req == 200:
    next_holiday = holidays[0]["name"]
    print("Próxima festividad:", next_holiday)
else:
    print("No se encontraron festividades próximas.")
print()

#3
filtros3 = {
    "search": "spain",
    "key": apikey
}
respuesta3 = requests.post("https://holidayapi.com/v1/countries", params=filtros3)
datos3 = respuesta3.json()

req = datos3["status"]
countries = datos3["countries"]

if req == 200:
    country = countries[0]
    print("Mejor resultado:") #cuando haga la app, bucle pa que muestre mas de 1
    print("Información de", country["name"])
    print("Código de país:", country["codes"].values()) #transformar el tipo de dato
    print("Nombre del país:", country["name"])
#   for i in country["subdivisions"]:
#       provincias     
else:
    print("No se encontró información sobre '", end="")
    print(filtros3, end="'")
'''