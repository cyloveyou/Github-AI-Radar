# Context & Memory

长上下文并不等于有效上下文。近期项目显示两条路线正在形成：

- **Compaction / Context Engineering**：只把当前任务真正需要的信息送入模型；
- **Durable Memory**：把长期知识、决策和项目状态放到可审计、可版本化的外部存储。

代表项目包括 fast-jev-compaction 与 ai-memory。

对科研项目而言，理想状态不是让模型“记住一切”，而是把实验结论、数据口径、踩坑、参数决策和待办变成项目内可读、可 diff 的资产。

## 2026-10-07 — Memory becomes portable; learned skills need lifecycle governance

`AgentMemoryRepo/agentmemoryrepo` 将跨会话记忆提出为独立 Git/Markdown 规范，强调跨客户端可读、可合并及多 Agent 冲突可见；`tigerless-labs/autoharness` 则把从真实会话产生的 Skill 纳入证据账本、合并去重、修订与归档生命周期。前者强调**可移植的记忆介质**，后者强调**生成经验的质量治理**。

这不是「模型记得更多」的简单升级，而是从 `Memory storage` 走向 `Memory / Skill governance`：写入来源、冲突、检索、复用和退役都需要可追溯。两项目尚无充分独立长期效果验证，应继续关注跨 Harness 互操作和误归档风险。

## 2026-10-09 — Separate remembered evidence from instructions

`vectorize-io/hindsight` v0.10.3（2026-10-08 发布）在 Coding Agent 记忆中将「过去发生的事实记录」与「团队制定的行动指导」分离，并改进多 Harness 接入、后台记忆深化任务的锁和 429 处理。这是 10-07 可移植 Memory 之外的语义治理问题：**memory ≠ policy/instructions**，不能让旧事实自动变成长期命令。

需要验证事实/指导冲突如何被发现、团队规则如何审批和撤回，以及跨 Codex、Hermes、TRAE 的兼容边界。Source: https://github.com/vectorize-io/hindsight/releases/tag/v0.10.3

## 2026-10-13 — Context as a routed data plane

`mksglu/context-mode` keeps raw tool output outside the model window and uses sandboxed code processing plus SQLite FTS5/BM25 event retrieval to supply only relevant summaries/state. It claims 17 client integrations with MCP and hooks. Unlike Hindsight memory semantics, this focuses on **which bytes enter model context at all**. The project’s 98% saving is a self-reported example, not independent evidence. Source: https://github.com/mksglu/context-mode
