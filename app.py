from flask import Flask
import requests

app = Flask(__name__)

user = {
    'email': 'email',
    'twitter': 'twitter',
    'password': 'mek8792'
}

@app.route('/')
def main():
    res = requests.post('https://hypeeyes-auth-server.herokuapp.com/mekpremeRaffles', headers={"Content-Type": "application/json"}, json=user)
    text, json_res = '',''
    if res:
        json_res = res.json()
        text = res.text()
    code = res.status_code
    return f'{code} <br> {text} <br> {json_res}'

if __name__ == '__main__':
    app.run()