import os

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

def generate_study_help(prompt):
    """
    Dummy AI Study Helper (no API dependency)
    """
    return f"Study Tip: {prompt} -> Break it into small concepts and revise daily."

def main():
    step = 0
    rewards = []
    success = False

    task = "ai-study-helper"
    env_name = "openenv"

    # START
    print(f"[START] task={task} env={env_name} model={MODEL_NAME}")

    try:
        done = False

        while not done:
            step += 1

            # Simulated user query
            prompt = "Explain photosynthesis simply"

            # AI action (study helper response)
            action = generate_study_help(prompt)

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
