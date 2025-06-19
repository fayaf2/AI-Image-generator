import openai
import requests
import shutil

# Replace with your OpenAI API key
openai.api_key = "your-openai-api-key"

def generate_image(prompt, output_path="generated_image.png"):
    try:
        # Request image from OpenAI
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        
        # Get image URL
        image_url = response['data'][0]['url']
        
        # Download the image
        img_response = requests.get(image_url, stream=True)
        if img_response.status_code == 200:
            with open(output_path, 'wb') as f:
                shutil.copyfileobj(img_response.raw, f)
            print(f"Image saved to {output_path}")
        else:
            print("Failed to download image")

    except Exception as e:
        print("Error:", e)

# Example usage
prompt = "a futuristic cityscape at night with flying cars"
generate_image(prompt)
