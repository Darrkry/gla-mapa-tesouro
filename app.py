from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de ilhas permitidas
ISLANDS = [
    "Lost Islant", "Gunkan Island", "Whisky Peak", "Little Garden", "Jaya Island",
    "G-7 Marine Base", "Drum Island", "Nanimonai Island", "Nige Hashiru Island",
    "Alabasta Weast", "Alabasta East"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_island = request.form.get("island")
        if not selected_island:
            return redirect(url_for("index"))
        return redirect(url_for("upload", island=selected_island))
    return render_template("index.html", islands=ISLANDS)

@app.route("/upload/<island>", methods=["GET", "POST"])
def upload(island):
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            # salvar ou processar a imagem aqui depois
            return f"Imagem recebida para a ilha {island}!"
    return render_template("upload.html", island=island)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
