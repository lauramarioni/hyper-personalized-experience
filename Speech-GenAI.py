import streamlit as st
import openai
from gtts import gTTS
import os

# Load the .env file
load_dotenv()
 
# Get the API key
openai_key = os.environ.get("OPENAI_KEY")
openai.api_key = openai_key

# Function to interact with GenAI for chatbot responses
def chat_with_genai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to convert text to speech using gTTS
def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Windows command, use appropriate command for other platforms

# Streamlit app
def main():
    st.title("GenAI Chatbot with Speech Synthesis")

    # User input
    user_input = st.text_input("Ask the chatbot:")

    if st.button("Ask"):
        # Get GenAI response
        genai_response = chat_with_genai(user_input)

        # Display GenAI response
        st.text("GenAI Response:")
        st.write(genai_response)

        # Convert GenAI response to speech
        st.text("Speech Synthesis:")
        text_to_speech(genai_response)

# Run the Streamlit app
if __name__ == "__main__":
    main()
