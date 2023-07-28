from flask import Flask
from flask import request
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

app = Flask(__name__)

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(3)
myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.FORWARD)
myMotor.run(Raspi_MotorHAT.RELEASE)


def turnOffMotors():
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

@app.route("/")
def web_interface():
  html = open("web_interface.html")
  response = html.read().replace('\n', '')
  html.close()
  myMotor.setSpeed(0)
  return response

@app.route("/set_speed")
def set_speed():
  speed = request.args.get("speed")
  print("Received " + str(speed))

  direction = Raspi_MotorHAT.FORWARD
  if int(speed) < 0:
    direction = Raspi_MotorHAT.BACKWARD

  myMotor.run(direction)
  myMotor.setSpeed(abs(int(speed)))

  return "Received " + str(speed)

def main():
  app.run(host= '0.0.0.0')

main()
