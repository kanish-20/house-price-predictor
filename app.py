from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        bedroom = int(request.form['bedroom'])
        Area = float(request.form['Area'])

       
        prediction = model.predict([[Area, bedroom]])[0]
        prediction = round(prediction, 2)

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
