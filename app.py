from flask import Flask, render_template, request

import pickle
import numpy as np
#import sklearn
#from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classifier_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Age = int(request.form['Age'])
        
        BMI_Class_Overweight=request.form['BMI_Class']
        if(BMI_Class_Overweight=='Overweight'):
                BMI_Class = 2
                
        elif(BMI_Class_Overweight=='Obese'):
                BMI_Class = 1
                
        else:
            BMI_Class = 0
            
        Use_Lenses = request.form['Use_Lenses']
        if( Use_Lenses =='Yes'):
             Use_Lenses = 1
        else:
             Use_Lenses = 0	

        Diabetes = request.form['Diabetes']
        if( Diabetes =='Yes'):
             Diabetes = 1
        else:
             Diabetes = 0

        High_Cholesterol = request.form['High_Cholesterol']
        if( High_Cholesterol =='Yes'):
             High_Cholesterol = 1
        else:
             High_Cholesterol = 0

        Have_Myopia = request.form['Have_Myopia']
        if( Have_Myopia =='Yes'):
             Have_Myopia = 1
        else:
             Have_Myopia=0

        Smoking = request.form['Smoking']
        if(Smoking =='Yes'):
            Smoking = 1
        else:
             Smoking = 0

        Alcohol=request.form['Alcohol']
        if( Alcohol=='Yes'):
             Alcohol=1
        else:
             Alcohol=0
        
        prediction=model.predict([[Age,BMI_Class,Use_Lenses,Diabetes,High_Cholesterol,Have_Myopia,Smoking,Alcohol]])
        
        output=(prediction[0])
        print(output)

        if output == 0:
            
             return render_template('index.html',prediction_text="You have no risk of cataract")
        elif output == 1:
             return render_template('index.html',prediction_text="You have low risk of cataract")
        else:
             return render_template('index.html',prediction_text="You have moderate risk of cataract")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

