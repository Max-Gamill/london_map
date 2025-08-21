# colours

import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class tubeDataFrames:
    
    def __init__(self):
        self.line_dfs = {}
        self.board = np.zeros((20,66,3), dtype=np.uint8)
        
        for line in ["bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern", "piccadilly", "victoria", "waterloo-city", "elizabeth"]:
            try:
                df = pd.read_csv(f"{line}.csv")
                self.line_dfs[line] = df
            except FileNotFoundError as e:
                print(f"{line} .csv file not found. {e}")

    def reset_df_colours(self, line, colour):
        self.line_dfs[line][["R","G","B"]] = colour

    def apply_disruption_colours(self, line, station_dict):
        for disruption_description, values in station_dict.items(): # should just pass if empty
            for disruption_station in values["stations"]:
                self.line_dfs[line][self.line_dfs[line].loc["station"] == disruption_station][["R","G","B"]] = values["colour"]
        
    def update_board(self, line):
        # reset board
        self.board[:, :, :] = (0, 0, 0)
        self.board[self.line_dfs[line]["array_y"], self.line_dfs[line]["array_x"], :] = self.line_dfs[line][["R", "G", "B"]]


if __name__ == "__main__":
    # checks each board looks correct and overlays correctly
    tdfs = tubeDataFrames()
    print(tdfs.line_dfs["district"].head())

    plt.imshow(tdfs.board)

    for line in ["bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern", "piccadilly", "victoria", "waterloo-city", "elizabeth"]:
        tdfs.update_board(line)
        print(np.unique(tdfs.board, return_counts=True))
        plt.imshow(tdfs.board)