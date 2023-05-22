---
title: "GradioGPT"
emoji: "🚀"
colorFrom: "red"
colorTo: "orange"
sdk: "gradio"
sdk_version: "3.32.0"
app_file: app.py
pinned: false
---

# GradioGPT
A perfect get started template for your amazing new shiny GPT application that comes with a gradio demo

**Features**

- [LangChain `ChatOpenAI`](https://python.langchain.com/en/latest/modules/models/chat/integrations/openai.html)
- Streaming
- [State managment](https://gradio.app/state-in-blocks/) so multiple user can use it
- UI with [Gradio](https://gradio.app/)
- types and comments

## Installation

### Virtual Enviroment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
``` 

Then

```bash
gradio app.py
```

### OpenAI key

Place your OpenAI key into `.env`

```
OPENAI_API_KEY=<YOUR_KEY>
```