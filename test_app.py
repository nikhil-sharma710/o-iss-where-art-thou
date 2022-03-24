from app import how_to_interact 
import pytest

def test_how_to_interact():
    assert isinstance(how_to_interact(), str) == True
