import pprint
import pyuca
import pandas as pd
from tabulate import tabulate
from typing import List, Dict


class ReportService:

    @staticmethod
    def create(data: List[Dict], columns: List[str]) -> None:
        report = pd.DataFrame(data)
        report["expires"] = pd.to_datetime(report['expires']).dt.strftime("%d %b %Y")
        report["domain"] = report["domain"].str.lower()
        report = report[columns]
        collator = pyuca.Collator()
        report.sort_values(by="domain", ascending=True, inplace=True, key=lambda x: x.apply(lambda x: collator.sort_key(x)))
        print(tabulate(report, headers='keys', tablefmt='psql'))
        
    @staticmethod
    def get_columns(data: List[Dict]):
        report = pd.DataFrame(data)
        pprint.pprint(report.columns.tolist(), indent=4)
