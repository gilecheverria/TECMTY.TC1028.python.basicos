import pytest
from src.main import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Hello Gil!\n", "Should read 'Hello Gil!'"
