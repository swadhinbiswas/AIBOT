#!/usr/bin/env python3
"""
Simple AI Image Generator for integration with existing bot
"""

import requests
import os
from urllib.parse import quote
import random

def generate_ai_image(prompt, output_dir="generated_images", **kwargs):
    """
    Generate an AI image using Pollinations API

    Args:
        prompt (str): Description of the image
        output_dir (str): Directory to save the image
        **kwargs: Additional options (width, height, style, etc.)

    Returns:
        str: Path to generated image file, or None if failed
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Default parameters
    width = kwargs.get('width', 1024)
    height = kwargs.get('height', 1024)
    seed = kwargs.get('seed', random.randint(1, 100000))
    model = kwargs.get('model', 'flux')
    style = kwargs.get('style', '')
    ratio = kwargs.get('ratio', '')

    # Build the prompt
    final_prompt = prompt
    if style:
        final_prompt += f", style {style}"
    if ratio:
        final_prompt += f", aspect ratio {ratio}"

    # Build the API URL
    encoded_prompt = quote(final_prompt)
    api_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    api_url += f"?width={width}&height={height}&seed={seed}&model={model}"
    api_url += "&nologo=true&private=false&enhance=false&safe=false"

    try:
        print(f"Generating image: '{final_prompt}'")
        response = requests.get(api_url, timeout=60)
        response.raise_for_status()

        # Check if we got an image
        if not response.headers.get('content-type', '').startswith('image/'):
            print("Error: Did not receive an image")
            return None

        # Save the image
        filename = f"ai_generated_{seed}.png"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Image saved: {filepath}")
        return filepath

    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Example usage for your bot
def bot_generate_image(prompt, user_id=None):
    """
    Generate image for bot usage
    """
    # You can customize output directory based on user_id
    output_dir = f"Bot/generated_images"
    if user_id:
        output_dir = f"Bot/generated_images/user_{user_id}"

    return generate_ai_image(prompt, output_dir)

if __name__ == "__main__":
    # Test the function
    prompt = input("Enter a prompt: ")
    result = generate_ai_image(prompt)
    if result:
        print(f"Success! Image saved at: {result}")
    else:
        print("Failed to generate image.")
