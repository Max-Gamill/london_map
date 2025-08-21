"""
London Underground LED Display System

Run this script on startup to continuously monitor TFL line status and update
the LED display board with service disruptions and delays.

Author: Maxgamill
"""

import time
from typing import Dict, Tuple, List

from tfl_status import LineStatus
from colours import tubeDataFrames


# RGB color values for each tube line
tube_colours: Dict[str, Tuple[int, int, int]] = {
    "bakerloo": (197, 98, 5),
    "central": (227, 32, 23),
    "circle": (255, 211, 0),
    "district": (0, 120, 41),
    "hammersmith-city": (236, 120, 155),
    "jubilee": (160, 165, 169),
    "metropolitan": (55, 0, 86),
    "northern": (255, 255, 255),
    "piccadilly": (8, 57, 190),
    "victoria": (0, 152, 212),
    "waterloo-city": (115, 176, 156),
    "elizabeth": (145, 79, 177),
}



if __name__ == "__main__":
    all_lines = ["bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern", "piccadilly", "victoria", "waterloo-city", "elizabeth"]
    # initialise dataframes
    tube_dfs = tubeDataFrames()

    # set LED disruption colours
    # disruption LEDs (x3): line, orange, red (make the central pink)

    while True:
        t1 = time.time()
        # loop to update the dataframe over all lines
        for line in all_lines:
            # reset all station colours
            tube_dfs.reset_df_colours(line, tube_colours[line])
            # change specific line colours  (line LEDs (x3))

            # get status & problematic stations
            status = LineStatus(line)
            data = status.get_line_status()
            stations = status.get_issue_stations(data) # should be a list of stations

            # apply station colour change dfs
            tube_dfs.apply_disruption_colours(line, stations)
        
        # iterate until next API call for 5 mins
        while time.time() - t1 > 60*5:
            # loop to cycle through all stations to update LEDs
            for line in all_lines:
                # update board
                tube_dfs.update_board(line)

                # update LEDs

                time.sleep(5) # sleep for 5s


