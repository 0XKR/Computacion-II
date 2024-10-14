from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')

def index():
    plantilla = '''index
<html>  
<head>  
<title>Index</title>  
</head>  
<body>  
    <h2>Tercer Parcial</h2>  
    <a href="/add">Guardar Punto</a><br><br>  
    <a href ="/view">Mostrar respuestas</a><br><br>  
     
</body>  
</html> '''
    return render_template_string(plantilla)

@app.route('/add', methods = ['GET','POST'])

def guardar():
    
    plantilla= '''<!DOCTYPE html>  
<html>  
<head>  
    <title>Anadir registro</title>  
</head>  
<body>  
    <h2>Informacion</h2>   
    <form action = "/save" method="post">  
    <table>  
        <tr><td>x</td><td><input type="text" name="x"></td></tr>  
        <tr><td>y</td><td><input type="text" name="y"></td></tr>  
          
        <tr><td><input type="submit" value="Guardar"></td></tr>  
    </table>  
    </form>  
</body>  
</html> '''
    
    return render_template_string(plantilla)
    
@app.route('/save', methods = ['GET','POST'])
def guardarBD():
    msg = '' 
    if request.method == "POST":  
        try:  
            x = request.form["x"]  
            y = request.form["y"]
            with sqlite3.connect("puntos") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into punto(x,y) values(?,?)",(x,y))  
                con.commit()  
                msg = f"Punto agregado ({x},{y}) correctamente"
                
                con = sqlite3.connect("puntos")  
                con.row_factory = sqlite3.Row  
                cur = con.cursor()  
                cur.execute("select * from punto")  
                rows = cur.fetchall()
                    
                puntos = []
                for row in rows:
                    punto = [0,0]
                    punto[0] = row['x']
                    punto[1] = row['y']
                    puntos.append(punto)
                ordenadas = []
                for i in puntos:
                    ordenada = i[1]
                    ordenadas.append(ordenada)
                    
                cont=0
                for j in ordenadas:
                    if j == int(y):
                        cont +=1
                
                dist_mayor = 0
                for k in puntos:
                    x_act = int(k[0])
                    y_act = int(k[1])
                    x = int(x)
                    y = int(y)
                    dist = ((x_act-x)**2+(y_act-y)**2)**(1/2)
                    
                    if dist > dist_mayor:
                        dist_mayor = dist
                        x1=k[0]
                        y1=k[1]
                    
                    
                    

        except:  
            con.rollback()  
            msg = 'No pudo agregar el punto'
        finally:
            plantilla ='''<!DOCTYPE html>  
<html>  
<head>  
    <title>Guardar punto</title>  
</head>  
<body>  
    <h3>Hola, {{msg}}</h3>
    <a href="/">Inicio</a>
    <br><br>
    
    <h2>{{cont}} puntos tienen la misma ordenada</h2>
    
    La coordenada mas alejada del punto es ({{x1}},{{y1}})

    <br>
</body>  
</html>  '''

            return render_template_string(plantilla,msg=msg,puntos=puntos,cont=cont,x1=x1,y1=y1)
            con.close()
          
@app.route("/view")  
def view():  
    con = sqlite3.connect("puntos")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from punto")  
    rows = cur.fetchall()
    
    puntos = []
    for row in rows:
        punto = [0,0]
        punto[0] = row['x']
        punto[1] = row['y']
        puntos.append(punto)
        
    #primera coordenada en el primer cuadrante
    band = True
    for i in puntos:
        x = i[0]
        y = i[1]
        
        if x >= 0 and y >= 0 and band == True:
            prim_coord = [x,y]
            band = False 
    
    plantilla = '''
    <!DOCTYPE html>  
<html>  
<head>  
    <title>...</title>  
</head>  
<body>  
   
<h1>Respuestas</h1>  
<table border=5>  
    <thead>  
        <td>X</td>   
        <td>Y</td>  
    </thead>  
       
    {% for row in rows %}  
       
        <tr>  
            <td>{{row["x"]}}</td>  
            <td>{{row["y"]}}</td>  
            
        </tr>  
       
    {% endfor %}  
</table>  
<br></br>

<h2>la primera cordenada en el primer cuadrante es ({{prim_coord[0]}},{{prim_coord[1]}})</h2>
   
<a href="/">volver al indice</a>  
   
</body>  
</html>'''
    
    return render_template_string(plantilla,rows = rows,prim_coord = prim_coord)
    
if __name__ == '__main__':
    app.run()
    
    




