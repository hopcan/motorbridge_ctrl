from motorbridge import Controller, Mode
import time


def scan_damiao_motors(start_can_id, end_can_id,channel="can0"):
    found_motors=[]
    for motor_can_id in range(start_can_id, end_can_id + 1):
        ctrl =Controller(channel)
        

        try:
            motor = ctrl.add_robstride_motor(motor_can_id,0xfd, "rs-00")
            
            try:
                can_id, respond_id = motor.robstride_ping()
                found_motors.append(can_id)
                print(f"can_id={can_id:02X} respond_id={respond_id:02X}") #respond id is not master id
                
            except Exception:
                # scan error
                print(f"[no respond] no this motor_can_id=0x{motor_can_id:02X}")
                
            finally:
                motor.close()

        except Exception as e:
            print(f"[error] motor_can_id=0x{motor_can_id:02X}: {e}")
        finally:
            ctrl.close_bus()
            ctrl.close()
    print(f"\nfinish find {len(found_motors)} motor\n")
    return found_motors

if __name__ == "__main__" :
    motors=scan_damiao_motors(1, 10,channel="can0")
        
    print("\nfind motor config:")
    for can_id in motors:
        print(f"  can_id=0x{can_id:02X}")