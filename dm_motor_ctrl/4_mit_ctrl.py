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

# change to MIT mode，timeout 1000ms
motor.ensure_mode(Mode.MIT, timeout_ms=1000)

#control mit
motor.send_mit(
    pos=0.0,
    vel=0.0,
    kp=0.0,    
    kd=0.0,    
    tau=0.8   # 0.8Nm 
)

#run 5s
time.sleep(5)
#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()