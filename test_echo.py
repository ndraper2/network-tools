import echo_client


def test_simple_string(capsys):
    echo_client("This is the message to send")
    assert capsys.readouterr() == "This is the message to send"
