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

# change to mit mode，timeout 1000ms
motor.ensure_mode(Mode.POS_VEL, 1000)

#record start time
start = time.perf_counter()

#control cycle
dt = 0.01  # 10ms 

#run 5s
while time.perf_counter()- start < 5.0:
    now_time = time.perf_counter() - start
    motor.send_pos_vel(
        pos=2.0,    # target angle（rad）
        vlim=1.5    # max vel（rad/s）
    )
    time.sleep(dt)
    state = motor.get_state()


    if state:
        print(f"time:{now_time:.3f}")
        print(f"pos: {state.pos:.3f} rad")
        print(f"vel: {state.vel:.3f} rad/s")
        print(f"torque: {state.torq:.3f} Nm\n")
    else:
        print("no respond\n")

#disable all motor
ctrl.disable_all()
ctrl.close_bus()
ctrl.close()