import sqlite3 as sql

def creatDB():
    conn=sql.connect('streamers.db')
    conn.commit()
    conn.close()

def creatTbale():
    conn = sql.connect("streamers.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
        name text,
        followers integer,
        subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre,follower,subs):
    conn=sql.connect("streamers.db")
    cursor = conn.cursor()
    intruccion=f"INSERT INTO streamers VALUES ('{nombre}',{follower},{subs})"
    cursor.execute(intruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devulve todo los datos seleccionados
    conn.commit()
    conn.close()
    print(datos)

def inserRows(streamerList):
    conn=sql.connect("streamers.db")
    cursor = conn.cursor()
    intruccion=f"INSERT INTO streamers VALUES (?,?,?)"#vamos a pasar tres valores para cada fila
    cursor.executemany(intruccion,streamerList) #executemany (para cuadno hacemos para inserciones)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devulve todo los datos seleccionados
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE  name like'Alex%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devulve todo los datos seleccionados
    conn.commit()
    conn.close()
    print(datos)

def updateFields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=12000000 WHERE name like 'elxokas'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRow():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE from streamers WHERE name ='Auronplay'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

   


if __name__  == "__main__":
   
    


    #creatDB()
    #creatTbale()
    #insertRow("ibai",7000000000,250000)
    #insertRow("AlexElcapo",800000,100000)
    #readRows()
    streamers = [
        ("Elxokas",1000000,9500),
        ("crisitnini",3000000,5500),
        ("Auronplay",8000000,20000)
    ]
    #inserRows(streamers)
    #readOrdered("subs")
    #search()
    #updateFields()
    deleteRow()