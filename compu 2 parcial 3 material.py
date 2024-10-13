from flask import *
import sqlite3  

app = Flask(__name__)

@app.route('/')
def index():
    plantilla = '''

index
<html>  
<head>  
<title>Index</title>  
</head>  
<body>  
    <h2>Hi, welcome to the website</h2>  
    <a href="/add">anadir</a><br><br>  
    <a href ="/view">mostrar</a><br><br>  
    <a href="/delete">Borrar</a><br><br>  
</body>  
</html> 
    '''
    return render_template_string(plantilla)

@app.route('/add', methods = ['GET','POST'])
def guardar():
    plantilla= '''
    add.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>Anadir registro</title>  
</head>  
<body>  
    <h2>Informacion</h2>   
    <form action = "/save" method="post">  
    <table>  
        <tr><td>Nombre</td><td><input type="text" name="name"></td></tr>  
        <tr><td>Correo</td><td><input type="email" name="email"></td></tr>  
        <tr><td>Direccion</td><td><input type="text" name="address"></td></tr>  
        <tr><td><input type="submit" value="Guardar"></td></tr>  
    </table>  
    </form>  
</body>  
</html> 

    '''
    return render_template_string(plantilla)

@app.route('/save', methods = ['GET','POST'])
def guardar_datos():
    msg = '' 
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into employees (name, email, address) values (?,?,?)",(name,email,address))  
                con.commit()  
                msg = "successfully Added"  
        except:  
            con.rollback()  
            msg = "No puedes agregar"  
        finally:  
            plantilla = '''<!DOCTYPE html>  
<html>  
<head>  
    <title>save details</title>  
</head>  
<body>  
    <h3>Hi Admin, {{msg}}</h3>  
    <a href="/view">ver tabla</a>  
</body>  
</html>  '''

            return render_template_string(plantilla,msg=msg)
            
            con.close()  

@app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from employees")  
    rows = cur.fetchall()  
    plantilla = '''
    <!DOCTYPE html>  
<html>  
<head>  
    <title>List</title>  
</head>  
<body>  
   
<h3>Informacion</h3>  
<table border=5>  
    <thead>  
        <td>ID</td>  
        <td>Name</td>  
        <td>Email</td>  
        <td>Address</td>  
    </thead>  
       
    {% for row in rows %}  
       
        <tr>  
            <td>{{row["id"]}}</td>  
            <td>{{row["name"]}}</td>  
            <td>{{row["email"]}}</td>  
            <td>{{row["address"]}}</td>  
        </tr>  
       
    {% endfor %}  
</table>  
<br></br>  
   
<a href="/">volver al indice</a>  
   
</body>  
</html>
        '''
    return render_template_string(plantilla,rows = rows)


@app.route("/delete")  
def delete():  
    plantilla = '''<!DOCTYPE html>  
<html>  
<head>  
    <title>borrar registro</title>  
</head>  
<body>  
   
    <h3>remover registro de la lista</h3>  
   
<form action="/deleterecord" method="post">  
Employee Id <input type="text" name="id">  
<input type="submit" value="guardar">  
</form>  
</body>  
</html>  '''
    return render_template_string(plantilla)
    
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "registro agregado"  
        except:  
            msg = "no se pudo borrar"  
        finally:  
            plantilla = '''<!DOCTYPE html>  
<html>  
<head>  
    <title>delete record</title>  
</head>  
<body>  
<h3>{{msg}}</h3>  
<a href="/view">ver lista</a>  
</body>  
</html>'''
            
            return render_template_string(plantilla,msg = msg)  

if __name__ == '__main__':
    app.run()