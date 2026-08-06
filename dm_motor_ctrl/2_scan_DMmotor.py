from motorbridge import Controller

def scan_damiao_motors(start_can_id, end_can_id,channel="/dev/ttyACM0"):
    found_motors = []
    
    print(f"start scanning  {channel},canID : {start_can_id} - {end_can_id}")

    for motor_can_id in range(start_can_id, end_can_id + 1):
            ctrl =Controller.from_dm_serial(channel, 921600)
            temp_motor_master_id = 0x11 + motor_can_id

            try:
                motor = ctrl.add_damiao_motor(motor_can_id, temp_motor_master_id, "4340P")
                
                try:
                    # read register to get the can id
                    esc_id = motor.get_register_u32(8, timeout_ms=100)
                    master_id = motor.get_register_u32(7, timeout_ms=100)
                    print(f"[find] motor_can_id=0x{esc_id:02X} motor_master_id=0x{master_id:02X}")
                    found_motors.append((esc_id))
                    
                except Exception:
                    # read error, no this can id
                    print(f"[no respond] motor_can_id=0x{motor_can_id:02X}")
                    
                finally:
                    motor.close()

            except Exception as e:
                print(f"[error] motor_can_id=0x{motor_can_id:02X}: {e}")
            finally:
                ctrl.close_bus()
                ctrl.close()
    
    print(f"\nfinish find {len(found_motors)} motor")
    return found_motors

# 运行扫描
if __name__ == "__main__":
    motors = scan_damiao_motors(start_can_id=1, end_can_id=10,channel="/dev/ttyACM0")
    
    print("\nfind motor config:")
    for can_id in motors:
        print(f"  can_id=0x{can_id:02X}")