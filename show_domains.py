import requests
import pprint
import pyuca
import pandas as pd
from tabulate import tabulate
from typing import List, Dict

GO_DADDY_API_KEY="9jL9mbzZ6jj_6KgdvfcYEZDm897eTefwnh"
GO_DADDY_API_SECRET="K9q8i8vaLqamVz2cw1Ddob"
GO_DADDY_API_URL="https://api.godaddy.com/v1"


class ReportService:

    @staticmethod
    def create(data: List[Dict], columns: List[str]) -> None:
        report = pd.DataFrame(data)
        
        if "expires" in columns:
            report["expires"] = pd.to_datetime(report['expires']).dt.strftime("%d %b %Y")
            report["expires"] = report["expires"].astype(str)
            
        if "domain" in columns:
            report["domain"] = report["domain"].str.lower()
            
        report = report[columns]
        collator = pyuca.Collator()
        report.sort_values(by="domain", ascending=True, inplace=True, key=lambda x: x.apply(lambda x: collator.sort_key(x)))
        # print(tabulate(report, headers='keys', tablefmt='psql'))
        for index, row in report.iterrows():
            row = row.to_dict()
            print("\t".join(list(row.values())))
        
    @staticmethod
    def get_columns(data: List[Dict]):
        report = pd.DataFrame(data)
        pprint.pprint(report.columns.tolist(), indent=4)


class GoDaddyService:
    
    APIS = dict(
        DOMAINS="/domains",
    )
    
    def __init__(self, api_key: str, api_secret: str, api_url: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_url = api_url
        
    def _create_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"sso-key {self.api_key}:{self.api_secret}",
            "Content-Type": "application/json",
        }
        
    def get_domains(self) -> List[Dict[str, str]]:
        try:
            url = f"{self.api_url}{self.APIS['DOMAINS']}"
            response = requests.get(
                url,
                headers=self._create_headers()
            )
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.HTTPError as e:
            print("Error: ", e)



def show_domains(columns: str="domain,expires,status") -> None:
    """Show domains."""
    go_daddy = GoDaddyService(GO_DADDY_API_KEY, GO_DADDY_API_SECRET, GO_DADDY_API_URL)
    domains = go_daddy.get_domains()
    ReportService.create(data=domains, columns=columns.split(","))
    
    
if __name__ == "__main__":
    show_domains(columns="domain,expires,status")