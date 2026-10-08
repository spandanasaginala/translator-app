import streamlit as st
from deep_translator import GoogleTranslator

# Initialize language options
translator_instance = GoogleTranslator(source="auto", target="en")
supported_languages = translator_instance.get_supported_languages(as_dict=True)

# Application title
st.title("🌐 Language Translation Tool")
st.write("Translate text easily between different languages.")

# Create input area for text
user_text = st.text_area("Enter text to translate:", height=150)

# Language selection dropdowns
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox(
        "Source Language", options=["auto"] + list(supported_languages.keys())
    )
with col2:
    tgt_lang = st.selectbox(
        "Target Language", options=list(supported_languages.keys()), index=27
    )

# Action button
if st.button("Translate"):
    if user_text.strip():
        try:
            # Configure translator
            src_code = "auto" if src_lang == "auto" else src_lang
            translated = GoogleTranslator(
                source=src_code, target=tgt_lang
            ).translate(user_text)

            # Display output
            st.subheader("Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")
