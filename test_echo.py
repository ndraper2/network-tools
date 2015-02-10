import os


def test_simple_string(capfd):
    os.system("python echo_client.py 'This is the message to send'")
    out, err = capfd.readouterr()
    print out
    print err
    assert out == "I heard: This is the message to send\n"
