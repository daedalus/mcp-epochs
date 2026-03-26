from mcp_epochs._core import get_unix_time


def test_get_unix_time_returns_dict() -> None:
    """Test that get_unix_time returns a dictionary with required keys."""
    result = get_unix_time()
    assert isinstance(result, dict)
    assert "unix_time" in result
    assert "unix_time_ms" in result
    assert "iso8601" in result


def test_get_unix_time_unix_time_is_int() -> None:
    """Test that unix_time is an integer."""
    result = get_unix_time()
    assert isinstance(result["unix_time"], int)


def test_get_unix_time_unix_time_ms_is_int() -> None:
    """Test that unix_time_ms is an integer."""
    result = get_unix_time()
    assert isinstance(result["unix_time_ms"], int)


def test_get_unix_time_iso8601_is_str() -> None:
    """Test that iso8601 is a string."""
    result = get_unix_time()
    assert isinstance(result["iso8601"], str)


def test_get_unix_time_ms_is_1000x_unix_time() -> None:
    """Test that unix_time_ms is approximately 1000x unix_time."""
    result = get_unix_time()
    assert result["unix_time_ms"] >= result["unix_time"] * 1000
    assert result["unix_time_ms"] < (result["unix_time"] + 1) * 1000


def test_get_unix_time_is_future() -> None:
    """Test that unix_time is greater than 0 (post-1970)."""
    result = get_unix_time()
    assert result["unix_time"] > 0


def test_get_unix_time_consecutive_calls_increase() -> None:
    """Test that consecutive calls return increasing or equal timestamps."""
    result1 = get_unix_time()
    result2 = get_unix_time()
    assert result2["unix_time"] >= result1["unix_time"]
