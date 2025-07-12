#!/usr/bin/env python3
"""
AI Image Generator using Pollinations AI API
Similar to the HTML page but as a Python script
"""

import requests
import os
import sys
import argparse
from urllib.parse import quote
import random
from PIL import Image
from io import BytesIO

class AIImageGenerator:
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt"
        self.models = ["flux", "flux-realism", "flux-anime", "flux-3d"]

    def generate_image(self, prompt, **kwargs):
        """
        Generate an image using the Pollinations AI API

        Args:
            prompt (str): Text description of the image to generate
            **kwargs: Additional parameters (width, height, style, etc.)

        Returns:
            bytes: Image data if successful, None if failed
        """
        # Default parameters
        params = {
            'width': kwargs.get('width', 1024),
            'height': kwargs.get('height', 1024),
            'seed': kwargs.get('seed', random.randint(1, 100000)),
            'model': kwargs.get('model', 'flux'),
            'nologo': kwargs.get('nologo', 'true'),
            'private': kwargs.get('private', 'false'),
            'enhance': kwargs.get('enhance', 'false'),
            'safe': kwargs.get('safe', 'false')
        }

        # Add style and ratio to prompt if provided
        final_prompt = prompt
        if kwargs.get('style'):
            final_prompt += f", style {kwargs['style']}"
        if kwargs.get('ratio'):
            final_prompt += f", aspect ratio {kwargs['ratio']}"

        # Encode the prompt
        encoded_prompt = quote(final_prompt)

        # Build the URL
        url = f"{self.base_url}/{encoded_prompt}"

        # Add parameters to URL
        param_string = "&".join([f"{k}={v}" for k, v in params.items()])
        full_url = f"{url}?{param_string}"

        print(f"Generating image with prompt: '{final_prompt}'")
        print(f"API URL: {full_url}")

        try:
            # Make the request
            response = requests.get(full_url, timeout=60)
            response.raise_for_status()

            # Check if we got an image
            if response.headers.get('content-type', '').startswith('image/'):
                return response.content
            else:
                print(f"Error: Received non-image response: {response.headers.get('content-type')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

    def save_image(self, image_data, filename=None):
        """
        Save image data to a file

        Args:
            image_data (bytes): Image data
            filename (str): Output filename (optional)

        Returns:
            str: Path to saved file
        """
        if not filename:
            filename = f"generated_image_{random.randint(1000, 9999)}.png"

        # Ensure filename has proper extension
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filename += '.png'

        try:
            # Save the image
            with open(filename, 'wb') as f:
                f.write(image_data)

            print(f"Image saved as: {filename}")
            return filename

        except Exception as e:
            print(f"Error saving image: {e}")
            return None

    def show_image(self, image_data):
        """
        Display the image using PIL

        Args:
            image_data (bytes): Image data
        """
        try:
            image = Image.open(BytesIO(image_data))
            image.show()
        except Exception as e:
            print(f"Error displaying image: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate AI images using Pollinations API')
    parser.add_argument('prompt', help='Text description of the image to generate')
    parser.add_argument('--width', type=int, default=1024, help='Image width (default: 1024)')
    parser.add_argument('--height', type=int, default=1024, help='Image height (default: 1024)')
    parser.add_argument('--style', choices=['anime', 'realistic', 'cyberpunk', 'pixelart', 'fantasy'],
                       help='Image style')
    parser.add_argument('--ratio', choices=['16:9', '1:1', '9:16', '4:5'],
                       help='Aspect ratio')
    parser.add_argument('--model', choices=['flux', 'flux-realism', 'flux-anime', 'flux-3d'],
                       default='flux', help='AI model to use')
    parser.add_argument('--seed', type=int, help='Seed for reproducible results')
    parser.add_argument('--output', '-o', help='Output filename')
    parser.add_argument('--show', action='store_true', help='Display the image after generation')
    parser.add_argument('--enhance', action='store_true', help='Enhance the prompt')
    parser.add_argument('--safe', action='store_true', help='Enable strict NSFW filtering')
    parser.add_argument('--logo', action='store_true', help='Include logo overlay')

    args = parser.parse_args()

    # Create generator instance
    generator = AIImageGenerator()

    # Prepare parameters
    params = {
        'width': args.width,
        'height': args.height,
        'model': args.model,
        'nologo': 'false' if args.logo else 'true',
        'enhance': 'true' if args.enhance else 'false',
        'safe': 'true' if args.safe else 'false'
    }

    if args.style:
        params['style'] = args.style
    if args.ratio:
        params['ratio'] = args.ratio
    if args.seed:
        params['seed'] = args.seed

    # Generate the image
    print("Starting image generation...")
    image_data = generator.generate_image(args.prompt, **params)

    if image_data:
        print("Image generated successfully!")

        # Save the image
        saved_path = generator.save_image(image_data, args.output)

        if saved_path and args.show:
            generator.show_image(image_data)
    else:
        print("Failed to generate image.")
        sys.exit(1)

def interactive_mode():
    """
    Interactive mode for easier use
    """
    generator = AIImageGenerator()

    print("=== AI Image Generator ===")
    print("Enter your prompts (type 'quit' to exit)")

    while True:
        prompt = input("\nEnter prompt: ").strip()

        if prompt.lower() in ['quit', 'exit', 'q']:
            break

        if not prompt:
            continue

        # Ask for optional parameters
        style = input("Style (anime/realistic/cyberpunk/pixelart/fantasy) [press enter to skip]: ").strip()
        ratio = input("Aspect ratio (16:9/1:1/9:16/4:5) [press enter to skip]: ").strip()

        params = {}
        if style and style in ['anime', 'realistic', 'cyberpunk', 'pixelart', 'fantasy']:
            params['style'] = style
        if ratio and ratio in ['16:9', '1:1', '9:16', '4:5']:
            params['ratio'] = ratio

        # Generate image
        print("\nGenerating image...")
        image_data = generator.generate_image(prompt, **params)

        if image_data:
            filename = generator.save_image(image_data)
            if filename:
                try:
                    generator.show_image(image_data)
                except:
                    print("Could not display image automatically.")
        else:
            print("Failed to generate image.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, run interactive mode
        interactive_mode()
    else:
        # Arguments provided, run CLI mode
        main()
