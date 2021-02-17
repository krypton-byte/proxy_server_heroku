from threading import Thread
from pyngrok import ngrok
from flask import Flask
from os import system
from os import environ
app=Flask(__name__)
Thread(target=system, args=("proxy --hostname=127.0.0.1 --port=8000", )).start()
ngrok.set_auth_token("YOUR_NGROK_APIKEY")
tcp=ngrok.connect(8000, "tcp")
@app.route("/")
def index():
    return str(tcp.public_url)
app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))