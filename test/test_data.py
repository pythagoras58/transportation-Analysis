def test_fremont_data():
    dataset = pd.read_csv('data/dataset.csv', index_col='Date', parse_dates=True)
    dataset.columns = ['Total', 'East', 'West']
    assert all(dataset.columns)
    assert isinstance(dataset.index, pd.DatetimeIndex)