import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You can provide answer of any question"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chatbot")

demo.launch(share=True)