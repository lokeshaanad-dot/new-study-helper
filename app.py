import gradio as gr

def chat(user_input):
    return f"📘 Study Answer:\n{user_input} → Try to understand basics first, then practice examples."

iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(placeholder="Ask your study question..."),
    outputs="text",
    title="AI Study Helper Chatbox"
)

iface.launch()
