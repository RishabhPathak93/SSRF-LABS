from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    try:
        response = requests.get(url)
        return render_template('result.html', content=response.text)
    except Exception as e:
        return render_template('result.html', content=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
