import streamlit as st
from deep_translator import GoogleTranslator

# Predefined language dictionary to avoid API rate limiting
LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "hi": "Hindi",
    "telugu": "Telugu",
    "tamil": "Tamil",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ar": "Arabic",
    "ru": "Russian",
    "pt": "Portuguese"
}

# Application title
st.title("🌐 Language Translation Tool")
st.write("Translate text easily between different languages.")

# Create input area for text
user_text = st.text_area("Enter text to translate:", height=150)

# Language selection dropdowns
col1, col2 = st.columns(2)
with col1:
    src_display = st.selectbox("Source Language", options=list(LANGUAGES.values()), index=0)
with col2:
    tgt_display = st.selectbox("Target Language", options=[v for k, v in LANGUAGES.items() if k != "auto"], index=0)

# Map selected display names back to language codes
src_code = [k for k, v in LANGUAGES.items() if v == src_display][0]
tgt_code = [k for k, v in LANGUAGES.items() if v == tgt_display][0]

# Action button
if st.button("Translate"):
    if user_text.strip():
        try:
            # Perform translation
            translated = GoogleTranslator(source=src_code, target=tgt_code).translate(user_text)

            # Display output
            st.subheader("Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")
