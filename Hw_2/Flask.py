from flask import Flask
import csv
from faker import Faker
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/avr_data")
def get_avr_data():
    INC_TO_CM = 2.54
    POUND_TO_KG = 0.45
    height_lst = []
    weight_lst = []
    with open('hw.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            height_lst.append(float(row[' "Height(Inches)"']))
            weight_lst.append(float(row[' "Weight(Pounds)"']))
    avr_height = (sum(height_lst) * INC_TO_CM) / len(height_lst)
    avr_weight = (sum(weight_lst) * POUND_TO_KG) / len(weight_lst)
    return "Is average height:" + str(avr_height) + "<br/g> Is average weight: " + str(avr_weight)


@app.route("/requirements")
def get_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read().replace('\n', '<br/>')
    return requirements


@app.route("/random_students")
def get_random_students2():
    fake = Faker(['uk_UA'])
    names_lst = [fake.name() for _ in range(10)]
    return json.dumps(str(names_lst), ensure_ascii=False)


app.run(debug=True, port=5000)
