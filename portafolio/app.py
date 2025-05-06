from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/Crear_informacion/", methods=["POST"])
def Agregar_informacion():
    if request.method == "POST":
        empresa = request.form["empresa"]
        nombre_puesto = request.form["nombre_puesto"]
        fecha = request.form["fecha"]
        mes = request.form["mes"]
        anio = request.form["anio"]
        conocimientos = request.form["conocimientos"]
        experiencia_laboral = request.form["experiencia_laboral"]
        universidad = request.form["universidad"]
        colegio = request.form["colegio"]

        if not all([empresa, nombre_puesto, fecha, mes, anio, conocimientos, experiencia_laboral, universidad, colegio]):
            print("Falta información")
            return redirect(url_for("Agregar_informacion"))

        return "Datos recibidos correctamente"

if __name__ == '__main__':
    app.run(debug=True)
