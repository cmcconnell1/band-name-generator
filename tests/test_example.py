"""Example test file to verify pytest setup."""


def test_example() -> None:
    """Example test that always passes."""
    assert True


def test_addition() -> None:
    """Test basic arithmetic."""
    assert 1 + 1 == 2


def test_string_operations() -> None:
    """Test string operations."""
    result = "hello".upper()
    assert result == "HELLO"
