from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_review = data.get('review')
    
    
    if "amazing" in user_review.lower():
        sentiment = "Positive 😊"
    else:
        sentiment = "Negative 😞"
    
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
