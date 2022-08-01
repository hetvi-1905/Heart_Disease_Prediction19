# from markupsafe import escape
# from sklearn.pipeline import Pipeline
from flask import Flask, render_template, request
#import jsonify
# import requests
import pickle
# import numpy as np
# import sklearn

# import xgboost as xgb
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
# model = pickle.load(open('XGBoost_Classifier_model.pkl', 'rb'))

standard_to = StandardScaler()

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        d = int(request.form['d'])
        e = float(request.form['e'])

        h = standard_to.fit_transform([[a,b,c,d,e]])

        gender_type = request.form['gender_type']
        if (gender_type == 'Male'):
            sex_1 = 1
        else:
            sex_1 = 0

        cp = request.form['cp']
        if (cp == '1'):
            cp_1 = 1
            cp_2 = 0
            cp_3 = 0
        elif (cp=='2'):
            cp_1 = 0
            cp_2 = 1
            cp_3 = 0
        elif (cp=='3'):
            cp_1 = 0
            cp_2 = 0
            cp_3 = 1
        else:
            cp_1 = 0
            cp_2 = 0
            cp_3 = 0

        fbs = request.form['fbs']
        if (fbs == '1'):
            fbs_1 = 1
        else:
            fbs_1 = 0

        restecg = request.form['restecg']
        if (restecg == '1'):
            restecg_1 = 1
            restecg_2 = 0
        elif (restecg == '2'):
            restecg_1 = 0
            restecg_2 = 1
        else:
            restecg_1 = 0
            restecg_2 = 0

        exang = request.form['exang']
        if (exang == '0'):
            exang_1 = 1
        else:
            exang_1 = 0

        slope = request.form['slope']
        if (slope == '1'):
            slope_1 = 1
            slope_2 = 0
        elif (slope == '2'):
            slope_1 = 0
            slope_2 = 1
        else:
            slope_1 = 0
            slope_2 = 0

        ca = request.form['ca']
        if (ca == '1'):
            ca_1 = 1
            ca_2 = 0
            ca_3 = 0
            ca_4 = 0
        elif (ca == '2'):
            ca_1 = 0
            ca_2 = 1
            ca_3 = 0
            ca_4 = 0
        elif (ca == '3'):
            ca_1 = 0
            ca_2 = 0
            ca_3 = 1
            ca_4 = 0
        elif (ca == '4'):
            ca_1 = 0
            ca_2 = 0
            ca_3 = 0
            ca_4 = 1
        else:
            ca_1 = 0
            ca_2 = 0
            ca_3 = 0
            ca_4 = 0

        thal = request.form['thal']
        if (thal == '1'):
            thal_1 = 1
            thal_2 = 0
            thal_3 = 0
        elif (thal == '2'):
            thal_1 = 0
            thal_2 = 1
            thal_3 = 0
        elif (thal == '3'):
            thal_1 = 0
            thal_2 = 0
            thal_3 = 1
        else:
            thal_1 = 0
            thal_2 = 0
            thal_3 = 0


        prediction = model.predict([[h[0][0],h[0][1],h[0][2],h[0][3],h[0][4],sex_1,cp_1,cp_2,cp_3,fbs_1,restecg_1,restecg_2,exang_1,slope_1,slope_2,ca_1,ca_2,ca_3,ca_4,thal_1,thal_2,thal_3]])
        output = round(prediction[0], 2)

        if output == 0:
            # print("ans is 0")
            return render_template('index.html', prediction_text ="Patient Doesn't Have Heart Disease")
        else:
            # print("ans is 1")
            return render_template('index.html', prediction_text="Patient Has Heart Disease")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)