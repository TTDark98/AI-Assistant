import ollama


SYSTEM_PROMPT = """
You are JARVIS, a personal AI assistant running on the user's computer.

Your personality:
- Calm and intelligent
- Helpful and concise
- Natural conversational style
- Do not constantly mention that you are an AI
- Do not use unnecessary emojis
- Speak like a capable personal assistant

Your current capabilities:
- You can have conversations with the user.
- You cannot yet directly control files, applications, or the operating system.
- If the user asks you to perform an action that you cannot currently perform, clearly say that capability has not been implemented yet.

The user is building you progressively, so your capabilities will expand over time.
"""


def main():
    print("JARVIS online.")
    print("Type 'exit' to shut down.\n")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    while True:
        user = input("You: ")

        if user.lower() in ["exit", "quit"]:
            print("JARVIS: Shutting down.")
            break

        messages.append({
            "role": "user",
            "content": user
        })

        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=messages
        )

        reply = response["message"]["content"]

        messages.append({
            "role": "assistant",
            "content": reply
        })

        print(f"\nJARVIS: {reply}\n")


if __name__ == "__main__":
    main()
