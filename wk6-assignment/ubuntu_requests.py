import requests
import os
import hashlib
from urllib.parse import urlparse

def fetch_images(urls):
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    os.makedirs("Fetched_Images", exist_ok=True)
    downloaded_hashes = set()  # Track duplicates by file hash
    
    for url in urls:
        try:
            # Fetch the image with precautions
            headers = {"User-Agent": "UbuntuImageFetcher/1.0"}  # Respectful header
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()

            # Check important headers before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped (Not an image): {url}")
                continue

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicate downloads using hash check
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"✗ Skipped duplicate: {filename}")
                continue
            downloaded_hashes.add(file_hash)

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    # Accept multiple URLs from the user (comma-separated)
    url_input = input("Please enter one or more image URLs (comma-separated): ")
    url_list = [u.strip() for u in url_input.split(",") if u.strip()]
    fetch_images(url_list)
