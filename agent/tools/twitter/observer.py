"""
observer.py

Observes Twitter streams: timelines, mentions, quote-tweets, and DMs.
Uses TwitterClient to fetch and filter new events.
"""

from typing import List, Dict, Any, Optional
from .twitter_client import TwitterClient

class TwitterObserver:
    """
    Fetches and processes incoming Twitter data for the agent.
    """

    def __init__(self, client: TwitterClient, user_id: str):
        """
        :param client: Initialized TwitterClient.
        :param user_id: Authenticated agent user ID.
        """
        self.client = client
        self.user_id = user_id
        self._since_id: Optional[str] = None

    def fetch_mentions(self, max_results: int = 20) -> List[Dict[str, Any]]:
        """
        Fetch recent mentions since last seen.
        """
        mentions = self.client.mentions(self.user_id, max_results=max_results)
        # TODO: filter by since_id and update since_id
        return mentions

    def fetch_timeline(self, max_results: int = 20) -> List[Dict[str, Any]]:
        """
        Fetch timeline tweets from followed accounts.
        """
        timeline = self.client.timeline(self.user_id, max_results=max_results)
        # TODO: filter new tweets since last seen
        return timeline

    def fetch_quote_tweets(self, tweet_id: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch quote tweets of a specific tweet.
        """
        # Note: Twitter API v2 does not provide direct quote query; use search endpoint.
        query = f'url:"https://twitter.com/{self.user_id}/status/{tweet_id}"'
        results = self.client.search(query, num_results=max_results)
        return results

    def fetch_direct_messages(self) -> List[Dict[str, Any]]:
        """
        TODO: implement DM fetching once DM endpoints available.
        """
        return []
