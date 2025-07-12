#!/usr/bin/env python3
"""
AI Image Generator integration for your Telegram bot
Add this to your Bot/API/ directory
"""

import requests
import os
import logging
from urllib.parse import quote
import random
from io import BytesIO

class AIImageAPI:
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt"
        self.output_dir = "Bot/API/generated_images"
        os.makedirs(self.output_dir, exist_ok=True)

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def generate_image(self, prompt, user_id=None, **options):
        """
        Generate AI image for Telegram bot

        Args:
            prompt (str): Image description
            **options: Generation options

        Returns:
            dict: Result with success status and file path or error
        """
        try:
            # Parameters
            width = options.get('width', 1024)
            height = options.get('height', 1024)
            seed = options.get('seed', random.randint(1, 100000))
            model = options.get('model', 'flux')
            style = options.get('style', '')
            safe_mode = options.get('safe', True)

            # Build prompt
            final_prompt = prompt
            if style:
                final_prompt += f", {style} style"

            # Build API URL
            encoded_prompt = quote(final_prompt)
            api_url = f"{self.base_url}/{encoded_prompt}"
            params = {
                'width': width,
                'height': height,
                'seed': seed,
                'model': model,
                'nologo': 'true',
                'private': 'false',
                'enhance': 'false',
                'safe': 'true' if safe_mode else 'false'
            }

            param_string = "&".join([f"{k}={v}" for k, v in params.items()])
            full_url = f"{api_url}?{param_string}"

            self.logger.info(f"Generating image for user {user_id}: '{prompt}'")

            # Make request
            response = requests.get(full_url, timeout=60)
            response.raise_for_status()

            # Validate response
            if not response.headers.get('content-type', '').startswith('image/'):
                return {
                    'success': False,
                    'error': 'Invalid response from AI service'
                }

            # Save image
            filename = f"ai_{user_id}_{seed}.png" if user_id else f"ai_{seed}.png"
            filepath = os.path.join(self.output_dir, filename)

            with open(filepath, 'wb') as f:
                f.write(response.content)

            return {
                'success': True,
                'filepath': filepath,
                'filename': filename,
                'prompt': final_prompt,
                'seed': seed
            }

        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Image generation timed out. Please try again.'
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Network error: {str(e)}'
            }
        except Exception as e:
            self.logger.error(f"Error generating image: {e}")
            return {
                'success': False,
                'error': 'Failed to generate image. Please try again.'
            }

    def generate_image_stream(self, prompt, **options):
        """
        Generate image and return as BytesIO stream (for direct Telegram sending)

        Args:
            prompt (str): Image description
            **options: Generation options

        Returns:
            BytesIO or None: Image stream if successful
        """
        result = self.generate_image(prompt, **options)

        if result['success']:
            try:
                with open(result['filepath'], 'rb') as f:
                    return BytesIO(f.read())
            except Exception as e:
                self.logger.error(f"Error reading generated image: {e}")
                return None

        return None

    def cleanup_old_images(self, max_age_hours=24):
        """
        Clean up old generated images

        Args:
            max_age_hours (int): Maximum age in hours before deletion
        """
        import time

        current_time = time.time()
        max_age_seconds = max_age_hours * 3600

        try:
            for filename in os.listdir(self.output_dir):
                filepath = os.path.join(self.output_dir, filename)
                if os.path.isfile(filepath):
                    file_age = current_time - os.path.getctime(filepath)
                    if file_age > max_age_seconds:
                        os.remove(filepath)
                        self.logger.info(f"Removed old image: {filename}")
        except Exception as e:
            self.logger.error(f"Error cleaning up images: {e}")

# Example integration with your bot
# def integrate_with_bot():
#     """
#     Example of how to integrate with your existing bot
#     """
#     ai_generator = AIImageAPI()

#     # Example function for your bot command
#     def handle_generate_image_command(update, context):
#         """
#         Telegram bot command handler
#         """
#         user_id = update.effective_user.id

#         # Get prompt from command
#         if not context.args:
#             update.message.reply_text("Please provide a prompt. Example: /generate a cat in space")
#             return

#         prompt = " ".join(context.args)

#         # Send "generating" message
#         generating_msg = update.message.reply_text("🎨 Generating your image...")

#         # Generate image
#         result = ai_generator.generate_image(prompt, user_id)

#         if result['success']:
#             # Send the generated image
#             with open(result['filepath'], 'rb') as photo:
#                 update.message.reply_photo(
#                     photo=photo,
#                     caption=f"Generated image for: '{result['prompt']}'\nSeed: {result['seed']}"
#                 )
#             # Delete the generating message
#             generating_msg.delete()
#         else:
#             generating_msg.edit_text(f"❌ Error: {result['error']}")

#     return handle_generate_image_command
