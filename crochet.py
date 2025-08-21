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

# ===== Custom CSS =====
st.markdown(
    """
    <style>
        /* الخلفية الأساسية */
        .stApp {
            background-color: #ffffff;
        }
        .block-container {
            background-color: #ffffff;
        }
        /* صندوق الكتابة */
        .stTextArea textarea {
            border-radius: 12px;
            border: 2px solid #dc3c3c;
            padding: 12px;
            font-size: 16px;
            background-color: #ffffff;
        }
        /* زر الإرسال */
        .send-btn {
            background-color: #dc3c3c;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
        }
        .send-btn:hover {
            background-color: #b83030;
        }
        /* محاذاة الوسط */
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== Header =====
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st.image("logo.png", width=150)
st.markdown(
    "<p style='text-align:center; color:#dc3c3c; font-size:18px; font-weight:bold;'>CREATE THEIR HAPPY MEMORIES</p>",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# ===== Input Box =====
col1, col2 = st.columns([8,1])

with col1:
    user_input = st.text_area(" ", placeholder="Type your message here...", height=80, label_visibility="collapsed")

with col2:
    send_clicked = st.button("➤", key="send", help="Send message")

# ===== Handle Input =====
if send_clicked:
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
