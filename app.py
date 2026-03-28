import gradio as gr

def study_helper(text, mode):
    text = text.strip()

    if not text:
        return "Please enter a question."

    # SUMMARIZE MODE
    if mode == "Summarize":
        if len(text.split()) < 10:
            return "Please enter a longer paragraph to summarize."
        
        sentences = text.split(".")
        summary = ". ".join(sentences[:2]).strip()
        return "📄 Summary: " + summary + "."

    # EXPLAIN MODE
    text_lower = text.lower()

    if "accountancy" in text_lower:
        return "📘 Accountancy is the process of recording and managing financial transactions."

    elif "economics" in text_lower:
        return "📊 Economics studies how resources are produced, distributed, and used."

    elif "marketing" in text_lower:
        return "📢 Marketing is the process of promoting and selling products or services."

    elif "photosynthesis" in text_lower:
        return "🌱 Photosynthesis is the process by which plants make food using sunlight."

    elif "balance sheet" in text_lower:
        return "📑 A balance sheet shows assets, liabilities, and capital of a business."

    else:
        return f"🤖 {text.capitalize()} is explained in simple and easy terms for better understanding."

interface = gr.Interface(
    fn=study_helper,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question or paste paragraph..."),
        gr.Radio(["Explain", "Summarize"], value="Explain", label="Choose Mode")
    ],
    outputs="text",
    title="🎓 Smart AI Study Assistant",
    description="Explain concepts or summarize long text easily"
)

interface.launch()
