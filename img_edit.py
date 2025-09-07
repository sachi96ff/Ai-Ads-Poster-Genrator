from google import genai
from google.genai.types import GenerateContentConfig, Modality
from PIL import Image
from io import BytesIO

API_KEY = "AIzaSyBMS4DnmOwG1BM8S_AKzMr_Skulu1qzUbs"

client = genai.Client(api_key=API_KEY)

# 1. Load your image
image = Image.open("test.png")

# 2. Prepare editing prompt
prompt = input('Enter Prompt')

# 3. Call Gemini 2.5 Flash Image Preview for editing
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[image, prompt],
    config=GenerateContentConfig(response_modalities=[Modality.TEXT, Modality.IMAGE]),
)

# 4. Save the edited image
for part in response.candidates[0].content.parts:
    if part.inline_data:
        edited = Image.open(BytesIO(part.inline_data.data))
        edited.save("edited_image.png")
        print("Edited image saved as edited_image.png")
