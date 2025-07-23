#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 22:36:02 2025

@author: Maxgamill
"""
from collections import OrderedDict

import networkx as nx
import matplotlib.pyplot as plt
import requests
import pandas as pd


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
    b = requests.get(f"https://api.tfl.gov.uk/Line/{line_id}/Route/Sequence/inbound").json()
    d = {}
    for seq in b["stopPointSequences"]:
        for stop in seq["stopPoint"]:
            d[stop["id"]] = stop["name"]

    return d


class tubeGraphs:

    def __init__(self):
        self.bakerloo_stations = [OrderedDict({
            '940GZZLUHAW': 'Harrow & Wealdstone Underground Station',
            '940GZZLUKEN': 'Kenton Underground Station',
            '940GZZLUSKT': 'South Kenton Underground Station',
            '940GZZLUNWY': 'North Wembley Underground Station',
            '940GZZLUWYC': 'Wembley Central Underground Station',
            '940GZZLUSGP': 'Stonebridge Park Underground Station',
            '940GZZLUHSN': 'Harlesden Underground Station',
            '940GZZLUWJN': 'Willesden Junction Underground Station',
            '940GZZLUKSL': 'Kensal Green Underground Station',
            '940GZZLUQPS': "Queen's Park Underground Station",
            '940GZZLUKPK': 'Kilburn Park Underground Station',
            '940GZZLUMVL': 'Maida Vale Underground Station',
            '940GZZLUWKA': 'Warwick Avenue Underground Station',
            '940GZZLUPAC': 'Paddington Underground Station',
            '940GZZLUERB': 'Edgware Road (Bakerloo) Underground Station',
            '940GZZLUMYB': 'Marylebone Underground Station',
            '940GZZLUBST': 'Baker Street Underground Station',
            '940GZZLURGP': "Regent's Park Underground Station",
            '940GZZLUOXC': 'Oxford Circus Underground Station',
            '940GZZLUPCC': 'Piccadilly Circus Underground Station',
            '940GZZLUCHX': 'Charing Cross Underground Station',
            '940GZZLUEMB': 'Embankment Underground Station',
            '940GZZLUWLO': 'Waterloo Underground Station',
            '940GZZLULBN': 'Lambeth North Underground Station',
            '940GZZLUEAC': 'Elephant & Castle Underground Station'
            })]

        self.central_stations = [
            OrderedDict({
                '940GZZLUEPG': 'Epping Underground Station',
                '940GZZLUTHB': 'Theydon Bois Underground Station',
                '940GZZLUDBN': 'Debden Underground Station',
                '940GZZLULGN': 'Loughton Underground Station',
                '940GZZLUBKH': 'Buckhurst Hill Underground Station',
                '940GZZLUWOF': 'Woodford Underground Station',
                '940GZZLUSWF': 'South Woodford Underground Station',
                '940GZZLUSNB': 'Snaresbrook Underground Station',
                '940GZZLULYS': 'Leytonstone Underground Station',
                '940GZZLULYN': 'Leyton Underground Station',
                '940GZZLUSTD': 'Stratford Underground Station',
                '940GZZLUMED': 'Mile End Underground Station',
                '940GZZLUBLG': 'Bethnal Green Underground Station',
                '940GZZLULVT': 'Liverpool Street Underground Station',
                '940GZZLUBNK': 'Bank Underground Station',
                '940GZZLUSPU': "St. Paul's Underground Station",
                '940GZZLUCHL': 'Chancery Lane Underground Station',
                '940GZZLUHBN': 'Holborn Underground Station',
                '940GZZLUTCR': 'Tottenham Court Road Underground Station',
                '940GZZLUOXC': 'Oxford Circus Underground Station',
                '940GZZLUBND': 'Bond Street Underground Station',
                '940GZZLUMBA': 'Marble Arch Underground Station',
                '940GZZLULGT': 'Lancaster Gate Underground Station',
                '940GZZLUQWY': 'Queensway Underground Station',
                '940GZZLUNHG': 'Notting Hill Gate Underground Station',
                '940GZZLUHPK': 'Holland Park Underground Station',
                '940GZZLUSBC': "Shepherd's Bush (Central) Underground Station",
                '940GZZLUWCY': 'White City Underground Station',
                '940GZZLUEAN': 'East Acton Underground Station',
                '940GZZLUNAN': 'North Acton Underground Station',
                '940GZZLUHGR': 'Hanger Lane Underground Station',
                '940GZZLUPVL': 'Perivale Underground Station',
                '940GZZLUGFD': 'Greenford Underground Station',
                '940GZZLUNHT': 'Northolt Underground Station',
                '940GZZLUSRP': 'South Ruislip Underground Station',
                '940GZZLURSG': 'Ruislip Gardens Underground Station',
                '940GZZLUWRP': 'West Ruislip Underground Station',

            }),
            OrderedDict({
                '940GZZLUEBY': 'Ealing Broadway Underground Station',
                '940GZZLUWTA': 'West Acton Underground Station',
                '940GZZLUNAN': 'North Acton Underground Station',
                }),
            OrderedDict({
                '940GZZLULYS': 'Leytonstone Underground Station',
                '940GZZLUWSD': 'Wanstead Underground Station',
                '940GZZLURBG': 'Redbridge Underground Station',
                '940GZZLUGTH': 'Gants Hill Underground Station',
                '940GZZLUBKE': 'Barkingside Underground Station',
                '940GZZLUNBP': 'Newbury Park Underground Station',
                '940GZZLUFLP': 'Fairlop Underground Station',
                '940GZZLUHLT': 'Hainault Underground Station',
                '940GZZLUGGH': 'Grange Hill Underground Station',
                '940GZZLUCWL': 'Chigwell Underground Station',
                '940GZZLURVY': 'Roding Valley Underground Station',
                '940GZZLUWOF': 'Woodford Underground Station',
                })
            
            ]

        self.circle_stations = [
            OrderedDict({
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLUPAC': 'Paddington Underground Station',
                '940GZZLUBWT': 'Bayswater Underground Station',
                '940GZZLUNHG': 'Notting Hill Gate Underground Station',
                '940GZZLUHSK': 'High Street Kensington Underground Station',
                '940GZZLUGTR': 'Gloucester Road Underground Station',
                '940GZZLUSKS': 'South Kensington Underground Station',
                '940GZZLUSSQ': 'Sloane Square Underground Station',
                '940GZZLUVIC': 'Victoria Underground Station',
                '940GZZLUSJP': "St. James's Park Underground Station",
                '940GZZLUWSM': 'Westminster Underground Station',
                '940GZZLUEMB': 'Embankment Underground Station',
                '940GZZLUTMP': 'Temple Underground Station',
                '940GZZLUBKF': 'Blackfriars Underground Station',
                '940GZZLUMSH': 'Mansion House Underground Station',
                '940GZZLUCST': 'Cannon Street Underground Station',
                '940GZZLUMMT': 'Monument Underground Station',
                '940GZZLUTWH': 'Tower Hill Underground Station',
                '940GZZLUALD': 'Aldgate Underground Station',
                '940GZZLULVT': 'Liverpool Street Underground Station',
                '940GZZLUMGT': 'Moorgate Underground Station',
                '940GZZLUBBN': 'Barbican Underground Station',
                '940GZZLUFCN': 'Farringdon Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLUESQ': 'Euston Square Underground Station',
                '940GZZLUGPS': 'Great Portland Street Underground Station',
                '940GZZLUBST': 'Baker Street Underground Station',
                '940GZZLUERC': 'Edgware Road (Circle Line) Underground Station',
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
            }),
            OrderedDict({
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLUERC': 'Edgware Road (Circle Line) Underground Station',
                }),
            OrderedDict({
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLURYO': 'Royal Oak Underground Station',
                '940GZZLUWSP': 'Westbourne Park Underground Station',
                '940GZZLULAD': 'Ladbroke Grove Underground Station',
                '940GZZLULRD': 'Latimer Road Underground Station',
                '940GZZLUWLA': 'Wood Lane Underground Station',
                '940GZZLUSBM': "Shepherd's Bush Market Underground Station",
                '940GZZLUGHK': 'Goldhawk Road Underground Station',
                '940GZZLUHSC': 'Hammersmith (H&C Line) Underground Station',
                })
            ]

        self.district_stations = [
            OrderedDict({
                '940GZZLUUPM': 'Upminster Underground Station',
                '940GZZLUUPB': 'Upminster Bridge Underground Station',
                '940GZZLUHCH': 'Hornchurch Underground Station',
                '940GZZLUEPK': 'Elm Park Underground Station',
                '940GZZLUDGE': 'Dagenham East Underground Station',
                '940GZZLUDGY': 'Dagenham Heathway Underground Station',
                '940GZZLUBEC': 'Becontree Underground Station',
                '940GZZLUUPY': 'Upney Underground Station',
                '940GZZLUBKG': 'Barking Underground Station',
                '940GZZLUEHM': 'East Ham Underground Station',
                '940GZZLUUPK': 'Upton Park Underground Station',
                '940GZZLUPLW': 'Plaistow Underground Station',
                '940GZZLUWHM': 'West Ham Underground Station',
                '940GZZLUBBB': 'Bromley-by-Bow Underground Station',
                '940GZZLUBWR': 'Bow Road Underground Station',
                '940GZZLUMED': 'Mile End Underground Station',
                '940GZZLUSGN': 'Stepney Green Underground Station',
                '940GZZLUWPL': 'Whitechapel Underground Station',
                '940GZZLUADE': 'Aldgate East Underground Station',
                '940GZZLUTWH': 'Tower Hill Underground Station',
                '940GZZLUMMT': 'Monument Underground Station',
                '940GZZLUCST': 'Cannon Street Underground Station',
                '940GZZLUMSH': 'Mansion House Underground Station',
                '940GZZLUBKF': 'Blackfriars Underground Station',
                '940GZZLUTMP': 'Temple Underground Station',
                '940GZZLUEMB': 'Embankment Underground Station',
                '940GZZLUWSM': 'Westminster Underground Station',
                '940GZZLUSJP': "St. James's Park Underground Station",
                '940GZZLUVIC': 'Victoria Underground Station',
                '940GZZLUSSQ': 'Sloane Square Underground Station',
                '940GZZLUSKS': 'South Kensington Underground Station',
                '940GZZLUGTR': 'Gloucester Road Underground Station',
                '940GZZLUECT': "Earl's Court Underground Station",
                }),
            OrderedDict({
                '940GZZLUECT': "Earl's Court Underground Station",
                '940GZZLUWKN': 'West Kensington Underground Station',
                '940GZZLUBSC': 'Barons Court Underground Station',
                '940GZZLUHSD': 'Hammersmith (Dist&Picc Line) Underground Station',
                '940GZZLURVP': 'Ravenscourt Park Underground Station',
                '940GZZLUSFB': 'Stamford Brook Underground Station',
                '940GZZLUTNG': 'Turnham Green Underground Station',
                '940GZZLUCWP': 'Chiswick Park Underground Station',
                '940GZZLUACT': 'Acton Town Underground Station',
                '940GZZLUECM': 'Ealing Common Underground Station',
                '940GZZLUEBY': 'Ealing Broadway Underground Station',
                }),
            OrderedDict({
                '940GZZLUTNG': 'Turnham Green Underground Station',
                '940GZZLUGBY': 'Gunnersbury Underground Station',
                '940GZZLUKWG': 'Kew Gardens Underground Station',
                '940GZZLURMD': 'Richmond Underground Station',
                }),
            OrderedDict({
                '940GZZLUECT': "Earl's Court Underground Station",
                '940GZZLUWBN': 'West Brompton Underground Station',
                '940GZZLUFBY': 'Fulham Broadway Underground Station',
                '940GZZLUPSG': 'Parsons Green Underground Station',
                '940GZZLUPYB': 'Putney Bridge Underground Station',
                '940GZZLUEPY': 'East Putney Underground Station',
                '940GZZLUSFS': 'Southfields Underground Station',
                '940GZZLUWIP': 'Wimbledon Park Underground Station',
                '940GZZLUWIM': 'Wimbledon Underground Station',
                }),
            OrderedDict({
                '940GZZLUERC': 'Edgware Road (Circle Line) Underground Station',
                '940GZZLUPAC': 'Paddington Underground Station',
                '940GZZLUBWT': 'Bayswater Underground Station',
                '940GZZLUNHG': 'Notting Hill Gate Underground Station',
                '940GZZLUHSK': 'High Street Kensington Underground Station',
                '940GZZLUECT': "Earl's Court Underground Station",
                }),
            OrderedDict({
                '940GZZLUECT': "Earl's Court Underground Station",
                '940GZZLUKOY': 'Kensington (Olympia) Underground Station',
                })    
            ]

        self.hammersmith_city_stations = [OrderedDict({
                '940GZZLUBKG': 'Barking Underground Station',
                '940GZZLUEHM': 'East Ham Underground Station',
                '940GZZLUUPK': 'Upton Park Underground Station',
                '940GZZLUPLW': 'Plaistow Underground Station',
                '940GZZLUWHM': 'West Ham Underground Station',
                '940GZZLUBBB': 'Bromley-by-Bow Underground Station',
                '940GZZLUBWR': 'Bow Road Underground Station',
                '940GZZLUMED': 'Mile End Underground Station',
                '940GZZLUSGN': 'Stepney Green Underground Station',
                '940GZZLUWPL': 'Whitechapel Underground Station',
                '940GZZLUADE': 'Aldgate East Underground Station',
                '940GZZLULVT': 'Liverpool Street Underground Station',
                '940GZZLUMGT': 'Moorgate Underground Station',
                '940GZZLUBBN': 'Barbican Underground Station',
                '940GZZLUFCN': 'Farringdon Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLUESQ': 'Euston Square Underground Station',
                '940GZZLUGPS': 'Great Portland Street Underground Station',
                '940GZZLUBST': 'Baker Street Underground Station',
                '940GZZLUERC': 'Edgware Road (Circle Line) Underground Station',
                '940GZZLUPAH': 'Paddington (H&C Line)-Underground',
                '940GZZLURYO': 'Royal Oak Underground Station',
                '940GZZLUWSP': 'Westbourne Park Underground Station',
                '940GZZLULAD': 'Ladbroke Grove Underground Station',
                '940GZZLULRD': 'Latimer Road Underground Station',
                '940GZZLUWLA': 'Wood Lane Underground Station',
                '940GZZLUSBM': "Shepherd's Bush Market Underground Station",
                '940GZZLUGHK': 'Goldhawk Road Underground Station',
                '940GZZLUHSC': 'Hammersmith (H&C Line) Underground Station'
                })]

        self.jubilee_stations = [OrderedDict({
                '940GZZLUSTD': 'Stratford Underground Station',
                '940GZZLUWHM': 'West Ham Underground Station',
                '940GZZLUCGT': 'Canning Town Underground Station',
                '940GZZLUNGW': 'North Greenwich Underground Station',
                '940GZZLUCYF': 'Canary Wharf Underground Station',
                '940GZZLUCWR': 'Canada Water Underground Station',
                '940GZZLUBMY': 'Bermondsey Underground Station',
                '940GZZLULNB': 'London Bridge Underground Station',
                '940GZZLUSWK': 'Southwark Underground Station',
                '940GZZLUWLO': 'Waterloo Underground Station',
                '940GZZLUWSM': 'Westminster Underground Station',
                '940GZZLUGPK': 'Green Park Underground Station',
                '940GZZLUBND': 'Bond Street Underground Station',
                '940GZZLUBST': 'Baker Street Underground Station',
                '940GZZLUSJW': "St. John's Wood Underground Station",
                '940GZZLUSWC': 'Swiss Cottage Underground Station',
                '940GZZLUFYR': 'Finchley Road Underground Station',
                '940GZZLUWHP': 'West Hampstead Underground Station',
                '940GZZLUKBN': 'Kilburn Underground Station',
                '940GZZLUWIG': 'Willesden Green Underground Station',
                '940GZZLUDOH': 'Dollis Hill Underground Station',
                '940GZZLUNDN': 'Neasden Underground Station',
                '940GZZLUWYP': 'Wembley Park Underground Station',
                '940GZZLUKBY': 'Kingsbury Underground Station',
                '940GZZLUQBY': 'Queensbury Underground Station',
                '940GZZLUCPK': 'Canons Park Underground Station',
                '940GZZLUSTM': 'Stanmore Underground Station'
                 })]

        self.metropolitan_stations = [
            OrderedDict({
                '940GZZLUALD': 'Aldgate Underground Station',
                '940GZZLULVT': 'Liverpool Street Underground Station',
                '940GZZLUMGT': 'Moorgate Underground Station',
                '940GZZLUBBN': 'Barbican Underground Station',
                '940GZZLUFCN': 'Farringdon Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLUESQ': 'Euston Square Underground Station',
                '940GZZLUGPS': 'Great Portland Street Underground Station',
                '940GZZLUBST': 'Baker Street Underground Station',
                '940GZZLUFYR': 'Finchley Road Underground Station',
                '940GZZLUWYP': 'Wembley Park Underground Station',
                '940GZZLUPRD': 'Preston Road Underground Station',
                '940GZZLUNKP': 'Northwick Park Underground Station',
                '940GZZLUHOH': 'Harrow-on-the-Hill Underground Station',
                }),
            OrderedDict({
                '940GZZLUHOH': 'Harrow-on-the-Hill Underground Station',
                '940GZZLUWHW': 'West Harrow Underground Station',
                '940GZZLURYL': 'Rayners Lane Underground Station',
                '940GZZLUEAE': 'Eastcote Underground Station',
                '940GZZLURSM': 'Ruislip Manor Underground Station',
                '940GZZLURSP': 'Ruislip Underground Station',
                '940GZZLUICK': 'Ickenham Underground Station',
                '940GZZLUHGD': 'Hillingdon Underground Station',
                '940GZZLUUXB': 'Uxbridge Underground Station',
                }),
            OrderedDict({
                '940GZZLUHOH': 'Harrow-on-the-Hill Underground Station',
                '940GZZLUNHA': 'North Harrow Underground Station',
                '940GZZLUPNR': 'Pinner Underground Station',
                '940GZZLUNWH': 'Northwood Hills Underground Station',
                '940GZZLUNOW': 'Northwood Underground Station',
                '940GZZLUMPK': 'Moor Park Underground Station',
                '940GZZLURKW': 'Rickmansworth Underground Station',
                '940GZZLUCYD': 'Chorleywood Underground Station',
                '940GZZLUCAL': 'Chalfont & Latimer Underground Station',
                '940GZZLUAMS': 'Amersham Underground Station',
                }),
            OrderedDict({
                '940GZZLUCSM': 'Chesham Underground Station',
                '940GZZLUCAL': 'Chalfont & Latimer Underground Station',
                }),
            OrderedDict({
                '940GZZLUMPK': 'Moor Park Underground Station',
                '940GZZLUCXY': 'Croxley Underground Station',
                '940GZZLUWAF': 'Watford Underground Station'
                })
            ]

        self.northern_stations = [
            OrderedDict({
                '940GZZLUHBT': 'High Barnet Underground Station',
                '940GZZLUTAW': 'Totteridge & Whetstone Underground Station',
                '940GZZLUWOP': 'Woodside Park Underground Station',
                '940GZZLUWFN': 'West Finchley Underground Station',
                '940GZZLUFYC': 'Finchley Central Underground Station',
                '940GZZLUEFY': 'East Finchley Underground Station',
                '940GZZLUHGT': 'Highgate Underground Station',
                '940GZZLUACY': 'Archway Underground Station',
                '940GZZLUTFP': 'Tufnell Park Underground Station',
                '940GZZLUKSH': 'Kentish Town Underground Station',
                '940GZZLUCTN': 'Camden Town Underground Station',
                '940GZZLUMTC': 'Mornington Crescent Underground Station',
                '940GZZLUEUS': 'Euston Underground Station',
                '940GZZLUWRR': 'Warren Street Underground Station',
                '940GZZLUGDG': 'Goodge Street Underground Station',
                '940GZZLUTCR': 'Tottenham Court Road Underground Station',
                '940GZZLULSQ': 'Leicester Square Underground Station',
                '940GZZLUCHX': 'Charing Cross Underground Station',
                '940GZZLUEMB': 'Embankment Underground Station',
                '940GZZLUWLO': 'Waterloo Underground Station',
                '940GZZLUKNG': 'Kennington Underground Station',
                '940GZZLUOVL': 'Oval Underground Station',
                '940GZZLUSKW': 'Stockwell Underground Station',
                '940GZZLUCPN': 'Clapham North Underground Station',
                '940GZZLUCPC': 'Clapham Common Underground Station',
                '940GZZLUCPS': 'Clapham South Underground Station',
                '940GZZLUBLM': 'Balham Underground Station',
                '940GZZLUTBC': 'Tooting Bec Underground Station',
                '940GZZLUTBY': 'Tooting Broadway Underground Station',
                '940GZZLUCSD': 'Colliers Wood Underground Station',
                '940GZZLUSWN': 'South Wimbledon Underground Station',
                '940GZZLUMDN': 'Morden Underground Station',
                }),
            OrderedDict({
                '940GZZLUEUS': 'Euston Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLUAGL': 'Angel Underground Station',
                '940GZZLUODS': 'Old Street Underground Station',
                '940GZZLUMGT': 'Moorgate Underground Station',
                '940GZZLUBNK': 'Bank Underground Station',
                '940GZZLULNB': 'London Bridge Underground Station',
                '940GZZLUBOR': 'Borough Underground Station',
                '940GZZLUEAC': 'Elephant & Castle Underground Station',
                '940GZZLUKNG': 'Kennington Underground Station',
                }),
            OrderedDict({
                '940GZZLUEGW': 'Edgware Underground Station',
                '940GZZLUBTK': 'Burnt Oak Underground Station',
                '940GZZLUCND': 'Colindale Underground Station',
                '940GZZLUHCL': 'Hendon Central Underground Station',
                '940GZZLUBTX': 'Brent Cross Underground Station',
                '940GZZLUGGN': 'Golders Green Underground Station',
                '940GZZLUHTD': 'Hampstead Underground Station',
                '940GZZLUBZP': 'Belsize Park Underground Station',
                '940GZZLUCFM': 'Chalk Farm Underground Station',
                '940GZZLUCTN': 'Camden Town Underground Station',
                }),
            OrderedDict({
                '940GZZLUFYC': 'Finchley Central Underground Station',
                '940GZZLUMHL': 'Mill Hill East Underground Station',
                }),
            OrderedDict({
                '940GZZLUKNG': 'Kennington Underground Station',
                '940GZZNEUGST': 'Nine Elms Underground Station',
                '940GZZBPSUST': 'Battersea Power Station Underground Station',
                })
            ]

        self.piccadilly_stations = [
            OrderedDict({
                '940GZZLUCKS': 'Cockfosters Underground Station',
                '940GZZLUOAK': 'Oakwood Underground Station',
                '940GZZLUSGT': 'Southgate Underground Station',
                '940GZZLUASG': 'Arnos Grove Underground Station',
                '940GZZLUBDS': 'Bounds Green Underground Station',
                '940GZZLUWOG': 'Wood Green Underground Station',
                '940GZZLUTPN': 'Turnpike Lane Underground Station',
                '940GZZLUMRH': 'Manor House Underground Station',
                '940GZZLUFPK': 'Finsbury Park Underground Station',
                '940GZZLUASL': 'Arsenal Underground Station',
                '940GZZLUHWY': 'Holloway Road Underground Station',
                '940GZZLUCAR': 'Caledonian Road Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLURSQ': 'Russell Square Underground Station',
                '940GZZLUHBN': 'Holborn Underground Station',
                '940GZZLUCGN': 'Covent Garden Underground Station',
                '940GZZLULSQ': 'Leicester Square Underground Station',
                '940GZZLUPCC': 'Piccadilly Circus Underground Station',
                '940GZZLUGPK': 'Green Park Underground Station',
                '940GZZLUHPC': 'Hyde Park Corner Underground Station',
                '940GZZLUKNB': 'Knightsbridge Underground Station',
                '940GZZLUSKS': 'South Kensington Underground Station',
                '940GZZLUGTR': 'Gloucester Road Underground Station',
                '940GZZLUECT': "Earl's Court Underground Station",
                '940GZZLUBSC': 'Barons Court Underground Station',
                '940GZZLUHSD': 'Hammersmith (Dist&Picc Line) Underground Station',
                '940GZZLUTNG': 'Turnham Green Underground Station',
                '940GZZLUACT': 'Acton Town Underground Station',
                '940GZZLUECM': 'Ealing Common Underground Station',
                '940GZZLUNEN': 'North Ealing Underground Station',
                '940GZZLUPKR': 'Park Royal Underground Station',
                '940GZZLUALP': 'Alperton Underground Station',
                '940GZZLUSUT': 'Sudbury Town Underground Station',
                '940GZZLUSUH': 'Sudbury Hill Underground Station',
                '940GZZLUSHH': 'South Harrow Underground Station',
                '940GZZLURYL': 'Rayners Lane Underground Station',
                '940GZZLUEAE': 'Eastcote Underground Station',
                '940GZZLURSM': 'Ruislip Manor Underground Station',
                '940GZZLURSP': 'Ruislip Underground Station',
                '940GZZLUICK': 'Ickenham Underground Station',
                '940GZZLUHGD': 'Hillingdon Underground Station',
                '940GZZLUUXB': 'Uxbridge Underground Station',
                }),
            OrderedDict({
                '940GZZLUACT': 'Acton Town Underground Station',
                '940GZZLUSEA': 'South Ealing Underground Station',
                '940GZZLUNFD': 'Northfields Underground Station',
                '940GZZLUBOS': 'Boston Manor Underground Station',
                '940GZZLUOSY': 'Osterley Underground Station',
                '940GZZLUHWE': 'Hounslow East Underground Station',
                '940GZZLUHWC': 'Hounslow Central Underground Station',
                '940GZZLUHWT': 'Hounslow West Underground Station',
                '940GZZLUHNX': 'Hatton Cross Underground Station',
                '940GZZLUHRC': 'Heathrow Terminals 2 & 3 Underground Station',
                '940GZZLUHR5': 'Heathrow Terminal 5 Underground Station',
                }),
            OrderedDict({
                '940GZZLUHRC': 'Heathrow Terminals 2 & 3 Underground Station',
                '940GZZLUHR4': 'Heathrow Terminal 4 Underground Station',
                '940GZZLUHNX': 'Hatton Cross Underground Station',
                })
            ]

        self.victoria_stations = [OrderedDict({
                '940GZZLUWWL': 'Walthamstow Central Underground Station',
                '940GZZLUBLR': 'Blackhorse Road Underground Station',
                '940GZZLUTMH': 'Tottenham Hale Underground Station',
                '940GZZLUSVS': 'Seven Sisters Underground Station',
                '940GZZLUFPK': 'Finsbury Park Underground Station',
                '940GZZLUHAI': 'Highbury & Islington Underground Station',
                '940GZZLUKSX': "King's Cross St. Pancras Underground Station",
                '940GZZLUEUS': 'Euston Underground Station',
                '940GZZLUWRR': 'Warren Street Underground Station',
                '940GZZLUOXC': 'Oxford Circus Underground Station',
                '940GZZLUGPK': 'Green Park Underground Station',
                '940GZZLUVIC': 'Victoria Underground Station',
                '940GZZLUPCO': 'Pimlico Underground Station',
                '940GZZLUVXL': 'Vauxhall Underground Station',
                '940GZZLUSKW': 'Stockwell Underground Station',
                '940GZZLUBXN': 'Brixton Underground Station'
                })]

        self.waterloo_city_stations = [OrderedDict({
                '940GZZLUBNK': 'Bank Underground Station',
                '940GZZLUWLO': 'Waterloo Underground Station'
                })]

        self.elizabeth_stations = [
            OrderedDict({
                '910GHTRWTM4': 'Heathrow Terminal 4 Rail Station',
                '910GHTRWAPT': 'Heathrow Terminals 2 & 3 Rail Station',
                '910GHAYESAH': 'Hayes & Harlington Rail Station',
                '910GSTHALL': 'Southall Rail Station',
                '910GHANWELL': 'Hanwell Rail Station',
                '910GWEALING': 'West Ealing Rail Station',
                '910GEALINGB': 'Ealing Broadway Rail Station',
                '910GACTONML': 'Acton Main Line Rail Station',
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
                '910GHTRWTM5': 'Heathrow Terminal 5 Rail Station',
                '910GHTRWAPT': 'Heathrow Terminals 2 & 3 Rail Station',
                }),
            OrderedDict({
                '910GLIVSTLL': 'Liverpool Street',
                '910GSTFD': 'Stratford (London) Rail Station',
                '910GMRYLAND': 'Maryland Rail Station',
                '910GFRSTGT': 'Forest Gate Rail Station',
                '910GMANRPK': 'Manor Park Rail Station',
                '910GILFORD': 'Ilford Rail Station',
                '910GSVNKNGS': 'Seven Kings Rail Station',
                '910GGODMAYS': 'Goodmayes Rail Station',
                '910GCHDWLHT': 'Chadwell Heath Rail Station',
                '910GROMFORD': 'Romford Rail Station',
                '910GGIDEAPK': 'Gidea Park Rail Station',
                '910GHRLDWOD': 'Harold Wood Rail Station',
                '910GBRTWOOD': 'Brentwood Rail Station',
                '910GSHENFLD': 'Shenfield Rail Station',
                }),
            OrderedDict({
                '910GRDNGSTN': 'Reading Rail Station',
                '910GTWYFORD': 'Twyford Rail Station',
                '910GMDNHEAD': 'Maidenhead Rail Station',
                '910GTAPLOW': 'Taplow Rail Station',
                '910GBNHAM': 'Burnham (Berks) Rail Station',
                '910GSLOUGH': 'Slough Rail Station',
                '910GLANGLEY': 'Langley (Berks) Rail Station',
                '910GIVER': 'Iver Rail Station',
                '910GWDRYTON': 'West Drayton Rail Station',
                '910GHAYESAH': 'Hayes & Harlington Rail Station',
                })
            ]
        
        self.graphs = {
            'bakerloo': self.construct_graph(self.bakerloo_stations),
            'central': self.construct_graph(self.central_stations),
            'circle': self.construct_graph(self.circle_stations),
            'district': self.construct_graph(self.district_stations),
            'hammersmith-city': self.construct_graph(self.hammersmith_city_stations),
            'jubilee': self.construct_graph(self.jubilee_stations),
            'metropolitan': self.construct_graph(self.metropolitan_stations),
            'northern': self.construct_graph(self.northern_stations),
            'piccadilly': self.construct_graph(self.piccadilly_stations),
            'victoria': self.construct_graph(self.victoria_stations),
            'waterloo-city': self.construct_graph(self.waterloo_city_stations),
            'elizabeth': self.construct_graph(self.elizabeth_stations),
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
        station_ids = [list(sub_stations.keys()) for sub_stations in station_dicts]
        line_nx = nx.Graph()    
        
        for k, sub_line in enumerate(station_ids):
            #print(f"Line: {k}")
            for i in range(len(sub_line)-1):
                line_nx.add_edge(sub_line[i], sub_line[i+1])
                #print(f"  {station_dicts[k][sub_line[i]]} -> {station_dicts[k][sub_line[i+1]]}")
        
        #nx.draw(line_nx, with_labels=True, pos=nx.spring_layout(line_nx))
        #plt.draw()
        
        return line_nx
    
    def shortest_path_nodes(self, line, source, target):
        path = nx.shortest_path(self.graphs[line], source, target)
        


class tubeDfs:
    
    def __init__(self):
        self.line_dfs = {}
        
        for line in ["bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern", "piccadilly", "victoria", "waterloo-city", "elizabeth"]:
            #stations = # get stations from station
            try:
                df = pd.read_csv(f"{line}.csv")
                self.line_dfs[line] = df
            except FileNotFoundError as e:
                print(f"{line} .csv file not found. {e}")


if __name__ == "__main__":
    tg = tubeGraphs()
    nx.draw(tg.graphs["district"], with_labels=True, pos=nx.spring_layout(tg.graphs["district"]))
    plt.draw()
    tdfs = tubeDfs()
    print(tdfs.line_dfs["district"])