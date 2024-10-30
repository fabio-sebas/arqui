from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route('/')
def home():
    return redirect(url_for('vista_usuario'))

@app.route('/vista_usuario')
def vista_usuario():
    historial = [
        {'fecha': '2024-10-01', 'tipo': 'Inicio de Sesión', 'detalles': 'Usuario inició sesión'},
        {'fecha': '2024-10-02', 'tipo': 'Consulta', 'detalles': 'Usuario consultó su historial'},
    ]
    return render_template('vista_usuario.html', historial=historial)

if __name__ == '__main__':
    app.run(debug=True)
