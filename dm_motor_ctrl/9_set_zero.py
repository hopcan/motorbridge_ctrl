from motorbridge import Controller, Mode
import time 



motor_can_id = 0x01 
motor_master_id = 0x11
channel="/dev/ttyACM0"

#get motor handle
ctrl =Controller.from_dm_serial(channel,921600)
motor = ctrl.add_damiao_motor(motor_can_id, motor_master_id, "4340P")

#enable all motor

try:
    motor.set_zero_position()
    print("set zero successfully")
except Exception:
    print("set zero failed")
time.sleep(1)


#check the position
start = time.perf_counter()
dt = 0.01  # 10ms 
while time.perf_counter()- start < 1.0:
    now_time = time.perf_counter() - start
    motor.request_feedback()
    time.sleep(dt)
    state = motor.get_state()
    if state:
        print(f"time:{now_time:.3f}")
        print(f"pos: {state.pos:.3f} rad")
        print(f"vel: {state.vel:.3f} rad/s")
        print(f"torque: {state.torq:.3f} Nm\n")
    else:
        print("no respond\n")

time.sleep(1)

ctrl.close_bus()
ctrl.close()