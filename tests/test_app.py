from rest_example.app import main
import subprocess


def test_main():
    assert main() == 0


def test_program():
    subprocess.call(["python", "rest_example/app.py"])
