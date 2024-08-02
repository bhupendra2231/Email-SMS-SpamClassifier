from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the model and vectorizer
with open('MB_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sms_text = request.form.get('sms_text')
    
    if not sms_text:
        return render_template('index.html', prediction='No text provided')

    text_vector = vectorizer.transform([sms_text])
    prediction = model.predict(text_vector)
    label = 'spam' if prediction[0] else 'not spam'
    
    return render_template('index.html', prediction=label)

if __name__ == '__main__':
    app.run(debug=True)
