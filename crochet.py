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

        /* اللوجو والجملة */
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 40px;
        }
        .tagline {
            text-align: center;
            color: #dc3c3c;
            font-size: 22px;
            font-weight: bold;
            margin-top: 10px;
        }

        /* صندوق الكتابة */
        .chat-box {
            position: relative;
            margin-top: 50px;
        }
        .chat-input textarea {
            border-radius: 20px;
            border: 2px solid #ccc;
            padding: 10px 40px 10px 15px;
            font-size: 15px;
            resize: none;
            height: 50px !important; /* أرفع */
        }

        /* أيقونة الإرسال جوه الصندوق */
        .send-icon {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: gray;
            font-size: 18px;
            cursor: pointer;
        }
        .send-icon:hover {
            color: #dc3c3c;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== Header =====
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st.image("logo.png", width=150)
st.markdown("<p class='tagline'>CREATE THEIR HAPPY MEMORIES</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# ===== Input Box =
