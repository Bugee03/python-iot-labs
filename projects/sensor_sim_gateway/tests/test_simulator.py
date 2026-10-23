from simulator import (generate_data)

def test_generate_data_keys():
    data = generate_data()
    assert "temperature" in data
    assert "current" in data
    assert "vibration" in data

