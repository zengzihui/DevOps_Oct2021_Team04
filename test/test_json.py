import pytest, json,os
from classes.json import *
def test_update_json():
    """
    test if update json works

    Swah Jianoon T01 26th January
    """
    data = {'board_size': 4, 'high_scores:': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = "high_score_20.json"
    update_json(filename)
    f = open(os.path.join("save_files",filename))
    output = json.load(f)
    assert output == data

def test_retrieve_json():
    data = {'board_size': 4, 'high_scores:': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = os.path.join("save_files",filename)
    with open(filename, "w") as jsonFile:
        json.dump(data, jsonFile)
    output = load_json(filename)
    assert output == data