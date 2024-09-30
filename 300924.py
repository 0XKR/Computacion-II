from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def mostrar_():
    #leer archivo de texto
    with open('notas.txt','r') as file:
        lineas = file.readlines()
    #procesar las lineas de archivo
    estudiantes=[]
    
    for linea in lineas:
        nombre,nota1, nota2, nota3 = linea.strip().split(',')
        estudiantes.append({'nombre':nombre,'nota1':nota1, 'nota2':nota2,'nota3':nota3})
    #crear una plantilla html simple para mostrar los datos
    plantilla = '''
    <!doctype html>
    <html lang='es'>
        <head>
            <meta charset='utf-8'>
            <title>Notas de estudiantes</title>
        </head>
        <body>
            <h1>Notas de estudiantes</h1>
            <table border = '1'>
                <tr>
                    <th>Nombre</th>
                    <th>Nota1</th>
                    <th>Nota2</th>
                    <th>Nota3</th>
                </tr>
                {%for estudiante in estudiantes %}
                <tr>
                    <td>{{estudiante.nombre}}</td>
                    <td>{{estudiante.nota1}}</td>
                    <td>{{estudiante.nota2}}</td>
                    <td>{{estudiante.nota3}}</td>
                </tr>
                {%endfor%}
            </table>
        </body>
    </html>
    '''
    return render_template_string(plantilla,estudiantes = estudiantes)

if __name__ == '__main__':
    app.run()
