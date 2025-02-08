from design_a_number_container_system import NumberContainers

def test_ex1():
    nc = NumberContainers()
    result = nc.find(10)
    assert result == -1
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    result = nc.find(10)
    assert result == 1
    nc.change(1, 20)
    result = nc.find(10)
    assert result == 2
