import base64
import os
import cv2
import requests
from io import BytesIO
from PIL import Image

api_key = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

language = input("select language: ")

def capture_and_encode_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Convert to PIL Image
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)

        # Convert to base64
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()

    return None


base64_image = capture_and_encode_image()

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "You are a Translator, your job is to translate the objects you see in the photo. Focus on one specific object that is in the center of the frame. Reply with what the object is in one or two words. For example, if the person is holding a blue pen, reply blue pen, in the selected language which is, " + language
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 50
}

def speak(text):
    audio = elevenlabs.generate(
        text=text,
        voice="Natasha - Valley girl",
        model = "eleven_multilingual_v2"
    )
    elevenlabs.save(audio, "response.mp3")
    elevenlabs.play(audio)
    os.remove("response.mp3")

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

response_json = response.json()

if response_json.get("choices"):
    description = response_json["choices"][0].get("message", {}).get("content", "")
    speak(description)
    print(description)
else:
    print("No description available in the response.")




