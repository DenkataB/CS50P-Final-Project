from project import format_schedule, get_iata_code, check_time
import pytest

data = {
            "flight_date": "2019-12-12",
            "flight_status": "active",
            "departure": {
                "airport": "San Francisco International",
                "timezone": "America/Los_Angeles",
                "iata": "SFO",
                "icao": "KSFO",
                "terminal": "2",
                "gate": "D11",
                "delay": 13,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": "2019-12-12T04:20:13+00:00",
                "estimated_runway": "2019-12-12T04:20:13+00:00",
                "actual_runway": "2019-12-12T04:20:13+00:00"

            }
}

def test_format_schedule():
    assert format_schedule(data["departure"]["scheduled"]) == "12/12/2019 at 04:20"

def test_get_iata_code():
    assert get_iata_code("ist") == "IST"
    assert get_iata_code("LAX") == "LAX"
    assert get_iata_code("istanbul") == "IST"
    assert get_iata_code("Los Angeles") == "LAX"

    with pytest.raises(SystemExit):
        get_iata_code("cats")

def test_check_time():
    assert check_time(data) == False
