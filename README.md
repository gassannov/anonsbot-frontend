# anonsbot-fronend
![haf](https://eponym.ru/GaleryImages/S9NO0IJWOT0YBFPFPXPTWFFEI.gif)

### Навигация:
1. [Overview](#overview) -  краткий обзор репо;
2. [Setup & Run](#setup--run) - установка и запуск;
3. [TO DO](#to-do) - что можно улучшить;
4. [a few tips](#a-few-tips) - пара советов;


# Overview 
anonsbot-fronend - фронтовая часть [чат-бота](https://anonsbot.streamlit.app/) нашей студии, написанная на  фрэймворке [streamlit](https://streamlit.io/). Если ты уже видел [репу](https://github.com/artlebedev/anonsbot) с серверной и ML логикой RAG системы, то будет проще, в противном случае рекомендую сначала ознакомиться с ней.

Общение с бэковой частью происходит по веб сокет соединению, этот протокол обычно используют в чатах и мессенджерах.

Для входа нужно вставить ключ авторизации. Кода здесь заметно меньше, чем в бэковой части, а логика проще, поэтому разобраться будет легче. 


#  Setup & Run
1. Клонь репу
```bash 
git clone git@github.com:artlebedev/anonsbot-frontend.git
```
2. Установи зависимости
```bash 
pip3 install -r requirements.txt
```
3. И можно запускать, указав точку входа приложения, `🔐_Auth.py` в нашем случае.
```bash 
streamlit run 🔐_Auth.py
```

# TO DO
Сейчас приложения хоститься на серверах streamlit от моего, аккаунта. Это удобно при разработке, так как ты сам быстро можешь вносить изменения и перезапускать фронт. 

Однако, тебе нужно перенести хост либо на сервера студии (докер файл уже написан), либо запустить его от своего аккаунта в облаке streamlit.

 Это не сложно и есть подробный [гайд](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app). Дай мне знать, когда вы не будете зависеть от моего ака и я смогу спокойно снести приложение. Мой тг: @yeamerci


# a few tips
- Изначально пытался запускать фронт на серверах hpc, но с этим возникли проблемы, поэтому лучше не тратить на это время
