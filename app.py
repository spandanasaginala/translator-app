import streamlit as st
from deep_translator import GoogleTranslator

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

st.title("🌐 Language Translation Tool")
st.write("Translate text easily between different languages.")

user_text = st.text_area("Enter text to translate:", height=150)

col1, col2 = st.columns(2)
with col1:
    src_display = st.selectbox("Source Language", options=list(LANGUAGES.values()), index=0)
with col2:
    tgt_display = st.selectbox("Target Language", options=[v for k, v in LANGUAGES.items() if k != "auto"], index=0)

src_code = [k for k, v in LANGUAGES.items() if v == src_display][0]
tgt_code = [k for k, v in LANGUAGES.items() if v == tgt_display][0]

if st.button("Translate"):
    if user_text.strip():
        try:
            translated = GoogleTranslator(source=src_code, target=tgt_code).translate(user_text)
            st.subheader("Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")
