import pytest, json,os
from classes.json import *
def test_load_json_file_does_not_exist():
    """
    test if load json if file does not exist

    Swah Jianoon T01 26th January
    """
    filename = "high_score_test.json"
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),filename)
    output = load_json(file_path)
    assert output == {'board_size': 0, 'high_scores': []}

def test_update_json():
    """
    test if update json works

    Swah Jianoon T01 26th January
    """
    data = {'board_size': 4, 'high_scores': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = "high_score_4.json"
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),filename)
    update_json(file_path,data)
    file = open (file_path, "r")
    output = json.loads(file.read())
    file.close()
    assert output == data

def test_load_json():
    """
    test if load json works

    Swah Jianoon T01 26th January
    """
    data = {'board_size': 4, 'high_scores': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = "high_score_4.json"
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),filename)
    with open(file_path, "w") as jsonFile:
            json.dump(data, jsonFile)
    output = load_json(file_path)
    assert output == data