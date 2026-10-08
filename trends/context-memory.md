# Context & Memory

长上下文并不等于有效上下文。近期项目显示两条路线正在形成：

- **Compaction / Context Engineering**：只把当前任务真正需要的信息送入模型；
- **Durable Memory**：把长期知识、决策和项目状态放到可审计、可版本化的外部存储。

代表项目包括 fast-jev-compaction 与 ai-memory。

对科研项目而言，理想状态不是让模型“记住一切”，而是把实验结论、数据口径、踩坑、参数决策和待办变成项目内可读、可 diff 的资产。

## 2026-10-07 — Memory becomes portable; learned skills need lifecycle governance

`AgentMemoryRepo/agentmemoryrepo` 将跨会话记忆提出为独立 Git/Markdown 规范，强调跨客户端可读、可合并及多 Agent 冲突可见；`tigerless-labs/autoharness` 则把从真实会话产生的 Skill 纳入证据账本、合并去重、修订与归档生命周期。前者强调**可移植的记忆介质**，后者强调**生成经验的质量治理**。

这不是「模型记得更多」的简单升级，而是从 `Memory storage` 走向 `Memory / Skill governance`：写入来源、冲突、检索、复用和退役都需要可追溯。两项目尚无充分独立长期效果验证，应继续关注跨 Harness 互操作和误归档风险。
