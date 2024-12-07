from src.cyber_immune.data_preprocessing import load_data

def test_load_data():
    X, y, df = load_data()
    assert len(X) > 0, "X should not be empty"
    assert 'bytes_sent' in X.columns, "bytes_sent column should exist"
    assert 'status_code' in X.columns, "status_code column should exist"
    assert len(y) == len(X), "y should match X in length"
