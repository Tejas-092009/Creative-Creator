import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_image(prompt, style):

    final_prompt = f"""
    Create a {style} based on the following.

    {prompt}

    High quality.

    Cinematic.

    Modern typography.

    4K.
    """

    response = client.models.generate_images(
        model="gemini-2.5-flash-image",
        prompt=final_prompt
    )

    output = "static/outputs/generated.png"

    image = response.generated_images[0].image

    image.save(output)

    return output
