#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 22:36:02 2025

@author: Maxgamill
"""
from collections import OrderedDict
import string

import networkx as nx
import matplotlib.pyplot as plt
import requests
import pandas as pd
import regex


def get_station_codes(line_id: str) -> dict:
    """
    Obtain the station codes and names in a 1-2-1 dictionary.

    Parameters
    ----------
    line_id : str
        The ID of the tube line.

    Returns
    -------
    dict
        1-2-1 dictionary of tube stop ID : tube stop name.

    """
    b = requests.get(f"https://api.tfl.gov.uk/Line/{line_id}/Route/Sequence/inbound", timeout=1000).json()
    d = {}
    for seq in b["stopPointSequences"]:
        for stop in seq["stopPoint"]:
            d[stop["id"]] = stop["name"]

    return d


class tubeGraphs:

    def __init__(self):
        self.bakerloo_stations = [OrderedDict({
            '940GZZLUHAW': 'Harrow & Wealdstone',
            '940GZZLUKEN': 'Kenton',
            '940GZZLUSKT': 'South Kenton',
            '940GZZLUNWY': 'North Wembley',
            '940GZZLUWYC': 'Wembley Central',
            '940GZZLUSGP': 'Stonebridge Park',
            '940GZZLUHSN': 'Harlesden',
            '940GZZLUWJN': 'Willesden Junction',
            '940GZZLUKSL': 'Kensal Green',
            '940GZZLUQPS': "Queen's Park",
            '940GZZLUKPK': 'Kilburn Park',
            '940GZZLUMVL': 'Maida Vale',
            '940GZZLUWKA': 'Warwick Avenue',
            '940GZZLUPAC': 'Paddington',
            '940GZZLUERB': 'Edgware Road (Bakerloo)',
            '940GZZLUMYB': 'Marylebone',
            '940GZZLUBST': 'Baker Street',
            '940GZZLURGP': "Regent's Park",
            '940GZZLUOXC': 'Oxford Circus',
            '940GZZLUPCC': 'Piccadilly Circus',
            '940GZZLUCHX': 'Charing Cross',
            '940GZZLUEMB': 'Embankment',
            '940GZZLUWLO': 'Waterloo',
            '940GZZLULBN': 'Lambeth North',
            '940GZZLUEAC': 'Elephant & Castle'
            })]

        self.central_stations = [
            OrderedDict({
                '940GZZLUEPG': 'Epping',
                '940GZZLUTHB': 'Theydon Bois',
                '940GZZLUDBN': 'Debden',
                '940GZZLULGN': 'Loughton',
                '940GZZLUBKH': 'Buckhurst Hill',
                '940GZZLUWOF': 'Woodford',
                '940GZZLUSWF': 'South Woodford',
                '940GZZLUSNB': 'Snaresbrook',
                '940GZZLULYS': 'Leytonstone',
                '940GZZLULYN': 'Leyton',
                '940GZZLUSTD': 'Stratford',
                '940GZZLUMED': 'Mile End',
                '940GZZLUBLG': 'Bethnal Green',
                '940GZZLULVT': 'Liverpool Street',
                '940GZZLUBNK': 'Bank',
                '940GZZLUSPU': "St. Paul's",
                '940GZZLUCHL': 'Chancery Lane',
                '940GZZLUHBN': 'Holborn',
                '940GZZLUTCR': 'Tottenham Court Road',
                '940GZZLUOXC': 'Oxford Circus',
                '940GZZLUBND': 'Bond Street',
                '940GZZLUMBA': 'Marble Arch',
                '940GZZLULGT': 'Lancaster Gate',
                '940GZZLUQWY': 'Queensway',
                '940GZZLUNHG': 'Notting Hill Gate',
                '940GZZLUHPK': 'Holland Park',
                '940GZZLUSBC': "Shepherd's Bush (Central)",
                '940GZZLUWCY': 'White City',
                '940GZZLUEAN': 'East Acton',
                '940GZZLUNAN': 'North Acton',
                '940GZZLUHGR': 'Hanger Lane',
                '940GZZLUPVL': 'Perivale',
                '940GZZLUGFD': 'Greenford',
                '940GZZLUNHT': 'Northolt',
                '940GZZLUSRP': 'South Ruislip',
                '940GZZLURSG': 'Ruislip Gardens',
                '940GZZLUWRP': 'West Ruislip',

            }),
            OrderedDict({
                '940GZZLUEBY': 'Ealing Broadway',
                '940GZZLUWTA': 'West Acton',
                '940GZZLUNAN': 'North Acton',
                }),
            OrderedDict({
                '940GZZLULYS': 'Leytonstone',
                '940GZZLUWSD': 'Wanstead',
                '940GZZLURBG': 'Redbridge',
                '940GZZLUGTH': 'Gants Hill',
                '940GZZLUBKE': 'Barkingside',
                '940GZZLUNBP': 'Newbury Park',
                '940GZZLUFLP': 'Fairlop',
                '940GZZLUHLT': 'Hainault',
                '940GZZLUGGH': 'Grange Hill',
                '940GZZLUCWL': 'Chigwell',
                '940GZZLURVY': 'Roding Valley',
                '940GZZLUWOF': 'Woodford',
                })
            
            ]

        self.circle_stations = [
            OrderedDict({
                '940GZZLUPAC': 'Paddington',
                '940GZZLUBWT': 'Bayswater',
                '940GZZLUNHG': 'Notting Hill Gate',
                '940GZZLUHSK': 'High Street Kensington',
                '940GZZLUGTR': 'Gloucester Road',
                '940GZZLUSKS': 'South Kensington',
                '940GZZLUSSQ': 'Sloane Square',
                '940GZZLUVIC': 'Victoria',
                '940GZZLUSJP': "St. James's Park",
                '940GZZLUWSM': 'Westminster',
                '940GZZLUEMB': 'Embankment',
                '940GZZLUTMP': 'Temple',
                '940GZZLUBKF': 'Blackfriars',
                '940GZZLUMSH': 'Mansion House',
                '940GZZLUCST': 'Cannon Street',
                '940GZZLUMMT': 'Monument',
                '940GZZLUTWH': 'Tower Hill',
                '940GZZLUALD': 'Aldgate',
                '940GZZLULVT': 'Liverpool Street',
                '940GZZLUMGT': 'Moorgate',
                '940GZZLUBBN': 'Barbican',
                '940GZZLUFCN': 'Farringdon',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLUESQ': 'Euston Square',
                '940GZZLUGPS': 'Great Portland Street',
                '940GZZLUBST': 'Baker Street',
                '940GZZLUERC': 'Edgware Road (Circle Line)',
            }),
            OrderedDict({
                '940GZZLUPAH': 'Paddington',
                '940GZZLUERC': 'Edgware Road (Circle Line)',
                }),
            OrderedDict({
                '940GZZLUERC': 'Edgware Road (Circle Line)',
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLURYO': 'Royal Oak',
                '940GZZLUWSP': 'Westbourne Park',
                '940GZZLULAD': 'Ladbroke Grove',
                '940GZZLULRD': 'Latimer Road',
                '940GZZLUWLA': 'Wood Lane',
                '940GZZLUSBM': "Shepherd's Bush Market",
                '940GZZLUGHK': 'Goldhawk Road',
                '940GZZLUHSC': 'Hammersmith (H&C Line)',
                })
            ]

        self.district_stations = [
            OrderedDict({
                '940GZZLUUPM': 'Upminster',
                '940GZZLUUPB': 'Upminster Bridge',
                '940GZZLUHCH': 'Hornchurch',
                '940GZZLUEPK': 'Elm Park',
                '940GZZLUDGE': 'Dagenham East',
                '940GZZLUDGY': 'Dagenham Heathway',
                '940GZZLUBEC': 'Becontree',
                '940GZZLUUPY': 'Upney',
                '940GZZLUBKG': 'Barking',
                '940GZZLUEHM': 'East Ham',
                '940GZZLUUPK': 'Upton Park',
                '940GZZLUPLW': 'Plaistow',
                '940GZZLUWHM': 'West Ham',
                '940GZZLUBBB': 'Bromley-by-Bow',
                '940GZZLUBWR': 'Bow Road',
                '940GZZLUMED': 'Mile End',
                '940GZZLUSGN': 'Stepney Green',
                '940GZZLUWPL': 'Whitechapel',
                '940GZZLUADE': 'Aldgate East',
                '940GZZLUTWH': 'Tower Hill',
                '940GZZLUMMT': 'Monument',
                '940GZZLUCST': 'Cannon Street',
                '940GZZLUMSH': 'Mansion House',
                '940GZZLUBKF': 'Blackfriars',
                '940GZZLUTMP': 'Temple',
                '940GZZLUEMB': 'Embankment',
                '940GZZLUWSM': 'Westminster',
                '940GZZLUSJP': "St Jamess Park",
                '940GZZLUVIC': 'Victoria',
                '940GZZLUSSQ': 'Sloane Square',
                '940GZZLUSKS': 'South Kensington',
                '940GZZLUGTR': 'Gloucester Road',
                '940GZZLUECT': "Earls Court",
                }),
            OrderedDict({
                '940GZZLUECT': "Earls Court",
                '940GZZLUWKN': 'West Kensington',
                '940GZZLUBSC': 'Barons Court',
                '940GZZLUHSD': 'Hammersmith',
                '940GZZLURVP': 'Ravenscourt Park',
                '940GZZLUSFB': 'Stamford Brook',
                '940GZZLUTNG': 'Turnham Green',
                '940GZZLUCWP': 'Chiswick Park',
                '940GZZLUACT': 'Acton Town',
                '940GZZLUECM': 'Ealing Common',
                '940GZZLUEBY': 'Ealing Broadway',
                }),
            OrderedDict({
                '940GZZLUTNG': 'Turnham Green',
                '940GZZLUGBY': 'Gunnersbury',
                '940GZZLUKWG': 'Kew Gardens',
                '940GZZLURMD': 'Richmond',
                }),
            OrderedDict({
                '940GZZLUECT': "Earls Court",
                '940GZZLUWBN': 'West Brompton',
                '940GZZLUFBY': 'Fulham Broadway',
                '940GZZLUPSG': 'Parsons Green',
                '940GZZLUPYB': 'Putney Bridge',
                '940GZZLUEPY': 'East Putney',
                '940GZZLUSFS': 'Southfields',
                '940GZZLUWIP': 'Wimbledon Park',
                '940GZZLUWIM': 'Wimbledon',
                }),
            OrderedDict({
                '940GZZLUERC': 'Edgware Road',
                '940GZZLUPAC': 'Paddington',
                '940GZZLUBWT': 'Bayswater',
                '940GZZLUNHG': 'Notting Hill Gate',
                '940GZZLUHSK': 'High Street Kensington',
                '940GZZLUECT': "Earls Court",
                }),
            OrderedDict({
                '940GZZLUECT': "Earls Court",
                '940GZZLUKOY': 'Kensington Olympia',
                })
            ]

        self.hammersmith_city_stations = [OrderedDict({
                '940GZZLUBKG': 'Barking',
                '940GZZLUEHM': 'East Ham',
                '940GZZLUUPK': 'Upton Park',
                '940GZZLUPLW': 'Plaistow',
                '940GZZLUWHM': 'West Ham',
                '940GZZLUBBB': 'Bromley-by-Bow',
                '940GZZLUBWR': 'Bow Road',
                '940GZZLUMED': 'Mile End',
                '940GZZLUSGN': 'Stepney Green',
                '940GZZLUWPL': 'Whitechapel',
                '940GZZLUADE': 'Aldgate East',
                '940GZZLULVT': 'Liverpool Street',
                '940GZZLUMGT': 'Moorgate',
                '940GZZLUBBN': 'Barbican',
                '940GZZLUFCN': 'Farringdon',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLUESQ': 'Euston Square',
                '940GZZLUGPS': 'Great Portland Street',
                '940GZZLUBST': 'Baker Street',
                '940GZZLUERC': 'Edgware Road (Circle Line)',
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLURYO': 'Royal Oak',
                '940GZZLUWSP': 'Westbourne Park',
                '940GZZLULAD': 'Ladbroke Grove',
                '940GZZLULRD': 'Latimer Road',
                '940GZZLUWLA': 'Wood Lane',
                '940GZZLUSBM': "Shepherd's Bush Market",
                '940GZZLUGHK': 'Goldhawk Road',
                '940GZZLUHSC': 'Hammersmith (H&C Line)'
                })]

        self.jubilee_stations = [OrderedDict({
                '940GZZLUSTD': 'Stratford',
                '940GZZLUWHM': 'West Ham',
                '940GZZLUCGT': 'Canning Town',
                '940GZZLUNGW': 'North Greenwich',
                '940GZZLUCYF': 'Canary Wharf',
                '940GZZLUCWR': 'Canada Water',
                '940GZZLUBMY': 'Bermondsey',
                '940GZZLULNB': 'London Bridge',
                '940GZZLUSWK': 'Southwark',
                '940GZZLUWLO': 'Waterloo',
                '940GZZLUWSM': 'Westminster',
                '940GZZLUGPK': 'Green Park',
                '940GZZLUBND': 'Bond Street',
                '940GZZLUBST': 'Baker Street',
                '940GZZLUSJW': "St. John's Wood",
                '940GZZLUSWC': 'Swiss Cottage',
                '940GZZLUFYR': 'Finchley Road',
                '940GZZLUWHP': 'West Hampstead',
                '940GZZLUKBN': 'Kilburn',
                '940GZZLUWIG': 'Willesden Green',
                '940GZZLUDOH': 'Dollis Hill',
                '940GZZLUNDN': 'Neasden',
                '940GZZLUWYP': 'Wembley Park',
                '940GZZLUKBY': 'Kingsbury',
                '940GZZLUQBY': 'Queensbury',
                '940GZZLUCPK': 'Canons Park',
                '940GZZLUSTM': 'Stanmore'
                 })]

        self.metropolitan_stations = [
            OrderedDict({
                '940GZZLUALD': 'Aldgate',
                '940GZZLULVT': 'Liverpool Street',
                '940GZZLUMGT': 'Moorgate',
                '940GZZLUBBN': 'Barbican',
                '940GZZLUFCN': 'Farringdon',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLUESQ': 'Euston Square',
                '940GZZLUGPS': 'Great Portland Street',
                '940GZZLUBST': 'Baker Street',
                '940GZZLUFYR': 'Finchley Road',
                '940GZZLUWYP': 'Wembley Park',
                '940GZZLUPRD': 'Preston Road',
                '940GZZLUNKP': 'Northwick Park',
                '940GZZLUHOH': 'Harrow-on-the-Hill',
                '940GZZLUNHA': 'North Harrow',
                '940GZZLUPNR': 'Pinner',
                '940GZZLUNWH': 'Northwood Hills',
                '940GZZLUNOW': 'Northwood',
                '940GZZLUMPK': 'Moor Park',
                '940GZZLURKW': 'Rickmansworth',
                '940GZZLUCYD': 'Chorleywood',
                '940GZZLUCAL': 'Chalfont & Latimer',
                '940GZZLUAMS': 'Amersham',
                }),
            OrderedDict({
                '940GZZLUHOH': 'Harrow-on-the-Hill',
                '940GZZLUWHW': 'West Harrow',
                '940GZZLURYL': 'Rayners Lane',
                '940GZZLUEAE': 'Eastcote',
                '940GZZLURSM': 'Ruislip Manor',
                '940GZZLURSP': 'Ruislip',
                '940GZZLUICK': 'Ickenham',
                '940GZZLUHGD': 'Hillingdon',
                '940GZZLUUXB': 'Uxbridge',
                }),
            OrderedDict({
                '940GZZLUCSM': 'Chesham',
                '940GZZLUCAL': 'Chalfont & Latimer',
                }),
            OrderedDict({
                '940GZZLUMPK': 'Moor Park',
                '940GZZLUCXY': 'Croxley',
                '940GZZLUWAF': 'Watford'
                })
            ]

        self.northern_stations = [
            OrderedDict({
                '940GZZLUHBT': 'High Barnet',
                '940GZZLUTAW': 'Totteridge & Whetstone',
                '940GZZLUWOP': 'Woodside Park',
                '940GZZLUWFN': 'West Finchley',
                '940GZZLUFYC': 'Finchley Central',
                '940GZZLUEFY': 'East Finchley',
                '940GZZLUHGT': 'Highgate',
                '940GZZLUACY': 'Archway',
                '940GZZLUTFP': 'Tufnell Park',
                '940GZZLUKSH': 'Kentish Town',
                '940GZZLUCTN': 'Camden Town',
                '940GZZLUMTC': 'Mornington Crescent',
                '940GZZLUEUS': 'Euston',
                '940GZZLUWRR': 'Warren Street',
                '940GZZLUGDG': 'Goodge Street',
                '940GZZLUTCR': 'Tottenham Court Road',
                '940GZZLULSQ': 'Leicester Square',
                '940GZZLUCHX': 'Charing Cross',
                '940GZZLUEMB': 'Embankment',
                '940GZZLUWLO': 'Waterloo',
                '940GZZLUKNG': 'Kennington',
                '940GZZLUOVL': 'Oval',
                '940GZZLUSKW': 'Stockwell',
                '940GZZLUCPN': 'Clapham North',
                '940GZZLUCPC': 'Clapham Common',
                '940GZZLUCPS': 'Clapham South',
                '940GZZLUBLM': 'Balham',
                '940GZZLUTBC': 'Tooting Bec',
                '940GZZLUTBY': 'Tooting Broadway',
                '940GZZLUCSD': 'Colliers Wood',
                '940GZZLUSWN': 'South Wimbledon',
                '940GZZLUMDN': 'Morden',
                }),
            OrderedDict({
                '940GZZLUEUS': 'Euston',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLUAGL': 'Angel',
                '940GZZLUODS': 'Old Street',
                '940GZZLUMGT': 'Moorgate',
                '940GZZLUBNK': 'Bank',
                '940GZZLULNB': 'London Bridge',
                '940GZZLUBOR': 'Borough',
                '940GZZLUEAC': 'Elephant & Castle',
                '940GZZLUKNG': 'Kennington',
                }),
            OrderedDict({
                '940GZZLUEGW': 'Edgware',
                '940GZZLUBTK': 'Burnt Oak',
                '940GZZLUCND': 'Colindale',
                '940GZZLUHCL': 'Hendon Central',
                '940GZZLUBTX': 'Brent Cross',
                '940GZZLUGGN': 'Golders Green',
                '940GZZLUHTD': 'Hampstead',
                '940GZZLUBZP': 'Belsize Park',
                '940GZZLUCFM': 'Chalk Farm',
                '940GZZLUCTN': 'Camden Town',
                }),
            OrderedDict({
                '940GZZLUFYC': 'Finchley Central',
                '940GZZLUMHL': 'Mill Hill East',
                }),
            OrderedDict({
                '940GZZLUKNG': 'Kennington',
                '940GZZNEUGST': 'Nine Elms',
                '940GZZBPSUST': 'Battersea Power Station',
                })
            ]

        self.piccadilly_stations = [
            OrderedDict({
                '940GZZLUCKS': 'Cockfosters',
                '940GZZLUOAK': 'Oakwood',
                '940GZZLUSGT': 'Southgate',
                '940GZZLUASG': 'Arnos Grove',
                '940GZZLUBDS': 'Bounds Green',
                '940GZZLUWOG': 'Wood Green',
                '940GZZLUTPN': 'Turnpike Lane',
                '940GZZLUMRH': 'Manor House',
                '940GZZLUFPK': 'Finsbury Park',
                '940GZZLUASL': 'Arsenal',
                '940GZZLUHWY': 'Holloway Road',
                '940GZZLUCAR': 'Caledonian Road',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLURSQ': 'Russell Square',
                '940GZZLUHBN': 'Holborn',
                '940GZZLUCGN': 'Covent Garden',
                '940GZZLULSQ': 'Leicester Square',
                '940GZZLUPCC': 'Piccadilly Circus',
                '940GZZLUGPK': 'Green Park',
                '940GZZLUHPC': 'Hyde Park Corner',
                '940GZZLUKNB': 'Knightsbridge',
                '940GZZLUSKS': 'South Kensington',
                '940GZZLUGTR': 'Gloucester Road',
                '940GZZLUECT': "Earl's Court",
                '940GZZLUBSC': 'Barons Court',
                '940GZZLUHSD': 'Hammersmith (Dist&Picc Line)',
                '940GZZLUTNG': 'Turnham Green',
                '940GZZLUACT': 'Acton Town',
                '940GZZLUECM': 'Ealing Common',
                '940GZZLUNEN': 'North Ealing',
                '940GZZLUPKR': 'Park Royal',
                '940GZZLUALP': 'Alperton',
                '940GZZLUSUT': 'Sudbury Town',
                '940GZZLUSUH': 'Sudbury Hill',
                '940GZZLUSHH': 'South Harrow',
                '940GZZLURYL': 'Rayners Lane',
                '940GZZLUEAE': 'Eastcote',
                '940GZZLURSM': 'Ruislip Manor',
                '940GZZLURSP': 'Ruislip',
                '940GZZLUICK': 'Ickenham',
                '940GZZLUHGD': 'Hillingdon',
                '940GZZLUUXB': 'Uxbridge',
                }),
            OrderedDict({
                '940GZZLUACT': 'Acton Town',
                '940GZZLUSEA': 'South Ealing',
                '940GZZLUNFD': 'Northfields',
                '940GZZLUBOS': 'Boston Manor',
                '940GZZLUOSY': 'Osterley',
                '940GZZLUHWE': 'Hounslow East',
                '940GZZLUHWC': 'Hounslow Central',
                '940GZZLUHWT': 'Hounslow West',
                '940GZZLUHNX': 'Hatton Cross',
                '940GZZLUHRC': 'Heathrow Terminals 2 & 3',
                '940GZZLUHR5': 'Heathrow Terminal 5',
                }),
            OrderedDict({
                '940GZZLUHRC': 'Heathrow Terminals 2 & 3',
                '940GZZLUHR4': 'Heathrow Terminal 4',
                '940GZZLUHNX': 'Hatton Cross',
                })
            ]

        self.victoria_stations = [OrderedDict({
                '940GZZLUWWL': 'Walthamstow Central',
                '940GZZLUBLR': 'Blackhorse Road',
                '940GZZLUTMH': 'Tottenham Hale',
                '940GZZLUSVS': 'Seven Sisters',
                '940GZZLUFPK': 'Finsbury Park',
                '940GZZLUHAI': 'Highbury & Islington',
                '940GZZLUKSX': "King's Cross St. Pancras",
                '940GZZLUEUS': 'Euston',
                '940GZZLUWRR': 'Warren Street',
                '940GZZLUOXC': 'Oxford Circus',
                '940GZZLUGPK': 'Green Park',
                '940GZZLUVIC': 'Victoria',
                '940GZZLUPCO': 'Pimlico',
                '940GZZLUVXL': 'Vauxhall',
                '940GZZLUSKW': 'Stockwell',
                '940GZZLUBXN': 'Brixton'
                })]

        self.waterloo_city_stations = [OrderedDict({
                '940GZZLUBNK': 'Bank',
                '940GZZLUWLO': 'Waterloo'
                })]

        self.elizabeth_stations = [
            OrderedDict({
                '910GHTRWTM4': 'Heathrow Terminal 4',
                '910GHTRWAPT': 'Heathrow Terminals 2 & 3',
                '910GHAYESAH': 'Hayes & Harlington',
                '910GSTHALL': 'Southall',
                '910GHANWELL': 'Hanwell',
                '910GWEALING': 'West Ealing',
                '910GEALINGB': 'Ealing Broadway',
                '910GACTONML': 'Acton Main Line',
                '910GPADTLL': 'Paddington',
                '910GBONDST': 'Bond Street',
                '910GTOTCTRD': 'Tottenham Court Road',
                '910GFRNDXR': 'Farringdon',
                '910GLIVSTLL': 'Liverpool Street',
                '910GWCHAPXR': 'Whitechapel',
                '910GCANWHRF': 'Canary Wharf',
                '910GCSTMHSXR': 'Custom House',
                '910GWOLWXR': 'Woolwich',
                '910GABWDXR': 'Abbey Wood',
                }),
            OrderedDict({
                '910GHTRWTM5': 'Heathrow Terminal 5',
                '910GHTRWAPT': 'Heathrow Terminals 2 & 3',
                }),
            OrderedDict({
                '910GLIVSTLL': 'Liverpool Street',
                '910GSTFD': 'Stratford (London)',
                '910GMRYLAND': 'Maryland',
                '910GFRSTGT': 'Forest Gate',
                '910GMANRPK': 'Manor Park',
                '910GILFORD': 'Ilford',
                '910GSVNKNGS': 'Seven Kings',
                '910GGODMAYS': 'Goodmayes',
                '910GCHDWLHT': 'Chadwell Heath',
                '910GROMFORD': 'Romford',
                '910GGIDEAPK': 'Gidea Park',
                '910GHRLDWOD': 'Harold Wood',
                '910GBRTWOOD': 'Brentwood',
                '910GSHENFLD': 'Shenfield',
                }),
            OrderedDict({
                '910GRDNGSTN': 'Reading',
                '910GTWYFORD': 'Twyford',
                '910GMDNHEAD': 'Maidenhead',
                '910GTAPLOW': 'Taplow',
                '910GBNHAM': 'Burnham (Berks)',
                '910GSLOUGH': 'Slough',
                '910GLANGLEY': 'Langley (Berks)',
                '910GIVER': 'Iver',
                '910GWDRYTON': 'West Drayton',
                '910GHAYESAH': 'Hayes & Harlington',
                })
            ]
        
        self.line_dict = {
            'bakerloo': {
                "graph": self.construct_graph(self.bakerloo_stations),
                "all_stations": {station for part in self.bakerloo_stations for _, station in part.items()},
                },
            'central':{
                "graph": self.construct_graph(self.central_stations),
                "all_stations": {station for part in self.central_stations for _, station in part.items()},
                },
            'circle':{
                "graph": self.construct_graph(self.circle_stations),
                "all_stations": {station for part in self.circle_stations for _, station in part.items()},
                },
            'district': {
                "graph": self.construct_graph(self.district_stations),
                "all_stations": {station for part in self.district_stations for _, station in part.items()},
                },
            'hammersmith-city':{
                "graph": self.construct_graph(self.hammersmith_city_stations),
                "all_stations": {station for part in self.hammersmith_city_stations for _, station in part.items()},
                },
            'jubilee':{
                "graph": self.construct_graph(self.jubilee_stations),
                "all_stations": {station for part in self.jubilee_stations for _, station in part.items()},
                },
            'metropolitan':{
                "graph": self.construct_graph(self.metropolitan_stations),
                "all_stations": {station for part in self.metropolitan_stations for _, station in part.items()},
                },
            'northern':{
                "graph": self.construct_graph(self.northern_stations),
                "all_stations": {station for part in self.northern_stations for _, station in part.items()},
                },
            'piccadilly':{
                "graph": self.construct_graph(self.piccadilly_stations),
                "all_stations": {station for part in self.piccadilly_stations for _, station in part.items()},
                },
            'victoria':{
                "graph": self.construct_graph(self.victoria_stations),
                "all_stations": {station for part in self.victoria_stations for _, station in part.items()},
                },
            'waterloo-city':{
                "graph": self.construct_graph(self.waterloo_city_stations),
                "all_stations": {station for part in self.waterloo_city_stations for _, station in part.items()},
                },
            'elizabeth':{
                "graph": self.construct_graph(self.elizabeth_stations),
                "all_stations": {station for part in self.elizabeth_stations for _, station in part.items()},
                },
            }


    @staticmethod
    def construct_graph(station_dicts: list[OrderedDict]) -> nx.Graph:
        """
        Build a nx graph representing the tube stops.

        Parameters
        ----------
        station_dicts : list
            A list of ordered dictionaries of the station IDs and names to linking the tube stops.

        Returns
        -------
        line_nx : nx.Graph
            Graph of the tube stations and connectivities.

        """
        station_ids = [list(sub_stations.values()) for sub_stations in station_dicts]
        line_nx = nx.Graph()
        
        for k, sub_line in enumerate(station_ids):
            #print(f"Line: {k}")
            for i in range(len(sub_line)-1):
                line_nx.add_edge(sub_line[i], sub_line[i+1])
                #print(f"  {station_dicts[k][sub_line[i]]} -> {station_dicts[k][sub_line[i+1]]}")
        
        #nx.draw(line_nx, with_labels=True, pos=nx.spring_layout(line_nx))
        #plt.draw()
        
        return line_nx
    
    @staticmethod
    def min_fuzzy_match(source, match_list, edits=3):
        # identify correct src / tgt from fuzzy matching
        min_word = None
        min_edits = float('inf')
        src_pattern = fr'({source}){{e<={edits}}}'
        # loop through stations to fuzzy match and find match with min edits
        for stn in match_list:
            match = regex.fullmatch(src_pattern, stn)
            if match:
                n_edits = sum(match.fuzzy_counts)
                if n_edits < min_edits:
                    min_edits = n_edits
                    min_word = stn
        return min_word

    def shortest_path_nodes(self, line, source, target):
        # create matching list without punctuation
        match_list = self.line_dict[line]["all_stations"]
        match_list = [i.translate(str.maketrans('', '', string.punctuation)).strip() for i in match_list]
        # ensure source and target have no punctuation for comparison
        source = source.translate(str.maketrans('', '', string.punctuation)).strip()
        target = target.translate(str.maketrans('', '', string.punctuation)).strip()
        # check against minimum edits in fuzzy matching
        src_station = self.min_fuzzy_match(source, match_list)
        tgt_station = self.min_fuzzy_match(target, match_list)
        print(f"Source: {source} -> {src_station}")
        print(f"Target: {target} -> {tgt_station}")

        return nx.shortest_path(self.line_dict[line]["graph"], src_station, tgt_station)



if __name__ == "__main__":
    tg = tubeGraphs()
    nx.draw(tg.line_dict["district"]["graph"], with_labels=True, pos=nx.spring_layout(tg.line_dict["district"]["graph"]))
    print(tg.line_dict["district"]["graph"].nodes)
    print(tg.shortest_path_nodes("district", "Earl's Court", "Ealing Broadway "))
    plt.draw()

