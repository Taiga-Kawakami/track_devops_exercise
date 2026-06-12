from src.main import add


def test_add_normal_integer_values():
    assert add(7, 2) == 9


def test_add_normal_decimal_values():
    assert add(1.2, 3.5) == 4


def test_add_with_third_argument():
    assert add(2.1, 9.3, 3.7) == 14


def test_add_boundary_min_values():
    assert add(0, 0, 0) == 0


def test_add_boundary_max_values():
    assert add(10, 10, 10) == 30


def test_add_decimal_truncation():
    assert add(5.4, 9.8) == 15


def test_add_decimal_third_argument_truncation():
    assert add(1.9, 4.3, 2.6) == 8


def test_add_a_is_string():
    assert add("5", 2) == -1


def test_add_b_is_string():
    assert add(3, "4") == -1


def test_add_c_is_string():
    assert add(2.5, 3, "x") == -1


def test_add_a_is_none():
    assert add(None, 3, 5.1) == -1


def test_add_b_is_none():
    assert add(2.6, None, 1) == -1


def test_add_c_is_none():
    assert add(2.6, 4, None) == -1


def test_add_a_less_than_zero():
    assert add(-1, 2, 3) == -2


def test_add_b_less_than_zero():
    assert add(1, -2, 3) == -2


def test_add_c_less_than_zero():
    assert add(1, 2, -3) == -2


def test_add_a_greater_than_ten():
    assert add(11, 2, 3) == -2


def test_add_b_greater_than_ten():
    assert add(1, 12, 3) == -2


def test_add_c_greater_than_ten():
    assert add(1, 2, 13) == -2


def test_add_type_check_before_range_check():
    assert add("20", 2, 3) == -1
