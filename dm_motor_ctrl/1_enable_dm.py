
#使能指定电机,3s后失能电机

from motorbridge import Controller, Mode
import time
motor_configs = {
    1 : {
        "can_id": 0x01,
        "master_id": 0x11, #0x10+1
        "model": "4310", #4310、4340P、6001
    },
}



ctrl = Controller.from_dm_serial("/dev/ttyACM0", 921600)


#add motor
motor={}
for num,cfg in motor_configs.items():
    motor[num] = ctrl.add_damiao_motor(cfg["can_id"], cfg["master_id"], cfg["model"])

#enable all motor
ctrl.enable_all()

time.sleep(3)
#disable all motor
ctrl.disable_all()