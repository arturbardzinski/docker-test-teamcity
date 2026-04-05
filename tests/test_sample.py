import pytest


def test_example():
    assert 1 + 1 == 2


def test_addition():
    assert 2 + 3 == 5


def test_list():
    assert isinstance([1, 2, 3], list)


def test_string_strip_and_upper():
    assert "  hello  ".strip() == "hello"
    assert "teamcity".upper() == "TEAMCITY"


def test_dict_get_default():
    cfg = {"branch": "main"}
    assert cfg.get("branch") == "main"
    assert cfg.get("missing", "default") == "default"


def test_set_membership():
    tags = {"ci", "docker", "python"}
    assert "ci" in tags
    assert "java" not in tags


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 2),
        (-3, 7, 4),
        (10, -10, 0),
    ],
)
def test_parametrized_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize("text", ["", "a", "pytest", "multi\nline"])
def test_string_len_non_negative(text):
    assert len(text) >= 0


def test_list_comprehension_filters_evens():
    assert [n for n in range(10) if n % 2 == 0] == [0, 2, 4, 6, 8]


def test_sorted_is_stable_order():
    assert sorted([3, 1, 2]) == [1, 2, 3]


def test_zero_division_raises():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0


def test_truthiness():
    assert bool([]) is False
    assert bool([0]) is True
    assert not None


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0


def test_is_string_instance():
    assert isinstance("hello", str)