"""
llm_interface.py

Abstracts interaction with an LLM provider. Handles prompt construction, API calls, and response parsing.
"""

import os
import openai
from typing import Optional, Dict, Any

class LLMInterface:
    """
    Interface for sending prompts to an LLM and receiving generated text.
    """

    def __init__(self,
                 api_key: Optional[str] = None,
                 model: str = "gpt-4",
                 temperature: float = 0.7,
                 max_tokens: int = 512):
        """
        :param api_key: OpenAI API key. Falls back to OPENAI_API_KEY env var.
        :param model: Model identifier.
        :param temperature: Sampling temperature.
        :param max_tokens: Maximum tokens for completion.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self,
                 prompt: str,
                 stop: Optional[list] = None,
                 **kwargs) -> str:
        """
        Send a completion request to the LLM with the given prompt.
        :param prompt: The text prompt to send.
        :param stop: Optional list of stop sequences.
        :return: Generated text response.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop=stop,
            **kwargs
        )
        # Extract generated content
        try:
            return response.choices[0].message.content.strip()
        except (IndexError, AttributeError):
            return ""

    def stream(self,
               prompt: str,
               callback: Optional[Any] = None,
               **kwargs) -> None:
        """
        Stream responses from the LLM for real-time applications.
        :param prompt: The text prompt to send.
        :param callback: Function to call with each chunk.
        """
        for chunk in openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,
            **kwargs
        ):
            content = chunk.choices[0].delta.get("content", "")
            if callback:
                callback(content)
