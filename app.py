import logging
from pathlib import Path
from typing import List, Tuple, Optional

from dotenv import load_dotenv

load_dotenv()

import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema import BaseMessage, HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODELS_NAMES = ["gpt-3.5-turbo", "gpt-4"]
DEFAULT_TEMPERATURE = 0.7

ChatHistory = List[str]

logging.basicConfig(
    format="[%(asctime)s %(levelname)s]: %(message)s", level=logging.INFO
)
# load up our system prompt
system_message = SystemMessage(content=Path("prompts/system.prompt").read_text())
# for the human, we will just inject the text
human_message_prompt_template = HumanMessagePromptTemplate.from_template("{text}")


def message_handler(
    chat: Optional[ChatOpenAI],
    message: str,
    chatbot_messages: ChatHistory,
    messages: List[BaseMessage],
):
    if chat is None:
        # let's create our default chat
        chat = ChatOpenAI(model_name=MODELS_NAMES[0], temperature=DEFAULT_TEMPERATURE, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
    logging.info("asking question to GPT")
    messages.append(HumanMessage(content=message))
    reply = chat(messages)
    messages.append(reply)
    logging.debug(f"reply = {reply.content}")
    logging.info(f"Done!")
    chatbot_messages.append((message, messages[-1].content))
    return chat, "", chatbot_messages, messages


def on_clear_click() -> Tuple[str, List, List]:
    return "", [], []

def on_apply_settings_click(model_name: str, temperature: float):
    logging.info(f"Applying settings: model_name={model_name}, temperature={temperature}")
    chat = ChatOpenAI(model_name=model_name, temperature=temperature)
    return chat, *on_clear_click()

with gr.Blocks() as demo:
    # here we keep our state so multiple user can use the app at the same time!
    messages = gr.State([system_message])
    chat = gr.State(None)

    with gr.Column():
        gr.Markdown("# Welcome to my Amazing App! 🌟🚀")
        gr.Markdown("It comes with state and settings managment")

        chatbot = gr.Chatbot()
        with gr.Column():
            message = gr.Textbox(label="chat input")
            message.submit(
                message_handler,
                [chat, message, chatbot, messages],
                [chat, message, chatbot, messages],
            )
            submit = gr.Button("Submit", variant="primary")
            submit.click(
                message_handler,
                [chat, message, chatbot, messages],
                [chat, message, chatbot, messages],
            )
        with gr.Row():
            with gr.Column():
                clear = gr.Button("Clear")
                clear.click(
                    on_clear_click,
                    [],
                    [message, chatbot, messages],
                    queue=False,
                )
            with gr.Accordion("Settings", open=False):
                model_name = gr.Dropdown(
                    choices=MODELS_NAMES, value=MODELS_NAMES[0], label="model"
                )
                temperature = gr.Slider(
                    minimum=0.0,
                    maximum=1.0,
                    value=0.7,
                    step=0.1,
                    label="temperature",
                    interactive=True,
                )
                apply_settings = gr.Button("Apply")
                apply_settings.click(
                    on_apply_settings_click,
                    [model_name, temperature],
                    [chat, message, chatbot, messages],
                    queue=False,
                )
