import sys
sys.path.append("C:/IPG/carmaker/win64-10.2.2/Python")

from parametrization_full_example import *


async def main():
    variation, variation_trailer = await make_variations()

    cmapi.logger.info(f"Executing with SimControl...")

    simcontrol = cmapi.SimControlInteractive()
    simcontrol.set_variation(variation)

    master = cmapi.CarMaker()
    await simcontrol.set_master(master)

    output_quants = cmapi.OutputQuantities.create()
    output_quants.add_quantities(["Car.v", "Time.Global", "Car.ay"])

    variation.set_outputquantities(output_quants)

    variation.set_storage_mode(cmapi.StorageMode.save)
    variation.set_storage_buffer_size(5000)
    # variation.set_initial_realtimefactor(1.0)


    # gpu_sensor = cmapi.GPUSensor()
    # await simcontrol.set_gpusensors([gpu_sensor])

    await simcontrol.start_and_connect()
    # await gpu_sensor.start()
    await simcontrol.start_sim()

    # Interactive commands
    condition = simcontrol.create_quantity_condition(lambda car_v: car_v > 10.0, "Car.v")
    await condition.wait()

    time_10, = await simcontrol.simio.dva_read_async("Time")
    cmapi.logger.info(f"{variation.get_name()}: Reached speed 10 m/s after {time_10} seconds")


    simcontrol.start_storage_save_all()
    output = variation.get_result_file_paths()
    print(f"Got output files: {output}")



    await simcontrol.create_simstate_condition(cmapi.ConditionSimState.finished).wait()
    await simcontrol.stop_and_disconnect()
    # await gpu_sensor.stop()

    cmapi.logger.info(f"Execution with SimControl finished.")

if __name__ == "__main__":
    cmapi.Task.run_main_task(main())
