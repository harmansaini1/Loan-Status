from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('classifier.pkl', 'rb'))
app = Flask(__name__)


def predict():
    CoapplicantIncome = input("Enter the CoapplicantIncome：", type=NUMBER)
    LoanAmount = input("Enter LoanAmount", type=NUMBER)
    Loan_Amount_Term = input("Enter Loan_Amount_Term", type=NUMBER)
    ApplicantIncome = input("Enter ApplicantIncome", type=NUMBER)
    Gender = select('Gender', ['Male', 'Female'])
    if (Gender == 'Male'):
        Gender = 1
    else:
        Gender = 0
    Married = select('Married Status', ['Yes', 'No'])
    if (Married == 'Yes'):
        Married = 1
    else:
        Married = 0

    Dependents = select('Dependents(in numbers)', ['Zero', 'One', 'Two', 'More'])
    if (Dependents == 'Zero'):
        Dependents = 0
    elif (Dependents == 'One'):
        Dependents = 1
    elif (Dependents == 'Two'):
        Dependents = 2
    else:
        Dependents = 4

    Education = select('Education Status', ['Graduate', 'Non-Graduate'])
    if (Education == 'Graduate'):
        Education = 1
    else:
        Education = 0

    Self_Employed = select('Employment Status', ['Working', 'Non-Working'])
    if (Self_Employed == 'Working'):
        Self_Employed = 1
    else:
        Self_Employed = 0

    Credit_History = select('Credit History Status', ['Taken', 'Non-Taken'])
    if (Credit_History == 'Taken'):
        Credit_History = 1
    else:
        Credit_History = 0

    Property_Area = select('Property Area', ['Rural', 'Urban', 'Semiurban'])
    if (Property_Area == 'Rural'):
        Property_Area = 0
    elif (Property_Area == 'Urban'):
        Property_Area = 2
    else:
        Property_Area = 1


    prediction = model.predict([[CoapplicantIncome, Loan_Amount_Term, LoanAmount,ApplicantIncome, Gender,Married,Dependents,Education,Self_Employed,Credit_History,Property_Area ]])
    output = int(prediction)

    if output == 0:
        put_text("Loan not granted")

    else:
        put_text('Loan Granted')

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)
#if __name__ == '__main__':
    #predict()

#app.run(host='localhost', port=80)

#visit http://localhost/tool to open the PyWebIO application.


