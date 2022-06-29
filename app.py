from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_ngrok import run_with_ngrok
from flask_eureka import Eureka
from flask_eureka.eureka import eureka_bp

APPCODE = 'dokidokiwakuwaku'
HOSTNAME = 'https://bf7e-82-129-108-141.eu.ngrok.io'

app = Flask(__name__)
run_with_ngrok(app)

app.config.update(
    SERVICE_NAME=APPCODE,
    EUREKA_SERVICE_URL='https://servicediscovery.uat.industryapps.net',
    EUREKA_INSTANCE_HOSTNAME=HOSTNAME,
    EUREKA_HOME_PAGE_URL='https://' + HOSTNAME,
    EUREKA_INSTANCE_PORT=80
)

eureka = Eureka(app)
eureka.register_service(name="my-flask-service")

app.register_blueprint(eureka_bp)


@app.route('/')
def index():
    return jsonify(
        {"Hello": "World"}
    )


if __name__ == "__main__":
    app.run()