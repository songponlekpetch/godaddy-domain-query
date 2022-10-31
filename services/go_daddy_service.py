import requests
from typing import List, Dict


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
            print(e.response.status_code)
            print(e.response.json())
    