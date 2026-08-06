from motorbridge import Controller, Mode
import time 



motor_can_id = 0x01 
motor_master_id = 0xfd
channel="can0"

#get motor handle
ctrl =Controller(channel)
motor = ctrl.add_robstride_motor(motor_can_id, motor_master_id, "rs-00")

#enable all motor
ctrl.enable_all()

# change to POS-VEL mode，timeout 1000ms
motor.ensure_mode(Mode.POS_VEL, timeout_ms=1000)

#control pos_vel

motor.send_pos_vel(
    pos=2.0,    # target angle（rad）
    vlim=1.5    # max vel（rad/s）
)

#run 5s
time.sleep(5)

#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()