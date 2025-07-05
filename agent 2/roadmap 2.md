# 🧠 ACE Framework Deep Integration - Applied to Twitter Autonomous Agent

Based on [ACE GitHub](https://github.com/daveshap/ACE_Framework) and the official PDF.

---

## ✅ ACE Layer Breakdown (Mapped to Agent Design)

| **Layer**               | **Function in Agent**                                                                 |
|------------------------|----------------------------------------------------------------------------------------|
| **1. Aspirational**     | Moral compass: defines purpose via heuristic imperatives, e.g., “Reduce suffering…”   |
| **2. Global Strategy**  | Strategic brain: formulates agent’s long-term plan based on mission and world state   |
| **3. Agent Model**      | Self-awareness: understands own capabilities, configs, telemetry, personality         |
| **4. Executive Function**| Project manager: turns plans into project roadmaps, allocates resources               |
| **5. Cognitive Control**| Task selector: manages task switching, frustration modeling, decision arbitration     |
| **6. Task Prosecution** | API/action executor: performs tweets, follows, replies, etc. Monitors success/failure |

Each layer has **privilege separation** and bi-directional flow:
- Higher layers supervise/correct lower layers.
- Lower layers report real state, success/failure upward.

---

## 🔁 ACE Execution Flow in Twitter Agent

1. **Aspirational Layer** - agent’s constitution:
   - Mission: “Facilitate useful discourse and reduce toxicity.”
   - Heuristic imperatives: “Increase understanding”, “Avoid harm”, etc.

1. **Global Strategy** - defines behavior:
   - “Engage with trending threads on AI ethics.”
   - “Grow AI dev follower base.”

1. **Agent Model** - introspective state:
   - Knows its capabilities: tweet, reply, etc.
   - Knows rate limits, prior metrics, style.

1. **Executive Function** - roadmap & tasks:
   - “Tweet 3 thoughts on AGI risks.”
   - “Follow 5 new AI researchers.”

1. **Cognitive Control** - action arbitration:
   - “Switch to quote instead of reply.”
   - “Pause tasks if emotion state is frustrated.”

1. **Task Prosecution** - direct Twitter calls:
   - Uses `twitter.account` to tweet, reply, DM.
   - Monitors outcomes and logs them.

---

## 🧱 Implementation Plan: ACE for Autonomous Twitter Agent

### Phase 1: Boot Architecture

- [x] `agent/ace/aspirational.py` - loads moral constitution (plain text)
- [x] `agent/ace/global_strategy.py` - generates strategic plan from aspiration + trends
- [x] `agent/ace/agent_model.py` - self-state: capabilities, rate limits, prior performance
- [x] `agent/ace/executive_function.py` - task planner (e.g. make 5 tweets, 3 replies today)
- [x] `agent/ace/cognitive_control.py` - frustration-based task switching
- [x] `agent/ace/task_prosecution.py` - interfaces with `twitter.account`

### Phase 2: Supporting Systems

- `agent/memory/` - episodic, procedural, and reflective memories
- `agent/emotion/` - frustration index, mood state
- `agent/tools/twitter_client.py` - abstract Twitter actions
- `agent/planner/goal_rewriter.py` - adjusts goals weekly
- `agent/reflection/reflector.py` - critiques actions
- `agent/core/runtime.py` - main loop that runs layers top-down and bottom-up

### Phase 3: Self-Improving Capabilities

- `meta/self_debugger.py` - detects errors, adapts strategy
- `meta/constitution_rewriter.py` - evolves aspirations
- `meta/strategy_rewriter.py` - changes long-term strategy if failing

---

## Folder Structure

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
├── core/                               # Conscious agent core & identity
│   ├── identity.py                     # Name, traits, role, tone
│   ├── emotion_engine.py               # Affective state system
│   ├── consciousness.py                # Core personality evolution
│   ├── mind_loop.py                    # Central cycle driver (tick loop)
│   ├── reflection_loop.py              # Meta-reasoning & growth
│   └── telemetry.py                    # Self-observation, metrics
│
├── memory/                             # Unified multi-type memory system
│   ├── episodic_memory.py              # Timeline of events
│   ├── semantic_memory.py              # Facts, concepts, entities
│   ├── procedural_memory.py            # Learned skills, best practices
│   ├── reflective_memory.py            # Lessons learned from reflection
│   ├── working_memory.py               # Short-term scratch space (attention)
│   ├── memory_indexer.py               # Cross-referencing + vector search
│   └── store/
│       ├── faiss_index/
│       ├── memory_logs/
│       └── embeddings/
│
├── emotion/
│   ├── affective_state.py              # Current emotional vector
│   ├── mood_modulation.py              # Modulates output based on emotion
│   ├── frustration_model.py            # Influences task switching
│   └── emotion_traits.py               # Personality traits
│
├── tools/                              # Tool abstraction layer
│   ├── twitter/
│   │   ├── twitter_client.py           # All low-level Twitter actions
│   │   ├── observer.py                 # Reads timelines, replies, stats
│   │   └── media_tools.py              # Meme/gen image support
│   ├── web_search.py                   # Optional: scraping/search fallback
│   └── tool_manager.py                 # Tool registration & dispatch
│
├── reasoning/                          # LLM-based reasoning, prompt mgmt
│   ├── llm_interface.py                # Unified wrapper for OpenAI, Anthropic, etc.
│   ├── system_prompt.py                # Agent persona/system prompt
│   ├── reasoning_chain.py              # CoT / ToT / agentic thought chains
│   ├── evaluator.py                    # Result scoring
│   ├── strategy_formulator.py          # Long-term strategy generator
│   └── replanner.py                    # Daily/weekly re-goaling
│
├── scheduler/                          # Clock + tasks + daily cycles
│   ├── heartbeat.py                    # Main event loop, beat frequency
│   ├── task_queue.py                   # Priority/task stack
│   ├── sleep_wake.py                   # Resting states, time cycles
│   └── triggers.py                     # Event-based activations
│
├── meta/                               # Self-reflection & self-modification
│   ├── self_reflector.py               # Reflects on decisions & behavior
│   ├── self_critic.py                  # Critiques decisions, flags mistakes
│   ├── constitution_rewriter.py        # Edits agent constitution if permitted
│   ├── strategy_rewriter.py            # Rewrites planning strategies
│   ├── self_debugger.py                # Logs, detects failures, attempts fixes
│   └── upgrade_engine.py               # Self-rewriting and versioning engine
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

---

