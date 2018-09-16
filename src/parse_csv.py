import csv
import sys
import json

try:
  arg_year = sys.argv[1]
except:
  arg_year = '2017'

a = dict()
scale = {0.0: '#a50026', 0.1: '#d73027', 0.2: '#f46d43', 0.3: '#fdae61', 0.4: '#fee090', 0.5: '#e0f3f8', 0.6: '#abd9e9', 0.7: '#74add1', 0.8: '#4575b4', 0.9: '#313695', 1.0: '#313695'}


with open('./data/GODT_downloads.csv', 'rt') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    if (arg_year == line['REPORTYEAR']):
      # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
      # e.g. print( line[ 'workers' ] ) yields 'w0'
      try:
        percentage = round(int(line['Total Heart'])/int(line['Actual DBD']),1)
        fill = scale[percentage]
      except:
        percentage = 'N/A'
        fill = scale[0.0]
      print(line['ISO'],line['REPORTYEAR'],line['TOTAL Actual DD'],line['Actual DBD'],line['Actual DCD'],line['Total Heart'],percentage)
      # a.update({line['ISO'] : {'Second': 2, 'Third': 3, 'First': 1, 'fill': '#00ff00', 'fill-opacity': 0.5 }})
      a.update({line['ISO'] : {'year': line['REPORTYEAR'],'TOTAL_Actual_DD': line['TOTAL Actual DD'],'Actual_DBD': line['Actual DBD'], 'Actual_DCD': line['Actual DCD'], 'Total_Heart': line['Total Heart'], 'percentage': percentage, 'fill': fill, 'fill-opacity': 0.5 }})

with open('./countries.geo.json', 'rt') as jsonfile:
  geo = json.load(jsonfile)
  print(geo['features'])
  for o in geo['features']:
    print(o['id'],o['properties'])
    try:
      b = a[o['id']]
      o['properties'].update(b)
    except:
      print('not found')
  with open('./research.'+arg_year+'.geo.json', 'wt') as researchfile:
    json.dump(geo,researchfile)

#  for row in spamreader:
#    i
#    print(', '.join(row))