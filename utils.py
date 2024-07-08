"""
Утилиты для создания пользовательского интерфейса чат-бота
"""

__all__ = [
    "chatting",
    "connect",
    "auth",
    "invoke"
]

import streamlit as st
import requests
import websocket


def chatting() -> None:
    """
    Отображение сообщений чата.

    Эта функция отображает сообщения чата в пользовательском интерфейсе Streamlit.

    :return: None
    """
    for message in st.session_state.messages:
        entity = st.chat_message(message["role"])
        entity.write(message["content"])


def connect(attempts: int = 1) -> None:
    """
    Подключение к API через WebSocket.

    Эта функция устанавливает соединение WebSocket с сервером API.

    :param attempts: Количество попыток подключения (по умолчанию 1).
    :type attempts: int
    :return: None
    """
    api_key = st.session_state.get("api_key", None)
    if api_key is None:
        st.info("API-ключ не был предоставлен.")
        st.stop()

    ws = websocket.WebSocket()
    with st.spinner(text="Подключение к API..."):
        for _ in range(attempts):
            try:
                ws.connect(
                    url="ws://p2.msk-1.hpc-park.ru:36509/ws",
                    header={"api_key": api_key}
                )
            except Exception as e:
                print(f"Ошибка: {e}")
                st.error("Ошибка подключения к API. Попробуйте позже.")
            else:
                st.session_state["ws"] = ws
                return st.success("Успешное подключение к API")


def auth() -> None:
    """
    Аутентификация пользователя.

    Эта функция запрашивает у пользователя ввод его API-ключа и инициирует подключение к API.

    :return: None
    """
    st.title("Авторизация")
    st.caption("🚀 Войдите, чтобы начать чат")
    if api_key := st.text_input(
            label="Введите ваш API-ключ 🔑",
            type="password",
            value=None
    ):
        st.session_state["api_key"] = api_key
        connect()


def invoke(prompt: str) -> None:
    """
    Вызов модели искусственного интеллекта с пользовательским запросом.

    Эта функция отправляет пользовательский запрос модели искусственного интеллекта через соединение WebSocket и отображает ответ.

    :param prompt: Пользовательский запрос.
    :type prompt: str
    :return: None
    """
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    ws = st.session_state["ws"]
    try:
        ws.send(prompt)
        with st.spinner("Думаем..."):
            response = ws.recv()
    except Exception as e:
        print(f"Ошибка: {e}")
        st.warning("Потеряно соединение с удаленным хостом. Попробуйте переподключиться...")
        st.session_state.messages.pop()
        connect()
    else:
        st.chat_message("ai").write(response)
        st.session_state.messages.append({"role": "ai", "content": response})
# ```

# Если есть что-то, что нужно дополнить или изменить, пожалуйста, дайте мне знать.
