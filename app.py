from flask import Flask, render_template, request
import time
from Raspi_MotorHAT import Raspi_MotorHAT
import atexit

app = Flask(__name__)

# Initialize the MotorHAT
motorhat = Raspi_MotorHAT(addr=0x6f)

# Define motor channels
motor1 = motorhat.getMotor(1)
motor2 = motorhat.getMotor(2)
motor3 = motorhat.getMotor(3)
motor4 = motorhat.getMotor(4)

def turnOffMotors():
    motorhat.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    motorhat.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    motorhat.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    motorhat.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    speed = int(request.form['speed'])

    # Set the motor speeds based on the direction
    if direction == 'forward':
        motor1.setSpeed(speed)
        motor1.run(Raspi_MotorHAT.FORWARD)
        motor2.setSpeed(speed)
        motor2.run(Raspi_MotorHAT.FORWARD)
        motor3.setSpeed(speed)
        motor3.run(Raspi_MotorHAT.FORWARD)
        motor4.setSpeed(speed)
        motor4.run(Raspi_MotorHAT.FORWARD)
    elif direction == 'backward':
        motor1.setSpeed(speed)
        motor1.run(Raspi_MotorHAT.BACKWARD)
        motor2.setSpeed(speed)
        motor2.run(Raspi_MotorHAT.BACKWARD)
        motor3.setSpeed(speed)
        motor3.run(Raspi_MotorHAT.BACKWARD)
        motor4.setSpeed(speed)
        motor4.run(Raspi_MotorHAT.BACKWARD)
    elif direction == 'left':
        motor1.setSpeed(speed)
        motor1.run(Raspi_MotorHAT.FORWARD)
        motor2.setSpeed(speed)
        motor2.run(Raspi_MotorHAT.BACKWARD)
        motor3.setSpeed(speed)
        motor3.run(Raspi_MotorHAT.FORWARD)
        motor4.setSpeed(speed)
        motor4.run(Raspi_MotorHAT.BACKWARD)
    elif direction == 'right':
        motor1.setSpeed(speed)
        motor1.run(Raspi_MotorHAT.BACKWARD)
        motor2.setSpeed(speed)
        motor2.run(Raspi_MotorHAT.FORWARD)
        motor3.setSpeed(speed)
        motor3.run(Raspi_MotorHAT.BACKWARD)
        motor4.setSpeed(speed)
        motor4.run(Raspi_MotorHAT.FORWARD)
    else:
        # Stop all motors
        motor1.setSpeed(0)
        motor1.run(Raspi_MotorHAT.RELEASE)
        motor2.setSpeed(0)
        motor2.run(Raspi_MotorHAT.RELEASE)
        motor3.setSpeed(0)
        motor3.run(Raspi_MotorHAT.RELEASE)
        motor4.setSpeed(0)
        motor4.run(Raspi_MotorHAT.RELEASE)

    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
