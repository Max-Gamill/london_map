#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 21:53:36 2025

@author: Maxgamill

Uses the TFL API to obtain the status of the TFL lines
"""

import requests
import json
import time
import networkx
import re

from tube_graphs import tubeGraphs
import tests_tfl


class LineStatus:

    def __init__(self): 
        self.colours = {
            # disruption colours
            "red": (255, 0, 0),
            "orange": (55, 100, 100), # ?
            "green" : (0, 255, 0),
            "white": (255, 255, 255),
            "off": (0, 0, 0),
            # line colours
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


        self.severity_codes = {
            "Planned Closure": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "Part Closure": {"code": 0, "colour": self.colours['red'], "alt_words": ["No Service"]},
            "Severe Delays": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Part Suspended": {"code": 0, "colour": self.colours['red'], "alt_words": ["No Service"]},
            "Suspended": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "Delayed": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Minor Delays": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Good Service": {"code": 0, "colour": self.colours['green'], "alt_words": []},
            "Part Closed": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "Reduced Service": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Special Service": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Bus Service": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "No Step Free Access": {"code": 0, "colour": self.colours['green'], "alt_words": []},
            "Change of Frequency": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "Diverted": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "Not Running": {"code": 0, "colour": self.colours['red'], "alt_words": []},
            "Issues Reported": {"code": 0, "colour": self.colours['orange'], "alt_words": []},
            "No Issues": {"code": 0, "colour": self.colours['green'], "alt_words": []},
            "Information": {"code": 0, "colour": self.colours['green'], "alt_words": []},
            "Service Closed": {"code": 0, "colour": self.colours['red'], "alt_words": []},
        }
        
        # Collect all descriptions and alt words into one list
        severity_phrases = []
        for desc, info in self.severity_codes.items():
            severity_phrases.append(desc)
            for alt in info.get("alt_words", []):
                if alt:
                    severity_phrases.append(alt)
        # Create regex pattern to match any of them (case-insensitive, word-boundaries)
        self.pattern = r'(?i)\b(' + '|'.join(re.escape(p.lower()) for p in severity_phrases) + r')\b'



    def get_line_status(line_id: str) -> dict | None:
        """
        Get the current status of the TFL line.
    
        Parameters
        ----------
        line_id : str
            The id corresponding to the line.
    
        Returns
        -------
        dict | None
            Dictionary of the service status. Is "None" when request fails.
    
        """
    
        response = requests.get(f"https://api.tfl.gov.uk/Line/{line_id}/Status")
        
        if response.status_code == 200:
            data = response.json()[0]
            
            return data
        return None
    
    
    def get_issue_stations(self, data: dict) -> dict:
        """
        Parse the description and return a dictionary of the type of closure and 
        delays.
    
        Parameters
        ----------
        data : dict
            DESCRIPTION.
    
        Returns
        -------
        dict
            DESCRIPTION.
    
        """
        results = {}
        
        # check if good service
        if data["lineStatuses"][0]["statusSeverity"] == 10:
            return {}
        
        # get reason, severity number and severity
        for status in data["lineStatuses"]:
            reason = status["reason"] # is the same for all statuses
            severity_number = status["statusSeverity"]
            # compile descriptions
            descriptions = [status["statusSeverityDescription"]] + self.severity_codes[status["statusSeverityDescription"]]["alt_words"]
            print(f"{severity_number} - {descriptions}: {reason}")
            # obtain the problematic stations and their issue
            results[severity_number] = self.parse_description(reason, descriptions)
        
        return results
    
    
    @staticmethod
    def split_reason_phrase(reason: str, pattern: str) -> list[str]:
        # split sentences and have them contain the desruption description
        matches = list(re.finditer(pattern, reason.lower()))
        sentences = []
        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(reason)
            chunk = reason[start:end].strip()
            sentences.append(chunk)
        # also split by sentence
        sentences_parts = [part for item in sentences for part in item.split('.')]
    
        return sentences_parts
    
    
    def parse_description(self, reason: str, descriptions: list[str]) -> dict:
        """
        
    
        Parameters
        ----------
        reason : str
            DESCRIPTION.
        descriptions : list[str]
            DESCRIPTION.
    
        Returns
        -------
        dict
            Dictionary of {station: {
                station_code,
                station_LED_ID,
                station_array_coord,
                station_colour
                }}.
    
        """
        print()
        sentences_parts = self.split_reason_phrase(reason, self.pattern)
        stations = {}
    
        # find relevant sentence
        for sentence in sentences_parts:
            print(descriptions, ' - ', sentence)
            # check if description is in the closure sentence message
            for description in descriptions:
                if description.lower() in sentence.lower():
                    # obtain identifer of which stations relate to the description
                    
                    # if "all" used get all stations
                    if " all " in sentence:
                        print("-> all present")
                        #stations = tubeGraphs().bakerloo_stations # these are objects in tube_graphs
                        pass
                    
                    # if "rest" used get remaining stations -> after all sentences parsed!
                    if " rest " in sentence:
                        print("-> rest present")
            
                    # if "between" used, use graphs to get stations
                    if " between " in sentence:
                        between_stations = re.findall(r' between ([\w\s]+) and ([\w\s]+)', sentence)
                        print("-> between present: ", between_stations)
                        # find relevant stations
                    
                        # add to colour
                        stations[description] = between_stations
        
        return stations
    
    def station_colours():
        pass


if __name__ == "__main__":
    #data = get_line_status("district")
    data = tests_tfl.weird_part_closure
    status = LineStatus()
    stations = status.get_issue_stations(data) # should be a list of stations




