import pytest
from app.io.input import input_file

# =============================================
# Tests for input_file() - Standard file input
# ============================================="
def test_input_file_reads_content(tmp_path):
    """Test reading from regular text file"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello\nWorld")

    content = input_file(str(test_file))
    assert content == "Hello\nWorld"


def test_input_file_empty(tmp_path):
    """Test reading empty file"""
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")

    assert input_file(str(empty_file)) == ""


def test_input_file_nonexistent():
    """Test handling of non-existent file"""
    with pytest.raises(FileNotFoundError):
        input_file("nonexistent_file.txt")