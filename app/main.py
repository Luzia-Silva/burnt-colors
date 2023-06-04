from __future__ import print_function
import numpy as np
import os.path
import analyzes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
    creds = None
    if os.path.exists('auth/token.json'):
        creds = Credentials.from_authorized_user_file('auth/token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'auth/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open('auth/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        burns = analyzes.DegreesOfBurns()
        if not burns:
            print("Sorry, i'dont identification your data burns.")
        else:
            get_burns = sheet.values().get(spreadsheetId=os.environ.get("SAMPLE_SPREADSHEET_ID"),
                                    range='database!A1:A51').execute()
            values = get_burns.get('values', [])
            analysesTheDegree = analyzes.AnalyzesTheBurns(burn_value=burns, burns_values=values)
            array = np.array(values)
            is_present = np.isin(array, str(burns)) 
            exists_value = np.any(is_present)
            if exists_value:
                print("Não vamos armazenar em nossa base esse dado, porque ele existe, porém não irá atrapalhar em nossas análises!")
            else:    
                body_burns =  {
                        'values' : [[ str(burns)]]
                    }
                sheet.values().append(spreadsheetId=os.environ.get("SAMPLE_SPREADSHEET_ID"),
                                            range='database!A1', valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body=body_burns).execute()
                    
            

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()