#!/usr/bin/env python3
"""
Test script for the URL to Image conversion functionality
"""

import sys
import os
sys.path.append('Bot/API')

from urltoiamge import url_to_image

def test_url_to_image():
    """Test the url_to_image function with different scenarios"""

    print("Testing URL to Image Conversion")
    print("=" * 50)

    # Test 1: Default filename
    print("\n1. Testing with default filename:")
    result1 = url_to_image("https://flair.ai/pricing")
    print(f"   Result: {result1}")

    # Test 2: Custom filename
    print("\n2. Testing with custom filename:")
    result2 = url_to_image("https://example.com", "custom_screenshot.png")
    print(f"   Result: {result2}")

    # Test 3: Custom filename with directory
    print("\n3. Testing with custom filename in subdirectory:")
    result3 = url_to_image("https://github.com", "screenshots/github_homepage.png")
    print(f"   Result: {result3}")

    # Test 4: Invalid URL (to test error handling)
    print("\n4. Testing with invalid URL:")
    result4 = url_to_image("not-a-valid-url")
    print(f"   Result: {result4}")

    print("\n" + "=" * 50)
    print("Test completed!")

    # List generated files
    print("\nGenerated files:")
    for file in os.listdir("."):
        if file.endswith(".png"):
            size = os.path.getsize(file)
            print(f"  - {file} ({size} bytes)")

    if os.path.exists("screenshots"):
        print("\nFiles in screenshots directory:")
        for file in os.listdir("screenshots"):
            if file.endswith(".png"):
                size = os.path.getsize(os.path.join("screenshots", file))
                print(f"  - screenshots/{file} ({size} bytes)")

if __name__ == "__main__":
    test_url_to_image()
