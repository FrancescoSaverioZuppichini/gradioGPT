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
A perfect starting template for your amazing new shiny GPT application that comes with a gradio demo

[gradioGPT.webm](https://github.com/FrancescoSaverioZuppichini/gradioGPT/assets/15908060/f5a23581-88bf-4129-9d28-a47beeae1bdf)


## 🔥 Features

- [LangChain `ChatOpenAI`](https://python.langchain.com/en/latest/modules/models/chat/integrations/openai.html)
- Streaming
- [State management](https://gradio.app/state-in-blocks/) so multiple users can use it
- UI with [Gradio](https://gradio.app/)
- types and comments

## 💻 Installation

Create a `.env` file with your OpenAI API Key

```bash
echo "OPENAI_API_KEY=<YOUR_API_KEY>" > .env
```

You `.env` should look like

```
OPENAI_API_KEY=<YOUR_KEY>
```

### Virtual Enviroment

You can use python virtual env

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
``` 

Then

```bash
cd src
gradio app.py
```

Using `gradio` is great because it gives you hot reloading

### Docker 

Easy peasy

```bash
docker build -t gradio-app .
docker run --rm -it -p 7860:7860 \
    -e GRADIO_SERVER_NAME=0.0.0.0 \
    -v $(pwd)/.env:/app/.env \
    gradio-app
```

Then, navigate to `http://0.0.0.0:7860/`

You can also change the python version used (defaults to `3.11`) by

```bash
docker build --build-arg PYTHON_VERSION=3.9 -t gradio-app .
```

## 🏆 contribution

Want to contribute? Thanks a lot! Please Fork it and PR it 🙏
