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

## 2026-10-14 — Subagent memory recovery after compaction

claude-mem v13.39.0 修复 Codex 子 Agent 压缩后记忆时间线消失：按 `session_id + agent_id` 记录 PostCompact，在下一次 PostToolUse 中注入一次时间线，根线程的 SessionStart 清理标记。关键技术方向是 **线程级生命周期事件 → 上下文压缩边界 → 可恢复记忆状态**，区别于 Context Mode 的工具输出路由和 Hindsight 的记忆语义治理。并发、崩溃和 exactly-once 仍需独立验证。

Source: https://github.com/thedotmack/claude-mem/releases/tag/v13.39.0

## 2026-10-16 — Signed retrieval corpora as an Agent data-plane boundary

XERJ 发布带签名的 Agent 会话轨迹语料包，包含失败步骤、构建元数据和 30 天过期拒绝策略。与 Context Mode 的上下文路由不同，这里强调检索前的语料来源与时效：**provenance → signature/freshness → indexing → retrieval**。签名不保证内容真实，仍需污染与偏差检测。

Source: https://github.com/xerj-org/xerj/releases/tag/pack-agent-session-trajectories-2026-10-15

## 2026-10-17 — Vectorless RAG: layout-first trees and portable Agent retrieval tools

PageIndex v0.4.1 通过 PDF 布局/书签构造结构树，再用 LLM 摘要与可选扩展，减少纯 LLM 结构生成开销；本地/云端 SDK 共享 Agent Tools 形态，覆盖 OpenAI/Anthropic/MCP。与 XERJ 的语料签名、Context Mode 的上下文路由互补：**document structure → index build → retrieval tool contract → agent use**。成本更低属于官方主张，必须以同语料召回率、问答正确率和模型调用费用对照验证。

Source: https://github.com/VectifyAI/PageIndex/releases/tag/v0.4.1

## 2026-10-18 — Compaction requires incremental ingest and concurrency-safe recovery

billion-context v0.1.198/199 introduces per-session ingest watermarks, delta-turn upload, fsync+rename state persistence, stale-reference checks, and dsh attach/takeover race fixes. Unlike Context Mode (tool-output routing) or claude-mem (thread memory restoration), this is long-lived context as a stateful data plane: delta ingestion, reference lifetime, transport, recovery idempotence and repair tooling. Claimed 5x token saving is project-reported; a fast release path skips portions of CI, so independent regression testing matters.

Sources: https://github.com/ranxianglei/billion-context/releases/tag/v0.1.198 ; https://github.com/ranxianglei/billion-context/releases/tag/v0.1.199

## 2026-10-19 — Code graph fidelity and decision-aware team memory

Graphify v0.9.92 修复多语言 AST 调用解析、节点 ID 冲突，以及 graph.json/MCP 往返时平行边丢失问题。与 PageIndex 的文档布局索引不同，其检索路径是 **deterministic AST → explainable code graph → MCP query**；重点应测试边保真率、同名解析与缓存 Schema 升级重建。

TencentDB Agent Memory v2.0.3-beta.1 将 Skill 选择和 Memory L3 更新判定纳入可插拔决策服务，支持按需加载 Skill 和保存会话轨迹。新能力默认关闭，决策服务失败可回退。这补足了此前 Hindsight 的事实/指导分离和 Context Mode 的输出路由：**memory asset → selection/update policy → observable agent reuse**。需要评估错误 Skill 选择、记忆遗漏与决策服务故障。

Sources: https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.92 ; https://github.com/TencentCloud/TencentDB-Agent-Memory/releases/tag/v2.0.3-beta.1


## 2026-10-20 — Reversible compression at the model request boundary

Headroom v0.41.0 brings context compression to an agent-facing proxy, MCP, local cache and per-agent cost attribution. The later HTTP/WebSocket Responses hook integrates Codex-like streaming request paths. Compared with Context Mode's output sandbox and retrieval, the differentiator is a reversible compression gateway with observability. Vendor-reported token savings and answer preservation require independent task-level testing.

Sources: https://github.com/headroomlabs-ai/headroom/releases/tag/v0.41.0 ; https://github.com/headroomlabs-ai/headroom/commit/fbf7bc3278c1

## 2026-10-22 — Smart recall and multimodal evidence memory

claude-mem v15.0.0 changes the default retrieval contract to **compact index search → contextual timeline → selected observation detail**, replacing the old guided/auto search interface. v15.0.1 fixes project-alias scope consistency across all three steps. This is a meaningful memory retrieval protocol change, not a repeat of v13.39's post-compaction subagent restoration.

OpenVLHarness makes boxes, masks, depth maps, images and web references addressable across visual-tool steps, while a separate Python coding context performs numerical operations over retained evidence. Unlike text-only context compression, this is **structured multimodal working memory with reusable intermediate measurements**. Claimed benchmark gains are author-reported.

Sources: https://github.com/thedotmack/claude-mem/releases/tag/v15.0.0 ; https://github.com/thedotmack/claude-mem/releases/tag/v15.0.1 ; https://github.com/uclanlp/OpenVLHarness
