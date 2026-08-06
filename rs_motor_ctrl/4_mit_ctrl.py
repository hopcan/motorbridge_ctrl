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

# change to MIT mode，timeout 1000ms
motor.ensure_mode(Mode.MIT, timeout_ms=1000)

#control mit
motor.send_mit(
    pos=0.0,
    vel=0.0,
    kp=0.0,    
    kd=0.0,    
    tau=0.3   # 0.3Nm 
)

#run 3s
time.sleep(3)
#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()