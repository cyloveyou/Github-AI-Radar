# Agent Auditing and Delegated Authority

## 2026-10-15 — 独立行为审计与人类授权委派

iFixAi 将 Agent 的工具授权、任务遵循、数据隔离、失败报告纳入行为探针，支持独立供应商评判模型、CLI/CI 和跨 Coding Agent Skill。v4.1.0 修复布尔解析、缺失裁决、截断输出与预算相关的评分偏高问题。其评分属于项目自身评测结果，并非第三方认证；默认套件可能涉及大量模型调用。

Paperclip v2026.1012.0 增加实验性 Assistant Connection (MCP)：外部 Coding Agent 通过用户 OAuth/设备码授权代用户处理任务，并支持只读和组织范围限制。同时，未知工具授权选择器和不匹配 scope.allow 的 grant 改为拒绝执行。

**新路线：** Runtime / Sandbox enforcement → User-delegated MCP authority → Independent behavior audit → Evidence-backed acceptance。

它与 Strands Box 的跨工具历史感知策略、tester-army/e2e 的动作重放互补，重点在于不仅限制 Agent，还应验证其是否遵守授权与目标。

待测：越权探针漏报、评判模型一致性、授权撤销时效、跨组织权限边界、恢复后重复执行和审计链完整性。

Sources:
- https://github.com/ifixai-ai/iFixAi/releases/tag/v4.1.0
- https://github.com/paperclipai/paperclip/releases/tag/v2026.1012.0
