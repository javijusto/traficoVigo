import json
import re
import time
import requests

#Autor: Javier Justo

url = 'https://datos.vigo.org/data/trafico/treal_congestion.json'

historico = open('datos.json', 'a')
historico.write("[")

iteraciones = 2

for i in range(iteraciones):
    for j in range(6):
        myfileJson = requests.get(url)
        decode =json.loads(myfileJson.text)
        ttotal = 0
        for tramo in decode:
            t= tramo["tiempo"]
            cadena = re.split(r'\W+', t) 
            min=int(cadena[0])
            seg=int(cadena[2])
            tiempo = (min * 60) + seg
            ttotal = ttotal + tiempo
            if j==0: tfinal=ttotal
            act = tramo["actualizacion"]
        if tfinal!=ttotal:break
        else: time.sleep(10)

    print(act + ": " +  str(tfinal) + "s")

    fila="{" + "'actualizacion': " + "'"+act+"'" + ", 'tiempo': " + "'"+str(ttotal)+"'" + "}"
    code = json.dumps(fila)
    print(str(i) + ": " + code)
    historico.write(code)
    if(i<iteraciones-1): historico.write(", ")
    ttotal = 0
    time.sleep(200)
    

historico.write("]")
historico.close
