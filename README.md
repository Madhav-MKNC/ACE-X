## ⚙️ ARCHITECTURE OVERVIEW — v2 (Ultra-Expanded Cognitive Agent Framework)

> Inspired by:
> - **ACE** (Dave Shapiro)
> - **OpenCog** (cognitive synergy, PLN, atomspace, etc.)
> - **LIDA**, **SOAR**, **CLARION**, **MCTS**, **GRAIL**, **CogPrime**
> - **System 1/System 2**, hierarchical reflective loops
> - **Self-rewriting**, **self-debugging**, **emotional modulation**
> - **Tool use**, **web integration**, **multi-agent abstraction**

---

### 🧠 Top-Level Cognitive Architecture

```
                   +--------------------+
                   |  Conscious Loop    |
                   |--------------------|
                   | Global agent state |
                   | Identity + traits  |
                   | Emotion influence  |
                   +--------+-----------+
                            |
         +------------------+-------------------+
         |                                      |
+--------v--------+                    +--------v--------+
| Perception Loop |                    | Reflection Loop |
|-----------------|                    |-----------------|
| Twitter input   |                    | Meta-reasoning  |
| Embeddings      |                    | Self-eval/meta  |
| Episodic logging|                    | Self-improvement|
+-----------------+                    +-----------------+

+---------------------------------------------------------+
|                   Executive Control                     |
|---------------------------------------------------------|
| Goal selection | Action planning | Decision arbitration |
+---------------------------------------------------------+

+----------------------+     +----------------------------+
| Memory Subsystems    |     | Expression Subsystems      |
|----------------------|     |----------------------------|
| Episodic             |     | Language generation        |
| Semantic             |     | Expression strategies      |
| Procedural           |     | Emotion-modulated tone     |
| Reflective           |     | Reply/meme/thread writers  |
+----------------------+     +----------------------------+

+-------------------------+ +-----------------------------+
| Tool Layer (Twitter, etc)| | Scheduler & Task Engine     |
|-------------------------| |-----------------------------|
| Twitter API             | | Cron-like heartbeat         |
| External tools          | | Dynamic task queue          |
+-------------------------+ +-----------------------------+
```

## 🧱 Expanded Module Stack (30+ Real Modules)

### `core/` — Heart of the agent
- `agent_core.py` — Master runtime loop (consciousness tick)
- `identity.py` — Persistent agent name, age, traits, tone
- `emotion_engine.py` — Trait-linked emotional state, affect modulation
- `consciousness.py` — Dynamic long-running personality + behavior shaping

### `perception/` — Input and world modeling
- `observer.py` — Twitter content observer
- `embedder.py` — LLM-based and local vector embeddings
- `sentiment_analyzer.py` — Emotional tone of content
- `event_modeler.py` — Distills events from input (ACE style)
- `input_bus.py` — Pipes everything into memory modules

### `memory/` — Multi-type memory architecture
- `episodic_memory.py` — Timeline of observed experiences
- `semantic_memory.py` — Declarative factual knowledge
- `procedural_memory.py` — How-to/skills/strategies
- `reflective_memory.py` — Insights about itself
- `working_memory.py` — Temporary state slots (LIDA-like)
- `memory_indexer.py` — Cross-links between memory types

### `reasoning/` — Cognitive processing
- `llm_interface.py` — Core LLM wrapper, API handler
- `reasoning_chain.py` — Multi-layered reasoning (ToT, CoT, ACE-style)
- `pln_engine.py` — Probabilistic logic networks (OpenCog style)
- `planner.py` — Temporal + goal-based planning
- `goal_selector.py` — Intention management
- `task_selector.py` — Behavior arbitrator
- `meta_reasoner.py` — Reflective evaluation of past actions

### `expression/` — Output subsystem
- `expression_strategy.py` — Style, tone, rhetorical methods
- `tweet_generator.py` — Generates tweet, replies, threads
- `meme_engine.py` — Optional meme generation (DALL·E etc.)
- `emotion_modulator.py` — Controls how emotion affects expression
- `persona_controller.py` — Controls how the agent sounds online

### `tools/` — Interfaces
- `twitter_client.py` — Post, reply, retweet, follow
- `web_lookup.py` — External info fetch (scraper/browse)
- `toolchain.py` — Registerable external tools

### `scheduler/`
- `heartbeat.py` — Main loop scheduler
- `time_events.py` — Time-triggered actions (e.g., daily tweet)
- `task_queue.py` — Asynchronous, prioritized task runner

### `meta/` — Self-aware layer
- `self_reflector.py` — Internal state analysis, critique
- `upgrade_engine.py` — Rewrite/edit own modules (bootstrapped)
- `self_debugger.py` — Detect and log inconsistencies or bugs
- `agent_editor.py` — Refines self goals, expands traits

### `frameworks/` — Third-party integrated cognition systems
- `ace_engine.py` — ACE-inspired executive engine
- `opencog_adapter.py` — Embeds PLN/AtomSpace-style logic
- `lida_cycle.py` — Implementations of LIDA attention/planning cycle
- `memory_graph.py` — Graph-like memory linkage layer

---
## Folder Structure

```
agent/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── core/
│   ├── agent_core.py
│   ├── consciousness_loop.py
│   ├── identity.py
│   ├── self_model.py
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
├── perception/
│   ├── observer.py
│   ├── embedder.py
│   ├── sentiment_analyzer.py
│   ├── event_modeler.py
│   └── input_bus.py
│
├── memory/
│   ├── episodic_memory.py
│   ├── semantic_memory.py
│   ├── procedural_memory.py
│   ├── reflective_memory.py
│   ├── working_memory.py
│   └── memory_indexer.py
│
├── reasoning/
│   ├── llm_interface.py
│   ├── reasoning_chain.py
│   ├── pln_engine.py
│   ├── planner.py
│   ├── goal_selector.py
│   ├── task_selector.py
│   └── meta_reasoner.py
│
├── expression/
│   ├── expression_strategy.py
│   ├── tweet_generator.py
│   ├── meme_engine.py
│   ├── emotion_modulator.py
│   └── persona_controller.py
│
├── interaction/
│   └── dialogue_manager.py
│
├── self/
│   ├── self_reflector.py
│   ├── upgrade_engine.py
│   ├── self_debugger.py
│   └── agent_editor.py
│
├── tools/
│   ├── web_lookup.py
│   └── toolchain.py
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
├── scheduler/
│   ├── heartbeat.py
│   ├── time_events.py
│   └── task_queue.py
│
├── cognition_engines/
│   ├── ace_framework/
│   ├── opencog/
│   ├── lida/
│   └── memory_graph/
│
└── data/
    ├── logs/
    ├── memory_store/
    └── state_snapshots/

```
---

## 🛠 Dev Stack

| Component         | Tool/Tech          |
|------------------|--------------------|
| LLM               | OpenAI (abstracted) |
| Scheduler         | Python `asyncio`   |
| Vector DB         | Chroma / FAISS     |
| Storage           | SQLite / local FS  |
| Logging           | rich / loguru      |
| Prompt mgmt       | langchain or raw   |
| Agent orchestration | custom or crewAI like shell |
| Memory model      | custom + inspiration from ReAct, MemGPT |

