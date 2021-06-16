import argparse
import json
import requests

import constant
from request_data_model import ENTITY_PARAMS_MAP


def get_data(entity, args={}):
    print("Getting {} data....".format(entity))
    if entity in constant.entity_url_map.keys():
        params = ENTITY_PARAMS_MAP[entity]
        for arg in args.keys():
            if arg in params.__dict__.keys():
                setattr(params, arg, args[arg])
        params = params.__dict__
        response = requests.get(constant.entity_url_map[entity], params=params)
        return response.json()
    return KeyError

def save_json_to_file(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Successfully saved: {}".format(filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Data Acquisition For Fantasy Football Euro 2020")
    parser.add_argument_group()
    parser.add_argument("-e", "--entity", default="players", type=str, help="Entity to get")
    parser.add_argument("-m", "--matchdayId", type=int, help="only for players entity")

    args = parser.parse_args().__dict__
    entity = args.pop('entity')
    params = args

    data = get_data(entity)
    if params["matchdayId"]:
        filename = "../data/raw/euro-2020/{}_{}.json".format(entity, params["matchdayId"])
    else:
        filename = "../data/raw/euro-2020/{}.json".format(entity)
    save_json_to_file(data, filename)
