#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 21:53:36 2025

@author: Maxgamill

Test the various line statuses.
"""


good = {
    '$type': 'Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities',
     'id': 'bakerloo',
     'name': 'Bakerloo',
     'modeName': 'tube',
     'disruptions': [],
     'created': '2025-06-24T15:15:34.57Z',
     'modified': '2025-06-24T15:15:34.57Z',
     'lineStatuses': [{'$type': 'Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities',
       'id': 0,
       'statusSeverity': 10,
       'statusSeverityDescription': 'Good Service',
       'created': '0001-01-01T00:00:00',
       'validityPeriods': []}],
     'routeSections': [],
     'serviceTypes': [{'$type': 'Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities',
       'name': 'Regular',
       'uri': '/Line/Route?ids=Bakerloo&serviceTypes=Regular'}],
     'crowding': {'$type': 'Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities'}
     }

severe_delay = {
    '$type': 'Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities',
     'id': 'circle',
     'name': 'Circle',
     'modeName': 'tube',
     'disruptions': [],
     'created': '2025-06-24T15:15:34.557Z',
     'modified': '2025-06-24T15:15:34.557Z',
     'lineStatuses': [{'$type': 'Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities',
       'id': 0,
       'lineId': 'circle',
       'statusSeverity': 6,
       'statusSeverityDescription': 'Severe Delays',
       'reason': 'Circle Line: Severe delays due to train cancellations. ',
       'created': '0001-01-01T00:00:00',
       'validityPeriods': [{'$type': 'Tfl.Api.Presentation.Entities.ValidityPeriod, Tfl.Api.Presentation.Entities',
         'fromDate': '2025-07-02T20:34:44Z',
         'toDate': '2025-07-03T00:29:00Z',
         'isNow': True}],
       'disruption': {'$type': 'Tfl.Api.Presentation.Entities.Disruption, Tfl.Api.Presentation.Entities',
        'category': 'RealTime',
        'categoryDescription': 'RealTime',
        'description': 'Circle Line: Severe delays due to train cancellations. ',
        'affectedRoutes': [],
        'affectedStops': [],
        'closureText': 'severeDelays'}}],
     'routeSections': [],
     'serviceTypes': [{'$type': 'Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities',
       'name': 'Regular',
       'uri': '/Line/Route?ids=Circle&serviceTypes=Regular'}],
     'crowding': {'$type': 'Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities'}
     }

weird_part_closure = {
    '$type': 'Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities',
    'id': 'district',
    'name': 'District',
    'modeName': 'tube',
    'disruptions': [],
    'created': '2025-07-15T15:56:39.177Z',
    'modified': '2025-07-15T15:56:39.177Z',
    'lineStatuses': [{'$type': 'Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities',
      'id': 0,
      'lineId': 'district',
      'statusSeverity': 5,
      'statusSeverityDescription': 'Part Closure',
      'reason': 'DISTRICT LINE: Saturday 19 and Sunday 20 July, no service between Earls Court and Ealing Broadway / Richmond. There will also be no PICCADILLY LINE service west of Kings Cross (and no Friday Night Tube on the whole line). Use MILDMAY LINE services where available between Gunnersbury, Kew Gardens and Richmond. Replacement buses operate.',
      'created': '0001-01-01T00:00:00',
      'validityPeriods': [{'$type': 'Tfl.Api.Presentation.Entities.ValidityPeriod, Tfl.Api.Presentation.Entities',
        'fromDate': '2025-07-19T03:30:00Z',
        'toDate': '2025-07-21T00:29:00Z',
        'isNow': False}],
      'disruption': {'$type': 'Tfl.Api.Presentation.Entities.Disruption, Tfl.Api.Presentation.Entities',
       'category': 'PlannedWork',
       'categoryDescription': 'PlannedWork',
       'description': 'DISTRICT LINE: Saturday 19 and Sunday 20 July, no service between Earls Court and Ealing Broadway / Richmond. There will also be no PICCADILLY LINE service west of Kings Cross (and no Friday Night Tube on the whole line). Use MILDMAY LINE services where available between Gunnersbury, Kew Gardens and Richmond. Replacement buses operate.',
       'additionalInfo': 'Replacement bus services operate:Service DL3: Early morning and late evening only when Mildmay line not running: Turnham Green - Chiswick Park - Kew Gardens (Royal Botanic Gardens) - Richmond;Service PL1: Day and Night service (the Green Park to Earls Court section only operates during Night Tube hours). Green Park - Hyde Park Corner - Knightsbridge - South Kensington - Gloucester Road - Earls Court - Hammersmith (for Barons Court) - Ravenscourt Park (day services only) - Stamford Brook (day services only) - Turnham Green - Chiswick Park (day services only) - Gunnersbury (for Mildmay line and DL3) (day services only)\xa0 - Acton Town - Ealing Common - Ealing Broadway - South Ealing - Northfields - Boston Manor - Osterley;Service PL3: Day service: Earls Court - Hammersmith - Heathrow Central Bus Station (for Terminals 2 and 3, and train connections to/from Terminal 5);Service PL4: Day service: Gunnersbury - Acton Town - Ealing Common - North Ealing - Hanger Lane (for Central line and Park Royal) - Alperton (Bridgewater Road) - Sudbury Town (Whitton Avenue East) - Sudbury Hill - South Harrow - Rayners Lane;Service PL7: Day and Night Service: Earls Court - Osterley - Hounslow East - Hounslow Central (Bell Corner) - Hounslow West - Hatton Cross - Heathrow Central Bus Station (for Terminals 2 and 3). During Night Tube hours and late on Sunday, buses also serve Heathrow Terminal 5;',
       'created': '2025-06-25T16:17:00Z',
       'affectedRoutes': [],
       'affectedStops': [],
       'closureText': 'partClosure'}}],
    'routeSections': [],
    'serviceTypes': [{'$type': 'Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities',
      'name': 'Regular',
      'uri': '/Line/Route?ids=District&serviceTypes=Regular'}],
    'crowding': {'$type': 'Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities'}
    }
