import json

from google.oauth2 import service_account
from googleapiclient.discovery import Resource, build

class GoogleAPI:
    
    def __init__(self, credentials_path: str):
        with open(credentials_path) as source:
            info = json.load(source)
        self.creds = service_account.Credentials.from_service_account_info(info)
        self.service: Resource = build('sheets', 'v4', credentials=self.creds)

class GoogleSheetTableLogger(GoogleAPI):
    """Logger that converts database-represented table into google sheet tables"""

    def __init__(self, credentials_path: str, sheetID: str, sheet_name: str):
        super().__init__(credentials_path)
        self.sheetID = sheetID
        self.sheet_name = sheet_name

    def __call__(self, table: list[dict[str, str]]) -> bool:

        cur_row = self.get_current_row()

        values = list(map(
            lambda el: [
                el["firstname"],
                el["lastname"],
                el["classID"],
                el["table"],
                f"=TO_DATE(DATEVAL(\"{el['time'].split(' ')[0]}\"))",
                f"{el['time'].split(' ')[1]}",
            ],
            table
        ))

        body = {
            "values": values
        }

        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.sheetID,
            range=f"Today!A{cur_row*9+3}:F{cur_row*9+11}",
            body=body,
            valueInputOption="USER_ENTERED"
        ).execute()

        if result.get('updatedCells') > 0 :
            self.set_next_row(cur_row + 1)

        return True # Should return False if everything does'nt go well

    def get_current_row(self) -> int:
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.sheetID,
            range=f"{self.sheet_name}!A1:A1"
        ).execute()
        value = int(result.get('values', [])[0][0])
        return value

    def set_next_row(self, next_row: int) -> None:
        self.service.spreadsheets().values().update(
            spreadsheetId=self.sheetID,
            range=f"{self.sheet_name}!A1:A1",
            body={"values": [[next_row]]},
            valueInputOption="USER_ENTERED"
        ).execute()