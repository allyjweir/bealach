import json
import psycopg2


print("Populating points")

with open('fixtures/cols-and-passes.json') as f:
    points = json.loads(f.read())
    values = []

    for point in points:
        values.append(f"('{point['name']}', '{point['lat']}', '{point['lng']}', (SELECT id FROM regions WHERE name='{point['region']}')), ")

    with psycopg2.connect(database='bealach') as conn:
        cur = conn.cursor()
        concat_values = ''.join(values)
        query = f'INSERT INTO points (name, lat, lon, region_id) VALUES {concat_values.strip()[:-1]}'
        cur.execute(query)

print("Successfully populated points")
