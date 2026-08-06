from motorbridge import Controller
from motorbridge import Controller, RID_MST_ID, RID_ESC_ID
import time
#set canID 
def set_DMmotor_ID(old_can_id,new_can_id,channel="can0"):

    ctrl =Controller(channel)
   
    motor = ctrl.add_robstride_motor(old_can_id,0xfd, "rs-00")
    try :
        motor.robstride_set_device_id(new_can_id)
        print(f"change to new id :{new_can_id}")
    except Exception:
        print("set id failed")

    time.sleep(1)
    ctrl.close_bus()
    ctrl.close()

if __name__== "__main__" :
    old_can_id = 0x01
    new_can_id = 0x01
    set_DMmotor_ID(old_can_id,new_can_id,channel="can0")