import pytest, json,os
from classes.json import *
def test_update_json():
    """
    test if update json works

    Swah Jianoon T01 26th January
    """
    data = {'board_size': 4, 'high_scores:': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = "high_score_4.json"
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"save_files",filename)
    update_json(file_path,data)
    file = open (file_path, "r")
    output = json.loads(file.read())
    file.close()
    assert output == data

def test_retrieve_json():
    """
    test if retrieve json works

    Swah Jianoon T01 26th January
    """
    data = {'board_size': 4, 'high_scores:': [{'name': 'john', 'score': 6}, {'name': 'john2', 'score': 5}, {'name': 'john3', 'score': 3}]}
    filename = "high_score_4.json"
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"save_files",filename)
    with open(file_path, "w") as jsonFile:
            json.dump(data, jsonFile)
    output = load_json(file_path)
    assert output == data