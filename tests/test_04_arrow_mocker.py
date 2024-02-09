import arrow

mocked_historical_date = '2024-02-09T09:42:32.247931+01:00'


def test_today_mocked_historical_date(mocker):
    with mocker.patch.object(arrow, 'now', return_value=mocked_historical_date):
        assert arrow.now() == mocked_historical_date


def test_today_arrow_implementation():
    assert arrow.now() != mocked_historical_date
