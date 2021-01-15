import json
from os import stat

# Assigning the station code into a variable after opening csv file
with open('stations.csv') as file1: 
    headers = file1.readline()
    stations = []
    for line in file1: 
        location, state, code = line.strip().split(',')
        stations.append({'Location': location, 'State': state, 'Station code': code})
    station_code = []
    for i in range(len(stations)):
        station_code.append(stations[i]['Station code'])

# Opening json file 
with open ('precipitation.json') as file:
    precipitation = json.load(file)

counter = 0 
for area_code in station_code:
    counter +=1
# Selecting the precipitation values of the area for the whole year.
    Area_prec = []
    for i in range(len(precipitation)):
        if precipitation[i]['station'] == area_code:
            data = f"{precipitation[i]['date']}-{precipitation[i]['value']}"
            year, month, day, value = data.strip().split('-')
            Area_prec.append({'year': year, 'month': month, 'day': day, 'value': int(value)})

# Summing the values for each month and putting them into dictionary.
    Area_prec_monthly = {}
    for i in range(len(Area_prec)):
        month = Area_prec[i]['month']
        value = Area_prec[i]['value']
        if not month in Area_prec_monthly.keys():
            Area_prec_monthly[month] = 0 
        Area_prec_monthly[month] += value
# Calculating the total precipitation value of Seattle for the whole year.
    total_prec = 0
    for i in range(len(Area_prec)):
        total_prec += Area_prec[i]['value']
    print(f'Total precipitation in {area_code} for the whole year = {total_prec}')
# Calculating relative precipitation per month in percentage.
    rel_prec = {key: int((Seattle_prec_monthly[key]/total_prec)*100) for key in Seattle_prec_monthly.keys()}
    print(f'Relative percentage comparing the precipitation of each month: {rel_prec}')
# Saving the file in json format
    with open(f'Location{counter}.json', 'w') as file: 
        json.dump(Area_prec_monthly, file, indent= 4)




