import csv
import sys
import json

try:
  arg_year = sys.argv[1]
except:
  arg_year = '2017'

a = dict()

with open('../data/GODT_downloads.csv', 'rt') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    if (arg_year == line['REPORTYEAR']):
      # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
      # e.g. print( line[ 'workers' ] ) yields 'w0'
      try:
        percentage = round(int(line['Total Heart'])/int(line['Actual DBD']),1)
      except:
        percentage = 'N/A'
      print(line['ISO'],line['REPORTYEAR'],line['TOTAL Actual DD'],line['Actual DBD'],line['Actual DCD'],line['Total Heart'],percentage)
      a.update({line['ISO'] : {'Second': 2, 'Third': 3, 'First': 1, 'fill': '#00ff00', 'fill-opacity': 0.5 }})

with open('../countries.geo.json', 'rt') as jsonfile:
  geo = json.load(jsonfile)
  print(geo['features'])
  for o in geo['features']:
    print(o['id'],o['properties'])
    try:
      b = a[o['id']]
      o['properties'].update(b)
    except:
      print('not found')
  with open('../research.geo.json', 'wt') as researchfile:
    json.dump(geo,researchfile)

#  for row in spamreader:
#    i
#    print(', '.join(row))