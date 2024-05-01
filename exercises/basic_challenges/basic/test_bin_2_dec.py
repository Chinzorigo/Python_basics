def test_find_binary():
    # Test case 1: decimal = 0
    assert find_binary(0) == ""

    # Test case 2: decimal = 1
    assert find_binary(1) == "1"

    # Test case 3: decimal = 10
    assert find_binary(10) == "1010"

    # Test case 4: decimal = 15
    assert find_binary(15) == "1111"

    # Test case 5: decimal = 100
    assert find_binary(100) == "1100100"


test_find_binary()
