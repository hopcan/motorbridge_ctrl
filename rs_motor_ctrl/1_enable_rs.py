
#使能指定电机,3s后失能电机

from motorbridge import Controller, Mode
import time
motor_configs = {
    1 : {
        "can_id": 0x07,
        "master_id": 0xfd, #fix
        "model": "rs-00", #rs-06、rs-00
    },
}



ctrl = Controller("can0")


#add motor
motor={}
for num,cfg in motor_configs.items():
    motor[num] = ctrl.add_robstride_motor(cfg["can_id"], cfg["master_id"], cfg["model"])

#enable all motor
ctrl.enable_all()

# change to MIT mode，timeout 1000ms  
motor[1].ensure_mode(Mode.MIT, timeout_ms=1000)

#control mit
motor[1].send_mit(
    pos=0.0,
    vel=0.0,
    kp=0.0,    
    kd=0.0,    
    tau=0.3  # 0.3Nm 
)

time.sleep(3)
#disable all motor
ctrl.disable_all()