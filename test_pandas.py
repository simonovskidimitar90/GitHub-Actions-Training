import pandas as pd
from datetime import datetime
from pandas.errors import EmptyDataError # 1. Import the specific empty data error

# Define the name of your CSV file
csv_filename = "data/test_data.csv"

def append_status_run():
    # Get the current date and time (formatted as YYYY-MM-DD HH:MM:SS)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Try to read the existing CSV file
    try:
        df = pd.read_csv(csv_filename)
    except (FileNotFoundError, EmptyDataError): # 2. Catch BOTH errors here!
        # If the file doesn't exist OR is empty, create a new DataFrame with columns
        df = pd.DataFrame(columns=["Date", "Script Status"])
        
    # Append the new row at the end of the DataFrame
    df.loc[len(df)] = {"Date": current_datetime, "Script Status": "Run"}
    
    # Save the updated DataFrame back to the CSV (index=False prevents saving row numbers)
    df.to_csv(csv_filename, index=False)
    
    print(f"Success! Appended Run status at {current_datetime}")
    print(df)

# Run the function
if __name__ == "__main__":
    append_status_run()
