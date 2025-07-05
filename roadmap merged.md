# ARCHITECTURE OVERVIEW — v1 & v2 merged (Ultra-Expanded Cognitive Agent Framework)

> Inspired by:
> - **ACE** (Dave Shapiro)
> - **OpenCog** (cognitive synergy, PLN, atomspace, etc.)
> - **LIDA**, **SOAR**, **CLARION**, **MCTS**, **GRAIL**, **CogPrime**
> - **System 1/System 2**, hierarchical reflective loops
> - **Self-rewriting**, **self-debugging**, **emotional modulation**
> - **Tool use**, **web integration**, **multi-agent abstraction**

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

2. **Global Strategy** - defines behavior:
   - “Engage with trending threads on AI ethics.”
   - “Grow AI dev follower base.”

3. **Agent Model** - introspective state:
   - Knows its capabilities: tweet, reply, etc.
   - Knows rate limits, prior metrics, style.

4. **Executive Function** - roadmap & tasks:
   - “Tweet 3 thoughts on AGI risks.”
   - “Follow 5 new AI researchers.”

5. **Cognitive Control** - action arbitration:
   - “Switch to quote instead of reply.”
   - “Pause tasks if emotion state is frustrated.”

6. **Task Prosecution** - direct Twitter calls:
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

## 🧠 Cognitive Architecture Layering Summary (Unified)

### Top-Level Systems
- Consciousness Loop → drives ticks
- Agent Self Model → centralized identity & capabilities
- Emotion Engine → modulates behavior
- Mind/Memory → stores experience
- Strategy + Planning → determines long-horizon behavior
- Expression System → composes content
- Tools → bridges to external world (Twitter, Reddit, etc.)
- Meta Layer → evolution, self-critique, repair
- World Model → tracks external entities and trends

---

## ✅ Final Unified Directory Tree

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
├── ace/
│   ├── aspirational.py
│   ├── global_strategy.py
│   ├── agent_model.py
│   ├── executive_function.py
│   ├── cognitive_control.py
│   ├── task_prosecution.py
│   └── interfaces.py
│
├── core/
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

