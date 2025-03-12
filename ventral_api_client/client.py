import requests

class VisionAPIClient:
    def __init__(self, api_key: str, base_url: str = "https://kontakt.mine.nu"):
        self.api_key = api_key
        self.base_url = base_url

    def _request(self, endpoint: str, payload: dict):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")
        
        return response.json()

    def detect_objects(self, image_path: str):
        with open(image_path, "rb") as image_file:
            files = {"file": image_file}
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(f"{self.base_url}/detect", files=files, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")

        return response.json()
