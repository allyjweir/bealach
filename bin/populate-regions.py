import json
import psycopg2


print('Populating regions')

regions = []
with open('fixtures/cols-and-passes.json') as f:
    points = json.loads(f.read())
    for point in points:
        if point['region'] not in regions:
            regions.append(point['region'])

with psycopg2.connect(database='bealach') as conn:
    cur = conn.cursor()
    concat_regions = ''
    for region in regions:
        concat_regions += f'(\'{region}\'),'
    concat_regions = concat_regions[:-1]

    cur.execute(f'INSERT INTO regions (name) VALUES {concat_regions}')

print('Successful population of regions')