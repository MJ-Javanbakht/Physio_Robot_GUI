import time
import canopen
import Adafruit_ADS1x15


class Isokinetic:
    def __init__(self):
        self.F_i1, self.F_i2, self.N_i, self.Count_i, self.Set_i, self.Stop_Time_i = [
            0
        ] * 6
        self.adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)
        self.network = canopen.Network()
        self.node1 = canopen.RemoteNode(1, "ASDA_A2_1042sub980_C.eds")

    def force_loadcell(self):
        GAIN = 1
        time.sleep(0.001)
        ADC_Value = (self.adc.read_adc(0, gain=GAIN, data_rate=860) - 19944) / 6.232
        return ADC_Value

    def output_force(self, exercise_num, input_force):
        if exercise_num == 1 or exercise_num == 4:
            return -input_force
        elif exercise_num == 2 or exercise_num == 3:
            return input_force

    def force_generator(
        self,
        position,
        range_of_motion_down,
        range_of_motion_up,
        extension_force,
        flexion_force,
    ):
        F_o = self.F_i1
        if position > range_of_motion_down:
            F_o = 1
        elif -range_of_motion_up > position:
            F_o = 2
        if self.F_i1 == 2:
            self.F_i1 = F_o
            return flexion_force
        else:
            self.F_i1 = F_o
            return extension_force

    def velocity_generator(
        self,
        position,
        range_of_motion_up,
        range_of_motion_down,
        flexion_speed,
        extension_speed,
        exercise_num,
        reference_force,
        force,
    ):
        N_o = self.N_i
        velocity = extension_speed
        if exercise_num == 1:
            if reference_force < 0:
                if N_o == 0:  # Down
                    if force > reference_force:
                        velocity = 0
                    else:
                        velocity = flexion_speed
                    if position > range_of_motion_down:
                        N_o = 1
                if N_o == 1:  # Up
                    if force < -reference_force:
                        velocity = 0
                    else:
                        velocity = -extension_speed
                    if position < -range_of_motion_up:
                        N_o = 0
        # Similar logic for other exercise_nums
        if reference_force == 0:
            velocity = 0
        self.N_i = N_o
        return velocity

    def set_repeat(
        self,
        range_of_motion_up,
        range_of_motion_down,
        velocity,
        sets_desired,
        rest_time,
        repeats_desired,
        position,
    ):
        F_o = self.F_i2
        Count_o = self.Count_i
        Set_o = self.Set_i
        Stop_Time_o = self.Stop_Time_i
        if position > 0:
            F_o = 1
        elif -range_of_motion_up > position:
            F_o = 2
        if F_o == 1 and self.F_i2 == 2:
            Count_o = self.Count_i + 1
        if Count_o == repeats_desired:
            if self.Set_i < sets_desired:
                Set_o = self.Set_i + 1
            Count_o = 0
            Stop_Time_o = time.time()
        if Set_o >= sets_desired:
            Set_o = sets_desired
        if self.Set_i >= sets_desired or time.time() - self.Stop_Time_i < rest_time:
            output = 0
        else:
            output = velocity
        self.F_i2 = F_o
        self.Count_i = Count_o
        self.Set_i = Set_o
        self.Stop_Time_i = Stop_Time_o
        return output

    def safety_function(self, time, theta_sat_pos, theta_sat_neg, input_force, theta):
        run_time_old = 0
        run_time = run_time_old + 0.001
        if theta > theta_sat_pos or theta < theta_sat_neg:
            output = 0
        else:
            output = input_force
        if run_time > time - 5:
            output = 0.01 * (-theta)
        run_time_old = run_time
        return output

    def init_drive(self):
        self.node1.nmt.state = "PRE-OPERATIONAL"
        self.node1.sdo["Controlword"].raw = 128  # Clear_Error
        self.node1.sdo["Controlword"].raw = 0  # Switch_ON
        self.node1.sdo["Controlword"].raw = 6
        self.node1.sdo["Controlword"].raw = 7  # Init & Run
        self.node1.sdo["Controlword"].raw = 15
        self.node1.sdo["Modes of operation"].raw = 3  # Velocity Mode
        self.node1.rpdo.read()
        self.node1.tpdo.read()
        self.node1.tpdo[1].clear()
        self.node1.tpdo[1].add_variable("Position actual value")
        self.node1.tpdo[1].enabled = True
        self.node1.tpdo[1].save()
        self.node1.rpdo[1].clear()
        self.node1.rpdo[1].add_variable("Target velocity")
        self.node1.rpdo[1].enabled = True
        self.node1.rpdo.save()
        self.node1.rpdo[1].start(0.005)

    def run(self):
        try:
            while True:
                position = self.node1.tpdo[1]["Position actual value"].raw * (
                    360 / (1280000 * 25)
                )
                (
                    range_of_motion_down,
                    range_of_motion_up,
                    extension_force,
                    flexion_force,
                ) = [0, 70, 15, 15]
                reference_force = self.force_generator(
                    position,
                    range_of_motion_down,
                    range_of_motion_up,
                    extension_force,
                    flexion_force,
                )

                flexsion_speed, extension_speed, exercise_num = [350, 350, 2]
                reference_force = self.output_force(exercise_num, reference_force)
                force = self.force_loadcell()
                velocity = self.velocity_generator(
                    position,
                    range_of_motion_up,
                    range_of_motion_down,
                    flexsion_speed,
                    extension_speed,
                    exercise_num,
                    reference_force,
                    force,
                )

                sets_desired, rest_time, repeats_desired = [2, 10, 1]
                velocity = self.set_repeat(
                    range_of_motion_up,
                    range_of_motion_down,
                    velocity,
                    sets_desired,
                    rest_time,
                    repeats_desired,
                    position,
                )

                self.node1.rpdo[1]["Target velocity"].raw = velocity

        except KeyboardInterrupt:
            print("STOP!")
            self.node1.sdo["Controlword"].raw = 0
            self.network.disconnect()


if __name__ == "__main__":
    isokinetic_instance = Isokinetic()
    isokinetic_instance.init_drive()
    print("All nodes are initiated")
    isokinetic_instance.node1.nmt.state = "OPERATIONAL"
    isokinetic_instance.run()
