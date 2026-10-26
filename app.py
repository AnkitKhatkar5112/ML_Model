from utils import make_predictions
from flask import render_template,request,jsonify
from flask import Flask
from utils import make_predictions
import pickle


tokenizer = pickle.load(open('models/cv.pkl', 'rb'))
model = pickle.load(open('models/clf.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text= request.form.get('email_content')

    predictions = make_predictions(email_text)

    return render_template('index.html', predictions = predictions, email_text = email_text)
    
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    email = data['content']

    predictions = make_predictions(email)

    return jsonify({predictions: predictions})


if __name__=='__main__':
    app.run(debug=True)