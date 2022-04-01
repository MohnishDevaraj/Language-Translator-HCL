from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = 'f9958bdaed7ba25babd76944734887d6'
from app import routes