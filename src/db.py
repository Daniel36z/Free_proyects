import sqlite3 #este viene incluido en python no necesita usar pip 
conexion = sqlite3.connect("basedbiot")#se crea la base de datos y se establece conexión
cursor = conexion.cursor()#cursor para navegar en las db



#creación de una tabla (solo se necesita ejecutar una vez)-------------------------------------
'''
cursor.execute(""" CREATE TABLE usuarios(
               usuario TEXT,
               nombre TEXT,
               password VARCHAR(20)
               )
""") 

'''


#insertar datos en una tabla(recuerde especificar el tipo con comillas si es text)-----------------------
'''
v5 = str('jmanuel2023')
v6 = 'juan manuel'
v7 = 'admin'
cursor.execute(f"INSERT INTO usuarios(usuario,nombre,password) VALUES('{v5}','{v6}','{v7}')" )
print("datos insertados en la tabla")
conexion.commit()
'''


#imprimir en pantalla los datos de la base de datos
"""
datosdb = cursor.execute("SELECT* FROM usuarios")#select* se refiere a todos los datso
for i in datosdb:
    print(i)
"""

#seleccionar datos especificos 
"""
cursor.execute("SELECT* FROM usuarios WHERE edad<'18'") 
print(cursor.fetchall())
"""

#organizar de manera creciente o decreciente---------------------------

#AGrEGAR O QUItar DESC si se quiere de mayor a menor
#sql = """
    #SELECT nombre FROM usuarios ORDER BY edad DESC



#filtrar y ordenar 
#sql2 = """
    #SELECT nombre FROM usuarios WHERE edad>10 ORDER BY edad DESC
   # """  
"""
cursor.execute(sql2)
datos = cursor.fetchall()#esto solo imprime en este orden no afecta el orden de la tabla real
for e in datos:
    print(e)
    """
 





#ACTUALIZAR UPDATE---------------------------
"""
#primero lo que se cambia y luego con lo que se compara
cursor.execute(" UPDATE usuarios SET id = 555 WHERE nombre = 'ignacio' ")
conexion.commit()    
"""        
               
"""
def clave(user,pas):
    cursor.execute(f"SELECT* FROM usuarios WHERE nombre = '{user}' ") 
    v11 = cursor.fetchall()
    if v11 == []:
        print("no esta en la db")
    elif v11[0][0] == user:
        if v11[0][2] == pas:
            print("contraseña corecta")
        else:
            print("contraseña erronea")
    conexion.close()


clave("dan","1002063859")


"""

#-----------------------UPDATE-----------------------------------------------
sql = "UPDATE nametabla SET column='ueva' WHERE column = 'vieja'"
cursor.execute(sql)
conexion.commit()
conexion.close() 



"""
@app.route(/register, methods=['POST'])
def register():
    data = request.data
    objeto_json = literal_eval(data.decode('utf-8'))
    usuario = objeto_json['user']
    password = objeto_json['password']
    cursor.execute(f"INSERT INTO usuarios(nombre,edad) VALUES('{usuario}',{password})" )
    print("datos insertados en la tabla")
    conexion.commit()
    return('')

"""