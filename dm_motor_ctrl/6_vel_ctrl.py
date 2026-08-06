from motorbridge import Controller, Mode
import time 


motor_can_id = 0x01 
motor_master_id = 0x11
channel="/dev/ttyACM0"

#get motor handle
ctrl =Controller.from_dm_serial(channel,921600)
motor = ctrl.add_damiao_motor(motor_can_id, motor_master_id, "4340P")

#enable all motor
ctrl.enable_all()

# change to VEL mode，timeout 1000ms
motor.ensure_mode(Mode.VEL, 1000)

#control vel
motor.send_vel(vel=1.0)  # 1 rad/s

#run 5s
time.sleep(5)

#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()