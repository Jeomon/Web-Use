"""ChatCheaperInference: defaults and environment overrides."""

from unittest.mock import patch

from src.providers import ChatCheaperInference
from src.providers.cheaper_inference.llm import CHEAPER_INFERENCE_BASE_URL


@patch("src.providers.openai.llm.AsyncOpenAI")
@patch("src.providers.openai.llm.OpenAI")
def test_defaults(mock_openai, mock_async_openai, monkeypatch):
    monkeypatch.setenv("CHEAPER_INFERENCE_API_KEY", "test-key")
    monkeypatch.delenv("CHEAPER_INFERENCE_API_BASE", raising=False)

    llm = ChatCheaperInference()

    assert llm.provider == "cheaper_inference"
    assert llm.model_name == "gpt-5.4-mini"
    assert llm.base_url == CHEAPER_INFERENCE_BASE_URL
    for mock_client in (mock_openai, mock_async_openai):
        mock_client.assert_called_once_with(
            api_key="test-key",
            base_url=CHEAPER_INFERENCE_BASE_URL,
            timeout=600.0,
            max_retries=2,
        )


@patch("src.providers.openai.llm.AsyncOpenAI")
@patch("src.providers.openai.llm.OpenAI")
def test_base_url_from_environment(mock_openai, mock_async_openai, monkeypatch):
    monkeypatch.setenv("CHEAPER_INFERENCE_API_KEY", "test-key")
    monkeypatch.setenv("CHEAPER_INFERENCE_API_BASE", "https://example.test/v1")

    llm = ChatCheaperInference(model="claude-sonnet-5")

    assert llm.model_name == "claude-sonnet-5"
    assert llm.base_url == "https://example.test/v1"
