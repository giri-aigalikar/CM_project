import testutils

import cmapi
from cmapi import Task

from pathlib import Path

async def main():

    sim_control = await testutils.init_all_interactive()
    variation = sim_control.get_variation()

    output_quants = cmapi.OutputQuantities.create()
    output_quants.add_quantities(["Car.v", "Time.Global", "TrfLight.*.State"])

    variation.set_outputquantities(output_quants)

    variation.set_storage_mode(cmapi.StorageMode.save)
    variation.set_storage_buffer_size(5000)
    variation.set_initial_realtimefactor(1.0)

    await sim_control.start_and_connect()


    await sim_control.start_sim()
    await sim_control.simstate.condition_running.wait()

    await cmapi.Task.sleep(10)

    # defaults, 1st output file with whole buffer content (should be 5 seconds)
    # TODO: Figure out, why set_storage_buffer_size(5000) has no effect
    sim_control.save_storage_buffer()

    await cmapi.Task.sleep(5)
    # 2nd output file with 3 seconds of buffer content
    sim_control.save_storage_buffer(3*1000)

    await cmapi.Task.sleep(5)

    # 3rd output file with 2x3 seconds output
    sim_control.save_storage_buffer(3*1000, 3*1000)

    await cmapi.Task.sleep(5)

    # 4th, the rest
    sim_control.start_storage_save_all()

    await sim_control.simstate.condition_finished.wait()

    await sim_control.stop_and_disconnect()

    output = variation.get_result_file_paths()
    print(f"Got output files: {output}")

    assert len(output) == 4
    assert abs(2*Path(output[1]).stat().st_size - Path(output[2]).stat().st_size) < 100
    assert Path(output[3]).stat().st_size > Path(output[2]).stat().st_size



Task.run_main_task(main())
