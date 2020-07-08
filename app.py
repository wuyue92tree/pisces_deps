from flask import Flask, render_template
from modules.car import Car
import settings

app = Flask(__name__)

smart_car = Car(**settings.car_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    smart_car.reset_status()
    smart_car.forward()
    smart_car.speed(50)
    return {'message': 'ok'}

@app.route('/backward')
def backward():
    smart_car.reset_status()
    smart_car.backward()
    smart_car.speed(50)
    return {'message': 'ok'}


@app.route('/left')
def left():
    smart_car.reset_status()
    smart_car.left(0)
    smart_car.forward()
    smart_car.speed(50)
    return {'message': 'ok'}


@app.route('/right')
def right():
    smart_car.reset_status()
    smart_car.right(0)
    smart_car.forward()
    smart_car.speed(50)
    return {'message': 'ok'}

@app.route('/stop')
def stop():
    smart_car.stop()
    return {'message': 'ok'}