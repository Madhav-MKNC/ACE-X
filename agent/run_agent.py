"""
run_agent.py

Entrypoint to assemble and launch the ACE-X autonomous Twitter agent.
Initializes components, registers tools, and starts the main runtime loop.
"""

import asyncio
from config.settings import Settings
from infra.db import Database
from infra.session_manager import SessionManager
from tools.tool_manager import ToolManager
from tools.web_search import WebSearch
from tools.twitter.twitter_client import TwitterClient
from ace.task_prosecution import TaskProsecution
from reasoning.llm_interface import LLMInterface
from reasoning.evaluator import Evaluator
from reasoning.reasoning_chain import ReasoningChain
from core.identity import Identity
from core.self_model import SelfModel
from core.consciousness_loop import ConsciousnessLoop

def main():
    # Load settings and initialize storage
    settings = Settings()
    db = Database(settings.DATABASE_FILE)
    session_mgr = SessionManager(settings.SESSION_FILE)

    # Initialize tool manager and register tools
    tools = ToolManager()
    twitter = TwitterClient(settings.TWITTER_BEARER_TOKEN)
    web = WebSearch(api_key=settings.OPENAI_API_KEY)
    tools.register("tweet", twitter.tweet)
    tools.register("reply", twitter.reply)
    tools.register("quote", twitter.quote)
    tools.register("follow", twitter.follow)
    tools.register("search_web", web.search)
    tools.register("summarize", web.summarize)

    # Initialize ACE framework adapter and task prosecutor
    prosecutor = TaskProsecution(tools)
    tools.register("execute_action", prosecutor.execute_action)

    # Initialize reasoning components
    llm = LLMInterface(api_key=settings.OPENAI_API_KEY)
    evaluator = Evaluator(llm)
    reasoning_chain = ReasoningChain(llm, evaluator)

    # Initialize core agent
    identity = Identity()
    self_model = SelfModel(identity)
    consciousness = ConsciousnessLoop(identity, self_model)

    # Start heartbeat and scheduler if needed (demo: run consciousness)
    consciousness.run_forever()

if __name__ == "__main__":
    main()
