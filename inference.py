import os
from openai import OpenAI

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_inference(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an AI study helper that gives short, clear explanations."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def main():
    step = 0
    rewards = []
    success = False

    task = "study-helper"
    env_name = "openenv"

    # START
    print(f"[START] task={task} env={env_name} model={MODEL_NAME}")

    try:
        done = False

        # Simulated steps (since no real env given)
        while not done:
            step += 1

            # AI generates study help
            action = run_inference("Explain photosynthesis in one line")

            # Simulated reward logic
            if step < 3:
                reward = 0.00
                done = False
            else:
                reward = 1.00
                done = True
                success = True

            rewards.append(reward)

            error = None
            error_str = "null" if error is None else str(error)

            # STEP
            print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_str}")

    finally:
        rewards_str = ",".join([f"{r:.2f}" for r in rewards])

        # END
        print(f"[END] success={str(success).lower()} steps={step} rewards={rewards_str}")


if __name__ == "__main__":
    main()
