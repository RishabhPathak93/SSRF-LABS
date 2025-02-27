from flask import Flask, request, render_template
import requests
import re

app = Flask(__name__)

ALLOWED_DOMAINS = ["example.com", "api.example.com"]

def is_url_allowed(url):
    pattern = r"https?://([^/]+)"
    match = re.match(pattern, url)
    if match:
        domain = match.group(1)
        return any(domain.endswith(allowed) for allowed in ALLOWED_DOMAINS)
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')

    if not is_url_allowed(url):
        return render_template('result.html', content="Access Denied: Domain not allowed.")

    try:
        response = requests.get(url)
        return render_template('result.html', content=response.text)
    except Exception as e:
        return render_template('result.html', content=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
