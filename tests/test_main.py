from pytest_mock import MockerFixture


def test_main_exits_zero(mocker: MockerFixture) -> None:
    """Test that main returns 0."""
    from mcp_epochs.__main__ import main

    mocker.patch("mcp_epochs.__main__.run_server", return_value=0)
    assert main() == 0


def test_main_calls_run_server(mocker: MockerFixture) -> None:
    """Test that main calls run_server."""
    mock_run = mocker.patch("mcp_epochs.__main__.run_server", return_value=0)
    from mcp_epochs.__main__ import main

    main()
    mock_run.assert_called_once()
