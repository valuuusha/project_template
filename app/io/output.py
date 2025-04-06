import pandas as pd


def output_console(text):
    """
    Output text to the console.

    Args:
        text (str): text to be printed to console.
    """
    print(text)


def output_file(text: str, file_path: str):
    """
    Write text to a file using Python's built-in file operations.

    Args:
        text (str): text content to be written to file.
        file_path (str): path to the output file.
    """
    with open(file_path, 'w') as file:
        file.write(text)


def output_csv(data: pd.DataFrame, file_path: str):
    """
    Write a pandas DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): data to be written to CSV file.
        file_path (str): path to the output CSV file.
    """
    data.to_csv(file_path, index=False)