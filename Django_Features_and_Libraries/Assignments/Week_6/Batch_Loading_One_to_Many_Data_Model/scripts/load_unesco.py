import csv 
from unesco.models import *
from collections import defaultdict
def run():
    with open("unesco/whc-sites-2018-clean.csv","r") as file:
        csv_data = csv.reader(file)
        meta = dict(enumerate(next(csv_data)))
        Site.objects.all().delete()
        Region.objects.all().delete()
        Iso.objects.all().delete()
        State.objects.all().delete()
        Category.objects.all().delete()
        line = 0
        iso_set = set()
        for row in csv_data:
            print(f"\r line: {line}", end='')
            row_data = defaultdict(lambda :None)
            for j in range(11):
                if row[j]:
                    row_data[meta[j]] = row[j]
            notWanted = ['region','iso','state','category']
            intFields = ['year']
            floatFields = ['latitude','longitude','area_hectares']
            strFields = ['name','description','justification']
            creation = f"Site("
            for i,j in row_data.items():
                if i in notWanted:
                    continue
                if i in strFields:
                    j = j.replace('\n', ' ')
                    j = j.replace('\'', '\"')
                    creation+=f"{i}=\'{j}\',"
                else:    
                    creation+=f"{i}={j},"
            if row_data["category"]:
                category, created = Category.objects.get_or_create(name=row_data["category"])
                creation += 'category = category,'
            if row_data["state"]:
                state, created = State.objects.get_or_create(name=row_data["state"])
                creation += 'state = state,'
            if row_data['iso']:
                iso, created = Iso.objects.get_or_create(name=row_data["iso"])
                creation += 'iso = iso,'
            if row_data['region']:
                region, created = Region.objects.get_or_create(name=row_data["region"])
                creation += 'region = region'

            creation += ")"
            site = eval(creation)
            site.save()
            line += 1