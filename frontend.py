import streamlit as st
import requests
import random

# 🎨 Configuración de la página
st.set_page_config(page_title="Análisis de Sentimientos", layout="wide")

# 📌 Cargar CSS externo con depuración
def load_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"❌ ERROR: No se encontró el archivo {file_name}.")

# 📌 Cargar estilos
load_css("styles.css")

# 📌 Verificar si el chatbot ya estaba activado antes
if "mostrar_chatbot" not in st.session_state:
    st.session_state.mostrar_chatbot = False

# 📌 Dividimos la pantalla en 2 columnas
col1, col2 = st.columns([2, 1])

### **SECCIÓN DE ANÁLISIS DE SENTIMIENTO**
with col1:
    st.markdown('<h1 class="title">📝 Análisis de Sentimientos</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="title3">¿Cuéntanos, cómo te sientes hoy?</h3>', unsafe_allow_html=True)
    
    # 📌 Input para ingresar texto
    comentario = st.text_area(
        "✍️ Escribe un comentario:",
        placeholder="¿Qué piensas?",
    )

    # 📌 Diccionario de imágenes según el sentimiento detectado
    imagenes = {
        "positivo": "images/positivo.jpg",
        "negativo": "images/negativo.jpg",
        "neutral": "images/neutral.jpg"
    }

    # 📌 Mensajes motivacionales o interactivos según el sentimiento
    mensajes_motivacionales = {
        "positivo": "🎉 ¡Me alegra saber que te sientes bien! Sigue disfrutando tu día. 🌞",
        "neutral": "🙂 Parece que estás en un estado neutro. ¡Hagamos algo divertido!",
        "negativo": "😞 Parece que no te sientes bien. ¿Quieres hablar con alguien?"
    }

# 📌 Lista de frases motivacionales para estado neutral
frases_neutral = [
    "🌟 Cada día es una nueva oportunidad para aprender y crecer.",
    "🔄 No todos los días son emocionantes, pero cada uno es valioso.",
    "📖 Un día neutro es un capítulo en tu historia, ¡hazlo interesante!",
    "⏳ A veces la calma es necesaria para prepararnos para algo grande.",
    "💡 Usa este momento para reflexionar sobre lo que realmente quieres.",
]

# 🟢 Botón para analizar el comentario
if st.button("🔍 Analizar Sentimiento"):
    if comentario.strip():
        url = "http://127.0.0.1:5000/analizar"
        try:
            respuesta = requests.post(url, json={"comentario": comentario})
            if respuesta.status_code == 200:
                resultado = respuesta.json()
                sentimiento = resultado["sentimiento"]

                st.markdown(f"## 🎭 Sentimiento Detectado: **{sentimiento.capitalize()}**")
                st.image(imagenes[sentimiento], width=150)

                # Mostrar mensaje motivacional o chatbot según el sentimiento
                st.markdown(f"### {mensajes_motivacionales[sentimiento]}")

                if sentimiento == "negativo":
                    st.session_state.mostrar_chatbot = True  # Se activa el chatbot
                    st.markdown("**💬 Habla con nuestro chatbot** para recibir apoyo.")
                    st.markdown("---")  # Separador
                elif sentimiento == "neutral":
                    # Seleccionar aleatoriamente una frase motivacional
                    frase = random.choice(frases_neutral)
                    st.markdown(f"**💭 {frase}**")  # Muestra la frase motivacional
                    st.session_state.mostrar_chatbot = False  # No mostrar el chatbot

            else:
                st.error("❌ Error en el análisis. Intenta de nuevo.")
        except requests.exceptions.ConnectionError:
            st.error("❌ No se pudo conectar con el backend. ¿Está corriendo Flask?")
    else:
        st.warning("⚠️ Escribe un comentario para analizar.")

### **SECCIÓN DEL CHATBOT (Solo se muestra si el sentimiento es negativo)**
if st.session_state.mostrar_chatbot:
    st.markdown('<div class="chatbot-box">', unsafe_allow_html=True)
    st.markdown('<div class="chat-title">🤖 Chatbot de Apoyo Emocional</div>', unsafe_allow_html=True)

    # 📌 Historial del chatbot
    if "chat_historial" not in st.session_state:
        st.session_state.chat_historial = []

    if len(st.session_state.chat_historial) > 0:
        st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
        for msg in st.session_state.chat_historial:
            st.markdown(msg)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("💬 Escribe algo para comenzar la conversación.")

    # 📌 Input para el chatbot
    mensaje_usuario = st.text_input("💬 Escribe tu mensaje aquí:", key="chat_input")

    # 🟢 Botón para enviar mensaje
    if st.button("✉️ Enviar Mensaje"):
        if mensaje_usuario.strip():
            url = "http://127.0.0.1:5000/chatbot"
            try:
                respuesta = requests.post(url, json={"mensaje": mensaje_usuario})
                if respuesta.status_code == 200:
                    resultado = respuesta.json()
                    mensaje = resultado["mensaje"]
                    respuesta_chatbot = resultado["respuesta"]
                    sentimiento = resultado["sentimiento"]

                    # Agregar el mensaje del usuario y la respuesta en el orden correcto
                    st.session_state.chat_historial.append(f"🧑‍💻 Tú: {mensaje}")  
                    st.session_state.chat_historial.append(f"🤖 Chatbot ({sentimiento.capitalize()}): {respuesta_chatbot}")  

                    # 📌 Limpiar el input después de enviar el mensaje
                    st.rerun()

                else:
                    st.error("❌ Error en la respuesta del chatbot.")
            except requests.exceptions.ConnectionError:
                st.error("❌ No se pudo conectar con el backend. ¿Está corriendo Flask?")
        else:
            st.warning("⚠️ Escribe un mensaje para interactuar con el chatbot.")

    st.markdown('</div>', unsafe_allow_html=True)

# 📌 Pie de página con estilo
st.markdown("---")
st.markdown('<p class="footer">Desarrollado con ❤️ por Ale</p>', unsafe_allow_html=True)
