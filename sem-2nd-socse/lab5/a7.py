import pandas as pd
def process_experience_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\nLast 3 rows:")
        print(df.tail(3))
        print("\nDataFrame Information:")
        print(df.info())
        print("\nDataFrame Description:")
        print(df.describe())
        print("\nColumn Names:")
        print(df.columns)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file at '{file_path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the CSV file at '{file_path}'. Check the file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
file_path = 'experience.csv'
try:
    with open(file_path, 'w') as f:
        f.write("Years_Experience,Salary\n")
        f.write("1,30000\n")
        f.write("2,40000\n")
        f.write("3,50000\n")
        f.write("4,60000\n")
        f.write("5,70000\n")
except Exception as e:
    print(f"Error creating test csv: {e}")
process_experience_data(file_path)
