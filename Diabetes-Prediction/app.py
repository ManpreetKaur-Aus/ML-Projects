from wsgiref import simple_server
from flask import Flask, request, app, render_template
from flask import Response
from flask_cors import CORS,cross_origin
from logistic_deploy import predObj

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


class ClientApi:

    def __init__(self):
        self.predObj = predObj()

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
def predictRoute():
    try:

        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['bloodPressure'])
        skin_thickness = float(request.form['skinThickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetesPedigreeFunction'])
        age = float(request.form['age'])

        data = [[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age]]
        # if request.json['data'] is not None:
        #     data = request.json['data']
        print('data is:     ', data)
        pred=predObj()
        prediction = pred.predict_log(data)

            #result = clntApp.predObj.predict_log(data)
        print('result is        ',prediction)
        return render_template('results.html', prediction=prediction)
    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'

# return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    #clntApp = ClientApi()
    #host = '0.0.0.0'
    #port = 5000
    app.run(debug=True)
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()