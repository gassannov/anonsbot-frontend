import streamlit as st
from utils import chatting, invoke

if "ws" not in st.session_state:
    st.switch_page("🔐_Auth.py")

# --- ОБЩИЕ НАСТРОЙКИ ---
PAGE_TITLE: str = "Чат"
PAGE_ICON: str = "💬"

# Установка конфигурации страницы
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

# --- СОСТОЯНИЯ ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "ai",
        "content": "Привет! Чем я могу помочь? 🙂"
    }]

st.sidebar.image("./assets/artlebedev.png")
st.title("💬 Чат-бот Anons")
st.caption("🚀 Чат-бот анонсов студии на основе LLM")
chatting()

if prompt := st.chat_input("Спросите меня что-нибудь ⌨️"):
    invoke(prompt)
