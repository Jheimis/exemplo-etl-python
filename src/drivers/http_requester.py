from typing import Dict
import requests

class HttpResquester:

    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[int, str]:
        try:
            response = requests.get(self.__url, timeout=5)
            return{
                "status_code" : response.status_code,
                "html" : response.text
            }
        except requests.exceptions.Timeout:
            print("The request timed out")
            return {
                "status_code": 408,  # Request Timeout status code
                "html": ""
            }
        