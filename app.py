from flask import Flask, render_template
from data import pets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/animals/<pet_type>')
def animals(pet_type):
    return render_template("animals.html",pt = pet_type, pets = pets[pet_type])

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    return render_template("pet.html", pet = pets[pet_type][pet_id])

if __name__ == "__main__":
    app.run(debug=True) 