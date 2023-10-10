from flask import Flask, request, redirect
from ast import literal_eval
import requests
import sqlite3 
import json
from werkzeug.security import generate_password_hash, check_password_hash

urljuan = ("http://192.168.0.197:5000")
app = Flask(__name__)

@app.route('/usuario', methods=['POST'])
def usuario0():
    v3 = request.json["status"]
    print(v3)
    return(v3)



@app.route('/login', methods=['POST'])
def clave():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    user = objeto_json["usuario"]
    pasoriginal = objeto_json["password"]
    conexion = sqlite3.connect("basedbiot")
    cursor = conexion.cursor()
    cursor.execute(f"SELECT* FROM usuarios WHERE usuario = '{user}' ") 
    v11 = cursor.fetchall()
    if v11 == []:
        estado_con=("no esta en la db")
    elif v11[0][0] == user:
        if check_password_hash(v11[0][2],pasoriginal) == True:
            estado_con = redirect("https://www.facebook.com/")
        else:
            estado_con=("contraseña erronea")
    conexion.close()
    return(estado_con)



@app.route('/create', methods=['POST'])
def crear():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    user = objeto_json["usuario"]
    name = objeto_json["nombre"]
    pasoriginal = objeto_json["password"]
    pasencript= generate_password_hash(pasoriginal)
    conexion = sqlite3.connect("basedbiot")
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO usuarios(usuario,nombre,password) VALUES('{user}','{name}','{pasencript}')" )
    conexion.commit()
    conexion.close()
    return("datos insertados con exito")




@app.route('/delete',methods=['POST'])
def borrar():
    conexion = sqlite3.connect("basedbiot")
    cursor = conexion.cursor()
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    user = objeto_json["usuario"]
    cursor.execute(f"SELECT* FROM usuarios WHERE usuario = '{user}' ") 
    v11 = cursor.fetchall()
    if v11 == []:
        estadoc=("no esta en la db")
        pasencript="malo"
    else:
        pasencript = v11[0][2]
    pasoriginal = objeto_json["password"]
    pasencript2= check_password_hash(pasencript,pasoriginal)# esto es True
    if pasencript2 == True:
        estadoc = "datos ok"
        borrado = f"""
            DELETE FROM usuarios WHERE usuario = '{user}' AND password = '{pasencript}'
            """
        cursor.execute(borrado)
        conexion.commit()
    else:
        estadoc = "credenciales no coinciden"

    conexion.close()
    return(estadoc)
    

@app.route('/update', methods = ['POST'])
def actualizar():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    user = objeto_json["usuario"]
    name = objeto_json["nombre"]
    pas = objeto_json["password"]
    newuser = objeto_json["newusuario"]
    newpas = objeto_json["newpassword"]
    newname = objeto_json["newname"]

    conexion = sqlite3.connect("basedbiot")
    cursor = conexion.cursor()
    cursor.execute(f"SELECT* FROM usuarios WHERE usuario = '{user}' ") 
    v11 = cursor.fetchall()
    if v11 == []:
        estadoc=("no esta en la db")
        pasencript="malo"
    else:
        pasencript = v11[0][2]
    pasencript2= check_password_hash(pasencript,pas)# esto es True
    newpasencr = generate_password_hash(newpas)
    
    if pasencript2 == True:
        estadoc = "datos ok"
        actualizado = f"UPDATE usuarios SET usuario='{newuser}' WHERE usuario = '{user}' " 
        actualizado2 = f"UPDATE usuarios SET nombre='{newname}' WHERE nombre = '{name}' " 
        actualizado3 = f"UPDATE usuarios SET password='{newpasencr}' WHERE password = '{pas}' " 
        cursor.execute(actualizado)
        cursor.execute(actualizado2)
        cursor.execute(actualizado3)
        conexion.commit()
    else:
        estadoc = "credenciales no coinciden"
    return(estadoc)





def entrega(urljuan,v1,v2):
    entrega= {"id":v1,"status":v2}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    requests.post(urljuan,  data = json.dumps(entrega),headers= headers)


@app.route('/cambio', methods=['POST'])
def llegada():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    v1 = objeto_json["id"]
    v2 = objeto_json["status"]
    if (objeto_json['id'] == '1'):
        entrega(urljuan+"/light/1",v1,v2)
    elif(objeto_json['id'] == '2'):
        entrega(urljuan+"/light/2",v1,v2)
    elif(objeto_json['id'] == '3'):
        entrega(urljuan+"/light/3",v1,v2)
    elif(objeto_json['id'] == '4'):
        entrega(urljuan+"/door/1",v1,v2)
    elif(objeto_json['id'] == '5'):
        requests.post(urljuan,"qui va la alarma") 
    return("ok")

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    