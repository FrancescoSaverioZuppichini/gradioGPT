# adapted from https://github.com/hwchase17/langchain/issues/2428#issuecomment-1512280045
from queue import Queue
from typing import Any

from langchain.callbacks.base import BaseCallbackHandler


class QueueCallback(BaseCallbackHandler):
    """Callback handler for streaming LLM responses to a queue."""

    def __init__(self, queue: Queue):
        self.queue = queue

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.queue.put(token)

    def on_llm_end(self, *args, **kwargs: Any) -> None:
        return self.queue.empty()
