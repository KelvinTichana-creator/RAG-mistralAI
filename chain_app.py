import chainlit as cl
import requests

API_URL = 'https://ffa87398fe8de1d7654fd29f4a1efadf.serveo.net/query'  # or flask-ngrok URL

chat_history = []
processing = False

@cl.on_message
async def main(message: cl.Message):
    global processing

    if processing:
        await cl.Message(content="Please wait until the current query is processed.").send()
        return

    query = message.content
    processing = True

    await cl.Message(content="Processing your query...").send()

    # Call the Flask API
    response = requests.post(API_URL, json={'question': query, 'chat_history': chat_history})
    data = response.json()
    answer = data.get('answer', 'No answer found.')

    chat_history.append((query, answer))

    await cl.Message(content=f"Answer: {answer}").send()

    processing = False

