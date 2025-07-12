#!/usr/bin/env python3
"""
Test script for AI Image Generation
"""

import sys
import os

# Add the current directory to Python path
sys.path.append('/home/swadhin/AIBOT')

def test_simple_generator():
    """Test the simple generator"""
    print("=== Testing Simple AI Generator ===")

    try:
        from simple_ai_generator import generate_ai_image

        prompt = "a cute cat sitting on a rainbow"
        print(f"Generating image with prompt: '{prompt}'")

        result = generate_ai_image(prompt, width=512, height=512)

        if result:
            print(f"✅ Success! Image saved at: {result}")
            return True
        else:
            print("❌ Failed to generate image")
            return False

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_bot_api():
    """Test the bot API"""
    print("\n=== Testing Bot API ===")

    try:
        from Bot.API.aiimage import AIImageAPI

        api = AIImageAPI()
        prompt = "a robot painting a picture"

        print(f"Generating image with prompt: '{prompt}'")
        result = api.generate_image(prompt, user_id=12345, width=512, height=512)

        if result['success']:
            print(f"✅ Success! Image saved at: {result['filepath']}")
            print(f"   Seed: {result['seed']}")
            return True
        else:
            print(f"❌ Failed: {result['error']}")
            return False

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("AI Image Generator Test Suite")
    print("=" * 40)

    # Check if requests is available
    try:
        import requests
        print("✅ requests library is available")
    except ImportError:
        print("❌ requests library not found. Please install: pip install requests")
        return

    # Check if PIL is available
    try:
        from PIL import Image
        print("✅ PIL (Pillow) library is available")
    except ImportError:
        print("⚠️  PIL (Pillow) not found. Install with: pip install Pillow")
        print("   (Image display won't work, but generation will)")

    print()

    # Run tests
    test1_passed = test_simple_generator()
    test2_passed = test_bot_api()

    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"Simple Generator: {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"Bot API:          {'✅ PASSED' if test2_passed else '❌ FAILED'}")

    if test1_passed or test2_passed:
        print("\n🎉 At least one method is working! You can generate AI images.")
    else:
        print("\n😞 All tests failed. Check your internet connection and try again.")

if __name__ == "__main__":
    main()
