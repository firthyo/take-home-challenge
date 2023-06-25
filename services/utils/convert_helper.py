import xmltodict
import csv
from flask import  jsonify

# ../data/orders.xml


def convert_xml_to_json(xml_file_path):
    with open(xml_file_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        
    return data_dict

# "../data/items.csv"
def convert_csv_to_json(csv_file_path):
    orders_dict = {}
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for order_dict in reader:
            id_value = order_dict["id"]
            orders_dict[id_value] = order_dict
    # print(orders_dict["000f2411-2e00-4e29-9312-e6e00b6f76a0"])
    return orders_dict