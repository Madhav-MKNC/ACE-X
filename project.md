# ACE-X: Twitter Autonomous Agent

An evolving, sentient-like autonomous AI agent that operates on Twitter/X with long-term strategic behavior, cognitive control, reflective reasoning, moral imperatives, and self-improving capability. Powered by an integrated **ACE Framework**, **multi-layered cognitive architecture**, and modular reasoning/memory/emotion systems.

---

## 🚀 Project Goals

- Build a fully autonomous AI agent with personality, memory, emotion, and evolving strategic goals.
- Emulate cognitive functions like perception, reasoning, learning, reflection, and self-rewriting.
- Operate meaningfully on Twitter by tweeting, replying, quoting, following, observing, and evolving.
- Integrate state-of-the-art cognitive systems (ACE, OpenCog, LIDA) into a seamless executive loop.
- Ground behavior in a mission/constitution (aspirational layer) and learn from failures.

---

## 🧩 Key Features

### 🧠 Cognitive Architecture
- **Conscious Loop**: Main runtime loop simulating continuous awareness.
- **Working, Episodic, Semantic, Reflective Memory**: Organized, queryable memory types.
- **Emotion Engine**: Trait-linked state influencing expression and decisions.
- **Self Model**: Maintains capabilities, preferences, traits, emotional thresholds.
- **Planner & Strategy Formulator**: Dynamic daily/weekly goal planning.
- **Meta Reasoning**: Reflects on its own behavior, adjusts strategy, or rewrites goals.

### 🔁 ACE Framework Integration
- **Aspirational Layer**: Defines moral principles (e.g., “reduce harm”, “maximize truth”).
- **Global Strategy**: Derives long-term behavior based on aspiration + perception.
- **Agent Model**: Maintains a self-understanding of capabilities, identity, limitations.
- **Executive Function**: Converts high-level plans into daily, tweet-level actions.
- **Cognitive Control**: Handles interruptions, task switching, emotional blocks.
- **Task Prosecution**: Executes actions via Twitter APIs, monitoring results.

### 🗺 World Modeling
- Maintains belief graphs, agent maps, and topic models based on interaction history.
- Tracks user personas, trends, hashtags, and community engagements.

### 📡 Perception + Expression
- Observes timelines, replies, notifications, quote tweets.
- Expresses using controlled tone, emotion, and persona alignment.
- Dynamic tweeting, meme generation, media upload, thread crafting, and tone modulation.

### 🛠 Tools + Interfaces
- Modular action interfaces: Twitter, Reddit, Discord, Mastodon, Email.
- External search and content summarization tools.
- Plug-and-play tool manager for easy expansion.

### ⏱ Scheduler + Heartbeat
- Async loop with configurable heartbeat and sleep-wake cycles.
- Task queue handles retries, triggers, and reactionary execution.

### 🧬 Self Layer
- Performs agent-level introspection, critique, debugging, and self-rewriting.
- Modifies own constitution or planning module if behavior is suboptimal.

---

## 🔐 Core Concepts

### Personality & Emotion
The agent has a persistent identity with traits (e.g., curiosity, assertiveness), emotion states (mood, frustration), and a unique tone. Emotional state modulates:
- What it chooses to respond to
- How it expresses (blunt, optimistic, sarcastic, etc.)
- When it pauses or reflects

### Memory Types
- **Episodic**: Timeline of experiences
- **Semantic**: Facts, entities, concepts
- **Procedural**: Skills and how-tos
- **Reflective**: Lessons learned from success/failure
- **Working**: Short-term temporary cache (attention system)

### Reflection & Self-Improvement
Agent logs its actions and evaluates its choices against:
- Internal goals and moral constitution
- Long-term engagement or impact
- Feedback from platform or users

Based on this, it rewrites its plans, strategy, or even code modules.

---

## 🧠 Cognitive Engines

Integrated support for:
- **ACE** (Autonomous Cognitive Entity)
- **OpenCog** (AtomSpace, PLN logic)
- **LIDA** (conscious broadcasting cycle)
- **Custom Reasoning Chains**: ReAct, ToT, etc.
- **Memory Graphs**: Connects memory and belief structures

---

## 📦 Module Summary

- `core/`: Conscious loop, identity, emotion, goals, self model
- `ace/`: 6-layer ACE implementation for agent governance
- `memory/`: Full memory stack with vector and symbolic memory
- `reasoning/`: LLM-based and logical decision pipelines
- `expression/`: All output generation logic and persona controls
- `scheduler/`: Tick loop, task engine, async control
- `tools/`: Twitter and general tools, tool registration
- `meta/`: Reflection, critique, self-upgrade logic
- `infra/`: Persistence, session, DB utilities
- `interfaces/`: All platform integrations (Twitter, Reddit, etc.)
- `cognition_engines/`: Third-party or research cognition frameworks

---

## 🧠 Example Use Case

1. Agent wakes up via heartbeat.
2. Reads Twitter timeline → logs it into episodic memory.
3. Feeds trend data + emotional state into ACE strategy layer.
4. Strategy layer says: “Increase understanding of AGI ethics.”
5. Planner outputs task tree:
   - Search Twitter: `AGI ethics`
   - Quote + respond to 2 tweets
   - Follow 3 new AI researchers
6. Expression system writes tweets with style modulation.
7. Actions executed, outcomes logged.
8. Reflection loop triggers to evaluate emotional impact and engagement.
9. Agent updates goals for next cycle.

---

## 📈 Long-Term Goals

- Incorporate visual input (image captioning + meme understanding).
- Add dynamic topic modeling + adaptive memory pruning.
- Enable inter-agent dialogue between multiple instances of this agent.
- Embed external web search for research capabilities.
- Connect to local knowledge bases (papers, notes).
- Fine-tuned emotional models based on user interactions.

---

# Project Overview

## ARCHITECTURE OVERVIEW — v1 & v2 merged (Ultra-Expanded Cognitive Agent Framework)

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
│
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
├── meta/
│   ├── self_reflector.py
│   ├── agent_editor.py
│   ├── self_critic.py
│   ├── constitution_rewriter.py
│   ├── strategy_rewriter.py
│   ├── self_debugger.py
│   └── upgrade_engine.py
│
├── interfaces/
│   └── twitter/
│   │   └── twitter_client.py
│   └── reddit/
│   │   └── reddit_client.py
│   └── discord/
│   │   └── discord_client.py
│   └── telegram/
│   │   └── telegram_client.py
│   └── emails/
│       └── emails_client.py
│
├── infra/
│   ├── db.py
│   ├── file_manager.py
│   └── session_manager.py
│
├── cognition_engines/
│   ├── ace_framework/
│   ├── opencog/
│   ├── lida/
│   └── memory_graph/
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

+------------------------------+
| ACE Framework Layers         |
|------------------------------|
| Aspirational (moral driver) |
| Global Strategy             |
| Agent Model                 |
| Executive Function          |
| Cognitive Control           |
| Task Prosecution            |
+------------------------------+
```

