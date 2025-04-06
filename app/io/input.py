import pandas as pd


def input_console():
    """
    Prompt the user to enter data via console input.

    Returns:
        str: user input as a string.
    """
    data = input("Enter data: ")
    return data


def input_file(file_path):
    """
    Read and return the entire content of a text file.

    Args:
        file_path (str): path to the text file to be read.

    Returns:
        str: content of the file as a string.
    """
    with open(file_path, "r") as file:
        data = file.read()
        return data


def input_csv(file_path):
    """
    Read and parse a CSV file into a pandas DataFrame.

    Args:
        file_path (str): path to the CSV file to be read.

    Returns:
        pd.DataFrame: data from the CSV file as a DataFrame.
    """
    df = pd.read_csv(file_path)
    return df