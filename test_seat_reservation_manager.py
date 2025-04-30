from seat_reservation_manager import SeatManager

def test_ex1():
    seatManager = SeatManager(5)
    result = seatManager.reserve()
    assert result == 1
    result = seatManager.reserve()
    assert result == 2
    seatManager.unreserve(2)
    result = seatManager.reserve()
    assert result == 2
    result = seatManager.reserve()
    assert result == 3
    result = seatManager.reserve()
    assert result == 4
    result = seatManager.reserve()
    assert result == 5
    seatManager.unreserve(5)
