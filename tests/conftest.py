import pytest


@pytest.fixture
def sample_timestamp() -> dict[str, int | str]:
    return {
        "unix_time": 1735689600,
        "unix_time_ms": 1735689600000,
        "iso8601": "2026-01-01T00:00:00Z",
    }
