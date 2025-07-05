# Directory Structure

```
agent/
├── main.py
├── run_agent.py
├── README.md
├── requirements.txt
│
├── config/
│   ├── settings.py
│   ├── constants.py
│   └── secrets.env
│
├── ace/                                # ACE framework implementation
│   ├── aspirational.py                 # Moral constitution, heuristic imperatives
│   ├── global_strategy.py              # Long-term planning from aspirations
│   ├── agent_model.py                  # Self-awareness, capabilities, rate limits
│   ├── executive_function.py           # Converts plans into structured tasks
│   ├── cognitive_control.py            # Task switching, frustration management
│   ├── task_prosecution.py             # Actual low-level execution (tweets, follows)
│   └── interfaces.py                   # Inter-layer data contracts
│
├── core/                               # Agent runtime, cognition, world model
│   ├── agent_core.py
│   ├── consciousness_loop.py
│   ├── self_model.py
│   ├── identity.py
│   ├── agency.py
│   ├── value_system.py
│   ├── emotion_engine.py
│   ├── goal_memory.py
│   ├── situational_context.py
│   ├── experience_synthesizer.py
│   ├── meta_governor.py
│   │
│   └── world/
│       ├── agent_map.py
│       ├── belief_model.py
│       └── topic_graph.py
│
├── memory/
│   ├── episodic_memory.py
│   ├── semantic_memory.py
│   ├── procedural_memory.py
│   ├── reflective_memory.py
│   ├── working_memory.py
│   ├── memory_indexer.py
│   └── store/
│       ├── faiss_index/
│       ├── memory_logs/
│       └── embeddings/
│
├── emotion/
│   ├── affective_state.py
│   ├── mood_modulation.py
│   ├── frustration_model.py
│   └── emotion_traits.py
│
├── tools/
│   ├── twitter/
│   │   ├── twitter_client.py
│   │   ├── observer.py
│   │   └── media_tools.py
│   ├── web_search.py
│   └── tool_manager.py
│
├── reasoning/
│   ├── llm_interface.py
│   ├── system_prompt.py
│   ├── reasoning_chain.py
│   ├── evaluator.py
│   ├── strategy_formulator.py
│   └── replanner.py
│
├── scheduler/
│   ├── heartbeat.py
│   ├── task_queue.py
│   ├── sleep_wake.py
│   └── triggers.py
│
├── meta/
│   ├── self_reflector.py
│   ├── self_critic.py
│   ├── constitution_rewriter.py
│   ├── strategy_rewriter.py
│   ├── self_debugger.py
│   └── upgrade_engine.py
│
├── interfaces/
│   ├── twitter_client.py
│   ├── reddit_client.py
│   ├── mastodon_client.py
│   ├── discord_client.py
│   └── email_handler.py
│
├── infra/
│   ├── db.py
│   ├── file_manager.py
│   └── session_manager.py
│
├── data/
│   ├── logs/
│   │   ├── execution.log
│   │   ├── reasoning.log
│   │   └── actions.jsonl
│   ├── snapshots/
│   │   └── mindstate_YYYYMMDD.json
│   └── config/
│       ├── agent_traits.json
│       └── constitution.txt
│
└── tests/
    ├── test_core.py
    ├── test_memory.py
    ├── test_ace_layers.py
    └── test_tools.py
```

