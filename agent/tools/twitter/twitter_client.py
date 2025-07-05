"""
twitter_client.py

Client for interacting with Twitter API: tweeting, replying, quoting, following, and retrieving timeline.
"""

import os
import requests
from typing import Any, Dict, List, Optional

class TwitterClient:
    """
    Wrapper around Twitter API endpoints.
    """

    def __init__(self,
                 bearer_token: Optional[str] = None,
                 api_key: Optional[str] = None,
                 api_key_secret: Optional[str] = None,
                 access_token: Optional[str] = None,
                 access_token_secret: Optional[str] = None):
        """
        Initialize TwitterClient with OAuth2 or OAuth1 credentials.
        Credentials can be loaded from environment if not passed explicitly.
        """
        self.bearer_token = bearer_token or os.getenv("TWITTER_BEARER_TOKEN")
        # TODO: support OAuth1 flows if needed
        self.base_url = "https://api.twitter.com/2"

    def _headers(self) -> Dict[str, str]:
        """
        Construct headers for authorization.
        """
        return {"Authorization": f"Bearer {self.bearer_token}",
                "Content-Type": "application/json"}

    def tweet(self, text: str, **kwargs) -> Dict[str, Any]:
        """
        Post a tweet with given text.
        Additional params (e.g., media_ids) via kwargs.
        """
        url = f"{self.base_url}/tweets"
        payload = {"text": text}
        payload.update(kwargs)
        resp = requests.post(url, json=payload, headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def reply(self, text: str, in_reply_to_tweet_id: str, **kwargs) -> Dict[str, Any]:
        """
        Reply to a tweet.
        """
        url = f"{self.base_url}/tweets"
        payload = {
            "text": text,
            "reply": {"in_reply_to_tweet_id": in_reply_to_tweet_id}
        }
        payload.update(kwargs)
        resp = requests.post(url, json=payload, headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def quote(self, text: str, quote_tweet_id: str, **kwargs) -> Dict[str, Any]:
        """
        Quote a tweet.
        """
        url = f"{self.base_url}/tweets"
        payload = {
            "text": text,
            "reply": {
                "in_reply_to_tweet_id": quote_tweet_id,
                "exclude_reply_user_ids": []
            }
        }
        payload.update(kwargs)
        resp = requests.post(url, json=payload, headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def follow(self, user_id: str) -> Dict[str, Any]:
        """
        Follow a user by user ID.
        """
        url = f"{self.base_url}/users/{user_id}/following"
        resp = requests.post(url, headers=self._headers())
        resp.raise_for_status()
        return resp.json()

    def timeline(self, user_id: str, max_results: int = 20) -> List[Dict[str, Any]]:
        """
        Get recent tweets from a user's timeline.
        """
        url = f"{self.base_url}/users/{user_id}/tweets"
        params = {"max_results": max_results}
        resp = requests.get(url, params=params, headers=self._headers())
        resp.raise_for_status()
        return resp.json().get("data", [])

    def mentions(self, user_id: str, max_results: int = 20) -> List[Dict[str, Any]]:
        """
        Get recent mentions of the authenticated user.
        """
        url = f"{self.base_url}/users/{user_id}/mentions"
        params = {"max_results": max_results}
        resp = requests.get(url, params=params, headers=self._headers())
        resp.raise_for_status()
        return resp.json().get("data", [])
