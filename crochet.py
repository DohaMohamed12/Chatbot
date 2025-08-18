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
    <p style='text-align:center;color:gray;'>اسأل أي حاجة عن الكروشيه وخليك جاهز لأجوبة فورية من الموديل 🪡</p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# text area for longer prompts
user_input = st.text_area("اكتب سؤالك هنا:", height=150)

# when user clicks the button
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b:fireworks-ai",
                messages=[{"role": "user", "content": user_input}],
            )

        st.write("### Response:")
        # instead of st.success (green background), just write the raw message:
        st.write(completion.choices[0].message.content)
    else:
        st.warning("Please enter a question before sending.")
