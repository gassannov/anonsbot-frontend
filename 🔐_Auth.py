"""
Точка входа в приложение
"""

from utils import auth
import streamlit as st
from websocket import WebSocket


# --- ОБЩИЕ НАСТРОЙКИ ---
PAGE_TITLE: str = "Аутентификация"
PAGE_ICON: str = "🔐"


# Установка конфигурации страницы
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)


if "ws" not in st.session_state:
    auth()
if isinstance(st.session_state.get("ws", None), WebSocket):
    st.switch_page("./pages/💬_Чат.py")
