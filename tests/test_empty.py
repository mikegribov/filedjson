from djson.src.djson import DJson
import os


def check_empty(name, info = {}):
    dj = DJson(os.path.join("examples", name))
    result = dj.structure.pop('_info', {})
    assert dj.structure == {}
    for name in info:
        assert info[name] == result[name]

def test_empty_file():
    check_empty('empty_file', {'size':0, 'type':'file', 'ext':'json', 'name':'empty_file'})

def test_empty_file_with_ext():
    check_empty('empty_file.json', {'size': 0, 'type': 'file', 'ext': 'json', 'name': 'empty_file'})

def test_empty_file_with_point():
    check_empty('empty_file.ext', {'size': 0, 'type': 'file', 'ext': 'json', 'name': 'empty_file.ext'})

def test_empty_file_with_point_and_ext():
    check_empty('empty_file.ext.json', {'size': 0, 'type': 'file', 'ext': 'json', 'name': 'empty_file.ext'})

def test_empty_file_no_json_ext():
    check_empty('empty_file.cfg', {'size': 0, 'type': 'file', 'ext': 'cfg', 'name': 'empty_file'})

def test_empty_file_not_existed():
    check_empty('file_not_existed')

def test_empty_dir():
    check_empty('empty_dir', {'type': 'directory', 'name': 'empty_dir'})

def test_empty_dir_with_point():
    check_empty('empty_dir.cfg', {'type': 'directory', 'name': 'empty_dir.cfg'})