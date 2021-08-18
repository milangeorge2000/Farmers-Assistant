from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pickle
import pandas as pd


# Define a flask app
app = Flask(__name__)

description_data = pickle.load(open("description.pkl","rb"))
precaution_data = pickle.load(open("precaution.pkl","rb"))
remedies_data = pickle.load(open("remedies.pkl","rb"))


crop_model = load_model("denseplant.h5")
soil_model = pickle.load(open("rf.pkl", 'rb'))
fert_model = pickle.load(open("rf_fert.pkl",'rb'))


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/index.html', methods=['GET'])
def home():
    # Main page
    return render_template('index.html')


@app.route('/fertilizerform.html', methods=['GET'])
def fertilizer():
    # Main page
    return render_template('fertilizerform.html')

@app.route('/soilform.html', methods=['GET'])
def crop():
    # Main page
    return render_template('soilform.html')

@app.route('/diseaseform.html', methods=['GET'])
def disease():
    # Main page
    return render_template('diseaseform.html')

@app.route('/diseasepredict', methods=['GET', 'POST'])
def leafupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        f.save("img.jpg")
        



        img = image.load_img("img.jpg",target_size=(224,224)) ##loading the image
        img = np.asarray(img) ##converting to an array
        img = img / 255 ##scaling by doing a division of 255
        img = np.expand_dims(img, axis=0) ##expanding the dimensions
        global output
        output = crop_model.predict(img)
        output = np.argmax(output, axis=1)
        if output[0] == 0 :
             return render_template("disease.html",prediction="Pepper Bell Bacterial Spot")
  
        elif output[0] == 1:
              return render_template("disease.html",prediction="Pepper Bell Healthy")

        elif output[0] == 2 :
             return render_template("disease.html",prediction="Potato Early Blight")
        
        elif output[0] == 3 :
             return render_template("disease.html",prediction="Potato Healthy")
        
        elif output[0] == 4 :
             return render_template("disease.html",prediction="Potato Late Blight")
        
        elif output[0] == 5 :
             return render_template("disease.html",prediction="Tomato Bacterial Spot")
        
        elif output[0] == 6 :
             return render_template("disease.html",prediction="Tomato Early Blight")

        elif output[0] == 7 :
               return render_template("disease.html",prediction="Tomato Healthy")

        elif output[0] == 8 :
               return render_template("disease.html",prediction="Tomato Late Blight")

        elif output[0] == 9 :
               return render_template("disease.html",prediction="Tomato Leaf Mold")

        elif output[0] == 10 :
               return render_template("disease.html",prediction="Tomato Mosaic Virus")
          
        elif output[0] == 11 :
               return render_template("disease.html",prediction="Tomato Septoria Leaf Spot")
          
        elif output[0] == 12:
               return render_template("disease.html",prediction="Tomato Spider Mites")

        elif output[0] == 13:
               return render_template("disease.html",prediction="Tomato Target Spot")

        elif output[0] == 14:
               return render_template("disease.html",prediction="Tomato Yellow Leaf Curl Virus")

        
@app.route('/description.html', methods=['GET'])
def get_description():
     if output[0] == 0 :
             return render_template("description.html",description=description_data[0])
  
     elif output[0] == 1:
              return render_template("description.html",description=description_data[1])

     elif output[0] == 2 :
             return render_template("description.html",description=description_data[2])
        
     elif output[0] == 3 :
          return render_template("description.html",description=description_data[3])
     
     elif output[0] == 4 :
          return render_template("description.html",description=description_data[4])
     
     elif output[0] == 5 :
          return render_template("description.html",description=description_data[5])
     
     elif output[0] == 6 :
          return render_template("description.html",description=description_data[6])

     elif output[0] == 7 :
          return render_template("description.html",description=description_data[7])

     elif output[0] == 8 :
          return render_template("description.html",description=description_data[8])

     elif output[0] == 9 :
          return render_template("description.html",description=description_data[9])

     elif output[0] == 10 :
          return render_template("description.html",description=description_data[10])
     
     elif output[0] == 11 :
          return render_template("description.html",description=description_data[11])
        
     elif output[0] == 12:
          return render_template("description.html",description=description_data[12])

     elif output[0] == 13:
          return render_template("description.html",description=description_data[13])

     elif output[0] == 14:
          return render_template("description.html",description=description_data[14])


        
@app.route('/remedies.html', methods=['GET'])
def get_remedies():
     if output[0] == 0 :
             return render_template("remedies.html",remedies=remedies_data[0])
  
     elif output[0] == 1:
              return render_template("remedies.html",remedies=remedies_data[1])

     elif output[0] == 2 :
             return render_template("remedies.html",remedies=remedies_data[2])
        
     elif output[0] == 3 :
          return render_template("remedies.html",remedies=remedies_data[3])
     
     elif output[0] == 4 :
          return render_template("remedies.html",remedies=remedies_data[4])
     
     elif output[0] == 5 :
          return render_template("remedies.html",remedies=remedies_data[5])
     
     elif output[0] == 6 :
          return render_template("remedies.html",remedies=remedies_data[6])

     elif output[0] == 7 :
          return render_template("remedies.html",remedies=remedies_data[7])

     elif output[0] == 8 :
          return render_template("remedies.html",remedies=remedies_data[8])

     elif output[0] == 9 :
          return render_template("remedies.html",remedies=remedies_data[9])

     elif output[0] == 10 :
          return render_template("remedies.html",remedies=remedies_data[10])
     
     elif output[0] == 11 :
          return render_template("remedies.html",remedies=remedies_data[11])
        
     elif output[0] == 12:
          return render_template("remedies.html",remedies=remedies_data[12])

     elif output[0] == 13:
          return render_template("remedies.html",remedies=remedies_data[13])

     elif output[0] == 14:
          return render_template("remedies.html",remedies=remedies_data[14])

  
@app.route('/precaution.html', methods=['GET'])
def get_precaution():
     if output[0] == 0 :
             return render_template("precaution.html",precaution=precaution_data[0])
  
     elif output[0] == 1:
              return render_template("precaution.html",precaution=precaution_data[1])

     elif output[0] == 2 :
             return render_template("precaution.html",precaution=precaution_data[2])
        
     elif output[0] == 3 :
          return render_template("precaution.html",precaution=precaution_data[3])
     
     elif output[0] == 4 :
          return render_template("precaution.html",precaution=precaution_data[4])
     
     elif output[0] == 5 :
          return render_template("precaution.html",precaution=precaution_data[5])
     
     elif output[0] == 6 :
          return render_template("precaution.html",precaution=precaution_data[6])

     elif output[0] == 7 :
          return render_template("precaution.html",precaution=precaution_data[7])

     elif output[0] == 8 :
          return render_template("precaution.html",precaution=precaution_data[8])

     elif output[0] == 9 :
          return render_template("precaution.html",precaution=precaution_data[9])

     elif output[0] == 10 :
          return render_template("precaution.html",precaution=precaution_data[10])
     
     elif output[0] == 11 :
          return render_template("precaution.html",precaution=precaution_data[11])
        
     elif output[0] == 12:
          return render_template("precaution.html",precaution=precaution_data[12])

     elif output[0] == 13:
          return render_template("precaution.html",precaution=precaution_data[13])

     elif output[0] == 14:
          return render_template("precaution.html",precaution=precaution_data[14])

@app.route('/soilpredict', methods=['GET', 'POST'])
def soilpredict():
    if request.method == 'POST':
        # Get the file from post request
          N=float(request.form['nitrogen'])
          P=float(request.form['phosphorous'])
          PT=float(request.form['pottasium'])
          T = float(request.form['temperature'])
          H = float(request.form['humidity'])
          PH=float(request.form['phlevel'])
          R =float(request.form['rainfall'])
          data = np.array([[N,P,PT,T,H,PH,R]])


          predictions = soil_model.predict(data)
          return render_template("prediction.html",prediction=predictions[0])


@app.route('/fertilizerpredict', methods=['GET', 'POST'])
def fertilizerpredict():
    if request.method == 'POST':
        # Get the file from post request
          temp=float(request.form['temp'])
          humid=float(request.form['humid'])
          moisture=float(request.form['moisture'])
          nitrogen= float(request.form['nitro'])
          potassium = float(request.form['pott'])
          phosphorous =float(request.form['phos'])
          temp_array = list()
                  
          soil = request.form['Soil-Type']
          if soil == 'Black':
               temp_array = temp_array + [1,0,0,0,0]
          elif soil == 'Clayey':
               temp_array = temp_array + [0,1,0,0,0]
          elif soil == 'Loamy':
               temp_array = temp_array + [0,0,1,0,0]
          elif soil == 'Red':
               temp_array = temp_array + [0,0,0,1,0]
          elif soil == 'Sandy':
               temp_array = temp_array + [0,0,0,0,1]
          
                  
          crop = request.form['Crop-Type']
          if crop == 'Barley':
               temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0]
          elif crop == 'Cotton':
               temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0]
          elif crop == 'Ground Nuts':
               temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0]
          elif crop == 'Maize':
               temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0]
          elif crop == 'Millets':
               temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0]
          elif crop == 'Oil seeds':
               temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0]
          elif crop == 'Paddy':
               temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0]
          elif crop == 'Pulses':
               temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0]
          elif crop == 'Sugarcane':
           temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0]
          elif crop == 'Tobacco':
             temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0]
          elif crop == 'Wheat':
                temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1]

          
          data = [[temp,humid,moisture,nitrogen,potassium,phosphorous] + temp_array]

          
       
          


          predictions = fert_model.predict(data)
          return render_template("prediction.html",prediction=predictions[0])





if __name__ == '__main__':
    app.run(debug=False)
