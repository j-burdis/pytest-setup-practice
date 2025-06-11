from unittest.mock import Mock
from lib.time_error import TimeError

def test_calls_api_to_get_time_error():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"unixtime":1749634880}
    timer_mock = Mock()
    timer_mock.time.return_value = 1749634880
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == 0
