import os
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import rdc_model


root_folder = os.path.abspath(os.path.dirname(__file__))
print(root_folder)
UPLOAD_FOLDER_temp = os.path.join(root_folder, "static")
UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER_temp,"uploads")
print(UPLOAD_FOLDER)
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    dir = UPLOAD_FOLDER
    # empty uploads folder as we do not save sound files of patients
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    return render_template("index.html",ospf = 1)

@app.route("/", methods = ['POST'])
def patient():
    if request.method == "POST":
        print(request)
        name = request.form["name"] #taking data from dictionary
        lungSounds = request.files["lungSounds"]
        print("\n")
        filename = secure_filename(lungSounds.filename)
        # temporarily save sound file of patient in the Uploads folder
        lungSounds.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url2 = os.path.join("static", "uploads")
        url = os.path.join(url2, filename)
        # url = os.path.abspath(url)
        print(url)
        absolute_url =  os.path.abspath(url)
        
        # pass url of sound file to the model
        res_list = rdc_model.classificationResults(absolute_url)
    return render_template("index.html",ospf = 0,n = name,  lungSounds = url, res = res_list)

if __name__ == "__main__":
    app.run()