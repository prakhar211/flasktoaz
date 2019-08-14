from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This sample script creates a web app in App Service with its related resources, and then deploys your web app code from a local Git repository."
