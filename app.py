from flask import Flask, render_template, url_for ,request, make_response
import datetime
fecha = datetime.datetime.now()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cookie/crear_cookies")
def set_cookie():
    resp = make_response(render_template("cookies.html"))
    try:
        resp.set_cookie(["name", "ye"])
    except Exception as e:
        msj = str(e)

    return resp

@app.route("/cookie/ver_mis_cookies")
def read_cookie():
    name = request.cookies.get("name", None)
    mkio = request.cookies.get("mkio", None)
    if name == None:
        return "Version antigua"
    msn = f"{name}+'  '+{mkio}"
    return msn

if __name__ == "__main__":
    app.run(debug=True, port = 2333)
