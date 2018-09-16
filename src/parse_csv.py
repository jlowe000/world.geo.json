import csv
import sys

try:
  arg_year = sys.argv[1]
except:
  arg_year = '2017'

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
      
#  for row in spamreader:
#    i
#    print(', '.join(row))