from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

oly_list = convert_to_dict('olympians.csv')

pairs_list = []
for olympian in oly_list:
    pairs_list.append( (olympian['rank'], olympian['name'] ) )

@app.route('/')
def index():
    return render_template('index.html', pairs_list=pairs_list)

@app.route('/olympian/<num>')
def olympian(num):
    oly = oly_list[int(num) - 1]
    return render_template('olympian.html', oly=oly)

if __name__ == '__main__':
    app.run(debug=True)
    