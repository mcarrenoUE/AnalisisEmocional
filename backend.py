from flask import Flask, request, jsonify
import mysql.connector
import nltk
import random
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Inicializar Flask
app = Flask(__name__)

# Conectar a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia esto si usas contraseña
    database="sentimentDB"
)
cursor = db.cursor()

# Descargar recursos de NLTK
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Variables de estado para recordar la conversación
if "ultimo_sentimiento" not in globals():
    ultimo_sentimiento = None
if "ultimo_mensaje" not in globals():
    ultimo_mensaje = None


def preprocesar_texto(texto):
    """
    1. Convierte a minúsculas
    2. Corrige errores ortográficos
    """
    texto = texto.lower()  # Convertir a minúsculas
    texto = TextBlob(texto).correct()  # Corregir ortografía
    return str(texto)  # Convertir a string nuevamente


@app.route('/analizar', methods=['POST'])
def analizar_sentimiento():
    datos = request.json
    texto = datos.get("comentario", "")

    if not texto:
        return jsonify({"error": "No se recibió comentario"}), 400

    # Preprocesar texto
    texto_procesado = preprocesar_texto(texto)

    # Analizar sentimiento
    resultado = sia.polarity_scores(texto_procesado)
    sentimiento = "positivo" if resultado['compound'] > 0 else "negativo" if resultado['compound'] < 0 else "neutral"

    # Guardar en la BD
    sql = "INSERT INTO comentarios (texto, sentimiento) VALUES (%s, %s)"
    cursor.execute(sql, (texto, sentimiento))
    db.commit()

    return jsonify({"comentario": texto, "texto_procesado": texto_procesado, "sentimiento": sentimiento})


@app.route('/chatbot', methods=['POST'])
def chatbot():
    global ultimo_sentimiento, ultimo_mensaje

    datos = request.json
    mensaje = datos.get("mensaje", "")

    if not mensaje:
        return jsonify({"respuesta": "No entendí lo que dijiste 🤖"}), 400

    # Preprocesar el texto
    mensaje_procesado = preprocesar_texto(mensaje)

    # Analizar sentimiento del mensaje
    resultado = sia.polarity_scores(mensaje_procesado)
    sentimiento = "positivo" if resultado['compound'] > 0 else "negativo" if resultado['compound'] < 0 else "neutral"

    # 📌 Evitar respuestas repetitivas
    if mensaje == ultimo_mensaje:
        return jsonify({"mensaje": mensaje, "sentimiento": sentimiento, "respuesta": "Interesante... dime más sobre eso. 🤔"})

    # 📌 Respuestas más naturales y variadas
    respuestas = {
        "positivo": [
            "¡Eso suena genial! 😊",
            "¡Qué buena noticia! 🎉 ¿Qué es lo que más te hace feliz en este momento?",
            "¡Me alegra escuchar eso! ¿Hay algo especial que hayas hecho hoy?"
        ],
        "negativo": [
            "Oh, lo siento mucho. 😔 ¿Quieres hablar sobre lo que te preocupa?",
            "A veces, compartir cómo te sientes puede ayudar. ¿Hay algo en lo que pueda apoyarte?",
            "Recuerda que no estás solo/a. 💙 ¿Hay algo que puedas hacer para sentirte mejor?"
        ],
        "neutral": [
            "Entiendo. ¿Tienes algo más en mente de lo que quieras hablar? 🤖",
            "Cada día puede traernos cosas nuevas. ¿Tienes algo en mente que te preocupe o emocione?",
            "Gracias por compartir eso. ¿Hay algo más en lo que pueda ayudarte?"
        ]
    }

    # 📌 Seleccionar una respuesta aleatoria
    respuesta_chatbot = random.choice(respuestas[sentimiento])

    # Guardar el último mensaje y sentimiento
    ultimo_sentimiento = sentimiento
    ultimo_mensaje = mensaje

    return jsonify({"mensaje": mensaje, "sentimiento": sentimiento, "respuesta": respuesta_chatbot})


if __name__ == '__main__':
    app.run(debug=True)
