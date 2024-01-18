import streamlit as st
import requests

# Function to send text to the genAI API for speech synthesis
def synthesize_speech_with_genai(text):
    genai_api_url = "https://api.genai.com/speech-synthesis"
    genai_api_key = "YOUR_GENAI_API_KEY"  # Replace with your actual genAI API key

    headers = {
        "Authorization": f"Bearer {genai_api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "text": text,
    }

    response = requests.post(genai_api_url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("audio_url", None)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Streamlit app
def main():
    st.title("Speech Synthesis with genAI")

    # Input text
    text_to_synthesize = st.text_area("Enter text for speech synthesis", "")

    # Button to trigger speech synthesis
    if st.button("Synthesize Speech"):
        if text_to_synthesize:
            st.info("Synthesizing speech...")

            # Call genAI API for speech synthesis
            audio_url = synthesize_speech_with_genai(text_to_synthesize)

            if audio_url:
                st.audio(audio_url, format="audio/wav", start_time=0)
                st.success("Speech synthesis complete!")
            else:
                st.error("Failed to synthesize speech.")
        else:
            st.warning("Please enter text for speech synthesis.")

if __name__ == "__main__":
    main()
