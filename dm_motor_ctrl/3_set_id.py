from motorbridge import Controller
from motorbridge import Controller, RID_MST_ID, RID_ESC_ID
import time
#set canID and masterID
def set_DMmotor_ID(old_can_id,new_can_id,new_master_id,channel="/dev/ttyACM0"):

    ctrl =Controller.from_dm_serial(channel, 921600)
    temp_motor_master_id= 0x10 + old_can_id 
    motor = ctrl.add_damiao_motor(old_can_id, temp_motor_master_id, "4340P")

    try :
        motor.write_register_u32(RID_MST_ID, new_master_id)
    except Exception:
        pass
    try :
        motor.write_register_u32(RID_ESC_ID, new_can_id)
    except Exception:
        pass
    new_motor = ctrl.add_damiao_motor(new_can_id , new_master_id, "4340P")
    new_motor.store_parameters()
    print("change ID and save")
    time.sleep(1)
    ctrl.close_bus()
    ctrl.close()

if __name__== "__main__" :
    old_can_id = 0x06
    new_can_id = 0x01
    new_master_id = 0x11
    set_DMmotor_ID(old_can_id,new_can_id,new_master_id,channel="/dev/ttyACM0")