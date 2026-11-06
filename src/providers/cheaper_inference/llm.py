"""Cheaper Inference LLM provider via OpenAI-compatible API."""

import os
from typing import Optional

from src.providers.openai.llm import ChatOpenAI

CHEAPER_INFERENCE_BASE_URL = "https://api.cheaperinference.com/v1"


class ChatCheaperInference(ChatOpenAI):
    """
    Cheaper Inference LLM implementation using the OpenAI client.

    Uses Cheaper Inference's OpenAI-compatible API.
    Set CHEAPER_INFERENCE_API_KEY in the environment.
    """

    def __init__(
        self,
        model: str = "gpt-5.4-mini",
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 600.0,
        max_retries: int = 2,
        temperature: Optional[float] = None,
        **kwargs,
    ):
        api_key = api_key or os.environ.get("CHEAPER_INFERENCE_API_KEY")
        base_url = (
            base_url or os.environ.get("CHEAPER_INFERENCE_API_BASE") or CHEAPER_INFERENCE_BASE_URL
        )
        super().__init__(
            model=model,
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            temperature=temperature,
            **kwargs,
        )

    @property
    def provider(self) -> str:
        return "cheaper_inference"
