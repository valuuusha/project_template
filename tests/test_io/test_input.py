import pytest
import pandas as pd
from app.io.input import input_file
from app.io.input import input_csv

# =============================================
# Tests for input_file() - Standard file input
# =============================================

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


# =============================================
# Tests for input_csv() - Pandas CSV input
# =============================================

def test_input_csv_reads_data(tmp_path):
    """Test reading CSV with pandas"""
    test_file = tmp_path / "test.csv"
    test_file.write_text("Name,Age\nAlice,25\nBob,30")

    df = input_csv(str(test_file))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Name", "Age"]


def test_input_csv_empty(tmp_path):
    """Test reading empty CSV"""
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    with pytest.raises(pd.errors.EmptyDataError):
        input_csv(str(empty_file))


def test_input_csv_nonexistent():
    """Test handling of non-existent CSV"""
    with pytest.raises(FileNotFoundError):
        input_csv("nonexistent.csv")