from app.io.input import input_console, input_file, input_csv
from app.io.output import output_console, output_file, output_csv


def main():
    # 1. Console input example
    console_data = input_console()
    output_console(f"Console input result: {console_data}")
    output_file(console_data, "data/console_output.txt")

    # 2. Text file example
    text_data = input_file("data/data_input.txt")
    output_console(f"\nText file content:\n{text_data}")
    output_file(text_data, "data/data_output.txt")

    # 3. CSV file example
    csv_data = input_csv("data/data_input_csv.csv")
    output_console("\nCSV file content:")
    output_console(str(csv_data.head()))
    output_csv(csv_data, "data/data_output_csv.csv")

if __name__ == "__main__":
    main()