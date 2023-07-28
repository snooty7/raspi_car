from Raspi_MotorHAT import Raspi_MotorHAT
import time

# Initialize the MotorHAT
motorhat = Raspi_MotorHAT(addr=0x6f)

# Define motor channels
motor1 = motorhat.getMotor(1)
motor2 = motorhat.getMotor(2)
motor3 = motorhat.getMotor(3)
motor4 = motorhat.getMotor(4)

# Test motors by running forward for 1 second, then stop
motor1.setSpeed(255)
motor1.run(Raspi_MotorHAT.FORWARD)
motor2.setSpeed(255)
motor2.run(Raspi_MotorHAT.FORWARD)
motor3.setSpeed(255)
motor3.run(Raspi_MotorHAT.FORWARD)
motor4.setSpeed(255)
motor4.run(Raspi_MotorHAT.FORWARD)

time.sleep(1)

motor1.setSpeed(0)
motor1.run(Raspi_MotorHAT.RELEASE)
motor2.setSpeed(0)
motor2.run(Raspi_MotorHAT.RELEASE)
motor3.setSpeed(0)
motor3.run(Raspi_MotorHAT.RELEASE)
motor4.setSpeed(0)
motor4.run(Raspi_MotorHAT.RELEASE)
