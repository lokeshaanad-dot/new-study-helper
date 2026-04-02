import gradio as gr
from openai import OpenAI
import os

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def study_helper(user_input):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an AI study helper. Give short answers."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


iface = gr.Interface(
    fn=study_helper,
    inputs=gr.Textbox(placeholder="Ask your study question..."),
    outputs="text",
    title="AI Study Helper"
)

iface.launch()
