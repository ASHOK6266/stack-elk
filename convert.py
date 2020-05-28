import csv
import json

csvfile = open('sample.csv','r')
jsonfile = open('sample.json','a+')

fieldnames = ("title","seo_title","url","author","date","category","locales","content")

reader = csv.DictReader(csvfile,fieldnames,delimiter=";")
for row in reader:
    jsonfile.write(r'{"index": {}}')
    jsonfile.write('\n')
    json.dump(row,jsonfile)
    jsonfile.write('\n')
    