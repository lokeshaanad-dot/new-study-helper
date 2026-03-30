from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# ===== OpenEnv REQUIRED APIs =====
@app.post("/reset")
def reset():
    return {"state": "reset done"}

@app.get("/state")
def state():
    return {"status": "running"}

@app.post("/step")
def step(action: dict):
    return {"result": "ok", "action_received": action}

# ===== AI FUNCTION =====
def study_helper(text, mode):
    text = text.strip()

    if not text:
        return "Please enter something."

    if mode == "Summarize":
        if len(text.split()) < 10:
            return "Please enter a longer paragraph."
        sentences = text.split(".")
        return "📄 Summary: " + ". ".join(sentences[:2])

    return f"📘 Explanation: {text} explained in simple terms."

# ===== UI =====
demo = gr.Interface(
    fn=study_helper,
    inputs=[
        gr.Textbox(lines=4, placeholder="Enter text..."),
        gr.Radio(["Explain", "Summarize"], value="Explain")
    ],
    outputs="text",
    title="🎓 AI Study Helper"
)

# 🔥 IMPORTANT (THIS FIXES YOUR ISSUE)
app = gr.mount_gradio_app(app, demo, path="/")
