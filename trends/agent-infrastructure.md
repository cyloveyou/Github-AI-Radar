# Agent Infrastructure

## Thesis

2026 年 9 月中下旬的连续开源热点显示，Agent 竞争焦点正在从“谁的 Agent Demo 更聪明”转向 **谁能提供可靠的长期运行基础设施**。

## Evolution

1. **Skills** — 把专业能力模块化；
2. **Context / Memory** — 解决长任务状态与跨 Agent handoff；
3. **Browser / Computer Use** — 连接真实执行环境；
4. **Harness** — 统一工具与任务循环；
5. **Sandbox / Permission / Audit** — 控制执行风险；
6. **Runtime / Control Plane** — 调度多个 Agent、工作区和任务。

## Representative projects

- cloudflare/security-audit-skill — 专业 Skill
- akitaonrails/ai-memory — Git/Markdown 长期记忆
- Tencent/BrowserSkill — 真实浏览器会话
- trycua/cua — Computer Use
- deepseek-ai/deepseek-harness — Harness
- coder/coder — Sandbox / Dev Environment
- google/ax — Agent Runtime / Orchestration
- Nasiko-Labs/nasiko — Control Plane

## Research workflow implication

科研 Agent 若要长期进入生产环境，核心问题会逐渐从 prompt engineering 转为：**任务如何排队、数据如何隔离、权限如何限制、状态如何恢复、结果如何审计、失败如何重试。**

## 2026-09-26 update — Sandbox becomes a portable deployment boundary

Docker Cloud Sandboxes 与 Sandbox Kit Specification v3 把此前的 Sandbox / Runtime 主线再推进一层：Agent、工具和权限声明可以作为 OCI artifact 一起构建、分发、签名与扫描；相同隔离模型还可从本机迁移到云端长任务执行。OpenSandbox 的开放 Sandbox API 与 Microsoft Quicksand 的 QEMU VM 路线则说明，独立 sandbox runtime 正成为跨 Agent 的基础设施层。

因此当前演化链可以更新为：

**Skills → Context/Memory → Computer Use → Harness → Sandbox → Runtime/Control Plane → Portable Authority + Cloud Execution**

值得继续观察的核心问题是：OCI Kit / Sandbox Protocol 是否会像容器时代的镜像与运行时接口一样，形成 Agent 时代的可移植执行标准。
