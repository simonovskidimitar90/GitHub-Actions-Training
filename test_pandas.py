import pandas as pd
from datetime import datetime

# Define the name of your CSV file
csv_filename = "data/test_data.csv"

def append_status_run():
    # 1. Get the current date and time (formatted as YYYY-MM-DD HH:MM:SS)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Try to read the existing CSV file
    try:
        df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        # If the file doesn't exist yet, create a new DataFrame with the correct columns
        df = pd.DataFrame(columns=["Date", "Script Status"])
        
    # 3. Append the new row at the end of the DataFrame
    # len(df) gives the next available index number at the bottom
    df.loc[len(df)] = {"Date": current_datetime, "Script Status": "Run"}
    
    # 4. Save the updated DataFrame back to the CSV (index=False prevents saving row numbers)
    df.to_csv(csv_filename, index=False)
    
    print(f"Success! Appended Run status at {current_datetime}")

# Run the function
if __name__ == "__main__":
    append_status_run()
