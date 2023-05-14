import importlib.util
from pathlib import Path
import pytest


@pytest.fixture
def iter_homework():
    def iterator(number):
        parent = Path(__file__).parents[1]
        homeworks = set(_ for _ in Path.rglob(
            parent, "homework_%02d.py" % number))
        for hwpath in homeworks:
            spec = importlib.util.spec_from_file_location(
                "homework_%02d" % number, hwpath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            yield hwpath.parent.stem, module
    return iterator
