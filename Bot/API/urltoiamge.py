import requests
import os
from datetime import datetime

from typing import Optional

def url_to_image(url: str, output_filename: Optional[str] = None) -> str:
    try:
        apiurl = "https://www.urltoany.com/api/function/to-image"
        payload = {
            "url": url
        }
        headers = {
            "Content-Type": "application/json"
        }

        print(f"Converting URL to image: {url}")
        response = requests.post(apiurl, json=payload, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            return f"Error: API returned status code {response.status_code}"

        # Check if response contains image data
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            return f"Error: Expected image data, got {content_type}"

        # Generate filename if not provided
        if output_filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"url_screenshot_{timestamp}.png"

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_filename) if os.path.dirname(output_filename) else "."
        os.makedirs(output_dir, exist_ok=True)

        # Save the image data
        with open(output_filename, "wb") as f:
            f.write(response.content)

        file_size = len(response.content)
        print(f"Successfully saved screenshot: {output_filename} ({file_size} bytes)")
        return output_filename

    except requests.RequestException as e:
        print(f"Network Error: {e}")
        return f"Error: Network request failed - {e}"
    except IOError as e:
        print(f"File Error: {e}")
        return f"Error: Failed to save file - {e}"
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return f"Error: {e}"