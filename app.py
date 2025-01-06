import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

import google.generativeai as genai

genai.configure(api_key=google_gemini_api_key)

st.set_page_config(layout="wide")

st.title('Generate your Blog')
st.subheader('Now you can generate blog with the help of AI')

import google.generativeai as genai

genai.configure(api_key=google_gemini_api_key)

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

with st.sidebar:
    st.title("Input Blog Details")
    st.subheader("Enter Details of the BLog you want to generate")

    blog_title=st.text_area("Keywords")

    num_words=st.slider("number of words",min_value=100,max_value=1000, step=100)

    ##num_images=st.number_input("number of images",min_value=1, max_value=5, step=1)

    submit_button=st.button("Generate Blog")

    response = chat_session.send_message("Generate a comprehensive, engaging blog post relevant to the given title Effects of Genrative aicontent and keywords. The blog should be suitable for an online audience. ensure the content is original, information and maintains a consistent tone throughout.")

if submit_button:
    st.write(response.text)



