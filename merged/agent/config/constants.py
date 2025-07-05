"""
Application Constants for ACE-X Agent
Defines symbolic constants for use throughout the agent codebase.
"""

# Agent identity
AGENT_NAME = "ACE-X"
AGENT_VERSION = "1.0"

# Default emotion states
MOOD_STATES = ["neutral", "curious", "assertive", "frustrated", "optimistic", "reflective"]

# Task/action types
ACTION_TYPES = ["tweet", "reply", "quote", "follow", "observe", "reflect", "self-modify"]

# Memory types
MEMORY_TYPES = ["episodic", "semantic", "procedural", "reflective", "working"]

# ACE Layer names
ACE_LAYERS = [
    "aspirational",
    "global_strategy",
    "agent_model",
    "executive_function",
    "cognitive_control",
    "task_prosecution"
]
