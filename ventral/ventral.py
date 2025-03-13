import requests
from typing import Dict, Any, List
from io import BytesIO
from .config import DEFAULT_BASE_URL


class VisionAPIClient:
    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE_URL):
        """Initialize the client with an API key and optional base API URL."""
        self.base_url = base_url
        self.headers = {"X-API-KEY": api_key}

    def _post_request(self, endpoint: str, files: Dict[str, Any], data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Helper function to send a POST request."""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, files=files, data=data)
        return response.json()

    def detect_objects(self, image_path: str, class_name: str = "person") -> Dict[str, Any]:
        """Detect objects in an image."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            data = {"class_name": class_name}
            return self._post_request("/detect", files, data)

    def segment_objects(self, image_path: str, class_name: str = "car") -> Dict[str, Any]:
        """Segment objects in an image."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            data = {"class_name": class_name}
            return self._post_request("/segment", files, data)

    def sam2_segment(self, image_path: str, point_x: int = 320, point_y: int = 320) -> Dict[str, Any]:
        """Run SAM2 segmentation using a point-based prompt."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            data = {"point_x": point_x, "point_y": point_y}
            return self._post_request("/sam2-segment", files, data)

    def classify_image(self, image_path: str) -> Dict[str, Any]:
        """Classify an image using YOLOv8 classification model."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            return self._post_request("/classify", files)

    def extract_text(self, image_path: str) -> Dict[str, Any]:
        """Perform OCR on an image and extract text."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            return self._post_request("/ocr", files)

    def caption_image(self, image_path: str) -> Dict[str, Any]:
        """Generate a caption for an image using BLIP model."""
        with open(image_path, "rb") as img:
            files = {"image": img}
            return self._post_request("/image-caption", files)

    def get_protected_resource(self) -> Dict[str, Any]:
        """Access a protected resource using the API key."""
        url = f"{self.base_url}/protected-resource/"
        response = requests.get(url, headers=self.headers)
        return response.json()

# Example Usage
if __name__ == "__main__":

    client = VisionAPIClient(api_key="your_api_key_here")

    # Example calls
    print(client.detect_objects("test_image.jpg", class_name="car"))
    print(client.segment_objects("test_image.jpg", class_name="person"))
    print(client.sam2_segment("test_image.jpg", point_x=200, point_y=300))
    print(client.classify_image("test_image.jpg"))
    print(client.extract_text("text_image.jpg"))
    print(client.caption_image("scene.jpg"))
    print(client.get_protected_resource())
