import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_video(video_path):

    uploaded = client.files.upload(file=video_path)

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=[
            uploaded,
            """
            Watch this video.

            Return:

            1. One sentence summary

            2. Key objects

            3. Mood

            4. Colors

            5. Visual composition

            6. A detailed image-generation prompt suitable for creating an eye-catching promotional poster.
            """
        ]
    )

    return response.text
