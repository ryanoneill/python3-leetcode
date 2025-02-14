from product_of_last_k_numbers import ProductOfNumbers

def test_ex1():
    pon = ProductOfNumbers()
    pon.add(3)
    pon.add(0)
    pon.add(2)
    pon.add(5)
    pon.add(4)
    result = pon.getProduct(2)
    assert result == 20
    result = pon.getProduct(3)
    assert result == 40
    result = pon.getProduct(4)
    assert result == 0
    pon.add(8)
    result = pon.getProduct(2)
    assert result == 32
