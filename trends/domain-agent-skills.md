# Domain Agent Skills and Local Tools

## 2026-10-16 — Scientific procedures and local multimodal execution

Scientific Agent Skills uses the open Agent Skills specification to package research software, scientific databases, and domain workflows for multiple Coding Agent hosts. The project describes 177 skills and more than 100 databases. These are project-reported counts; repository tests and stars are not substitutes for independent scientific correctness assessment.

VoiceStudio's local voice-processing API and MCP integration illustrate another path: multimodal desktop software becomes an Agent-callable local tool, with deployment, permission, and consent boundaries.

**Pattern:** Domain software and local models → standardized Skill/MCP interface → cross-harness orchestration → verifiable domain artifact.

Sources: https://github.com/K-Dense-AI/scientific-agent-skills ; https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6

## 2026-10-18 — Platform-official Skills target model weaknesses

Google/Android official Android Skills v1.0.15 adds LiteRT on-device inference, Jetpack Compose performance and parked-car app workflows, alongside Android Profiler/Perfetto references. Its README says the program prioritizes tasks where evaluations show LLM underperformance. This refines the domain-Skill thesis: official, versioned procedures should target specific failure modes and testable artifacts rather than generic prompts. Actual benchmark gains are not independently verified here.

Sources: https://github.com/android/skills ; https://github.com/android/skills/commit/ac598b69

## 2026-10-24 — Scientific Harness with formal proof checking; agents inside training loops

Open Math Harness v0.41.0 adds a research-specific Rust capability microkernel, parallel mathematical exploration (Ultramath), and Lean/Mathlib checking of submitted proof candidates. Unlike a general-purpose scientific Skill pack, verification is a tool-mediated runtime decision, not an LLM assertion. However, its full interactive proof-search runtime still depends on Open Math OS infrastructure; only a small Linux/bubblewrap example is self-contained.

OPAL introduces a reactive PyTorch optimizer wrapper: a Coding Agent can revise optimizer and analysis programs during training. This is **closed-loop agent-controlled scientific computation**, not a new fixed optimizer. The generated program executes in the training process (not sandboxed), and author-reported gains require matched-budget independent reproduction.

Sources: https://github.com/openmathmodel/open-math-harness/releases/tag/v0.41.0 ; https://github.com/xingjian-bai/opal ; https://github.com/xingjian-bai/opal/releases/tag/v0.3.7
