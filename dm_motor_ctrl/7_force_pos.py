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

# change to  force_pos mode，timeout 1000ms
motor.ensure_mode(Mode.FORCE_POS, 1000)

#control vel
motor.send_force_pos(
    pos=0.5,    # target angle（rad）
    vlim=1.0,   # max vel（rad/s）
    ratio=0.3   # torque ratio（0.0 - 1.0）0 means no torque, 1 means full torque
)

#run 5s
time.sleep(5)

#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()