import streamlit as st
from googletrans import LANGUAGES, Translator

# Initialize translator
translator = Translator()

# Application title
st.title("🌐 Language Translation Tool")
st.write("Translate text easily between different languages.")

# Create input area for text
user_text = st.text_area("Enter text to translate:", height=150)

# Language selection dropdowns
languages_list = list(LANGUAGES.values())

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox(
        "Source Language", options=["auto"] + languages_list, index=0
    )
with col2:
    tgt_lang = st.selectbox("Target Language", options=languages_list, index=21)

# Action button
if st.button("Translate"):
    if user_text.strip():
        # Get language codes
        src_code = (
            "auto"
            if src_lang == "auto"
            else list(LANGUAGES.keys())[languages_list.index(src_lang)]
        )
        tgt_code = list(LANGUAGES.keys())[languages_list.index(tgt_lang)]

        # Perform translation
        try:
            translation = translator.translate(
                user_text, src=src_code, dest=tgt_code
            )

            # Display output
            st.subheader("Translated Text:")
            st.success(translation.text)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")