# Photo Translator
Real-Time Photo Describer and Translator with Speech Output

This project is designed to capture an image from a camera, translate the main object in the image into a specified language using GPT-4V, and then generate an audio output of the translated text using ElevenLabs' API.

## Features

- **Image Capture**: Uses OpenCV to capture an image from the webcam.
- **Image Processing**: Converts the captured image to a base64 encoded string for processing.
- **Translation**: Sends the encoded image to OpenAI's GPT-4V, requesting a description of the central object in the specified language.
- **Audio Output**: Utilizes ElevenLabs API to convert the translated text into spoken audio.

You need to have API keys for OpenAI and ElevenLabs
You need to install the required packages (pip install opencv-python-headless pillow requests elevenlabs)



