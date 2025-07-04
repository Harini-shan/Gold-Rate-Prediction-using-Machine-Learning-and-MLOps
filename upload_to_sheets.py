
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def append_flagged_to_sheets(csv_file_path, sheet_name="Uploaded_flagged_data"):
    # Setup credentials
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Open spreadsheet
    try:
        spreadsheet = client.open(sheet_name)
    except:
        spreadsheet = client.create(sheet_name)
    
    worksheet = spreadsheet.sheet1

    # Read flagged CSV
    df = pd.read_csv(csv_file_path)

    # Get current number of rows in sheet
    existing_rows = len(worksheet.get_all_values())

    # Remove header if already present
    if existing_rows > 0:
        df = df.iloc[existing_rows - 1:]

    # Only append new rows
    if not df.empty:
        worksheet.append_rows(df.values.tolist(), value_input_option="USER_ENTERED")
        print("✅ Appended new flagged data to Google Sheets.")
    else:
        print("ℹ️ No new data to append.")

append_flagged_to_sheets(r"C:\Users\sride\OneDrive\Documents\Data Science\Gold_rate_prediction\.gradio\flagged\dataset1.csv")