import psycopg2
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list_points():
    points = []
    with psycopg2.connect(database='bealach') as conn:
        cur = conn.cursor()
        cur.execute('SELECT points.name, lat, lon, regions.name \
                     FROM points \
                     JOIN regions ON (points.region_id=regions.id);')
        points = cur.fetchall()

    return render_template('list.html', points=points)
