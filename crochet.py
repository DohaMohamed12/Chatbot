import streamlit as st
import os
from openai import OpenAI

# Create client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---- PAGE LAYOUT ----
st.set_page_config(page_title="Crochet Hub Chatbot", layout="centered")

# custom header
st.markdown(
    """
    <h1 style='text-align:center;'>🧶 Crochet Hub Chatbot</h1>
    <p style='text-align:center;color:gray;'>Ask anything about crochet and get instant answers 🧵</p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# text area for longer prompts
user_input = st.text_area("Your question:", height=150)

# when user clicks the button
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b:fireworks-ai",
                messages=[{"role": "user", "content": user_input}],
            )

        # split answer by line and show each line separately
        answer = completion.choices[0].message.content
        for line in answer.split("\n"):
            if line.strip() != "":
                st.write(line)
    else:
        st.warning("Please enter a question before sending.")
