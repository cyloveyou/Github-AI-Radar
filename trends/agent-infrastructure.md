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

## 2026-09-29 update — Runtime enforcement moves outside the agent

NVIDIA 在 2026-09-28 发布 Open Agent Safety Platform，将 OpenShell secure runtime 与 Sentry out-of-band watchdog 组合为从软件到硬件/基础设施的 Agent 控制层。OpenShell 在 sandbox 外部执行文件、system call、网络与凭据策略，并对策略变更做形式化检查；Sentry 则把高风险监督进一步放到独立的硬件信任域。

这使当前演化链继续扩展为：

**Skills → Context/Memory → Computer Use → Harness → Sandbox → Runtime/Control Plane → Portable Authority → Runtime Policy Enforcement → Independent Oversight**

与 9 月 26 日 Docker Sandbox Kit v3 的 Portable Authority 信号结合看，Agent 基础设施正在同时解决两个问题：**权限如何声明/分发**，以及 **权限如何在 Agent 无法绕过的边界上被真正执行**。

## 2026-10-06 — Kubernetes-native sandbox becomes an Agent workload primitive

`kubernetes-sigs/agent-sandbox` v1.0.5 strengthens a new control-plane layer: declarative Sandbox CRDs, warm pools, durable claim adoption, direct runtime transports, framework adapters, browser/MCP bridging, observability, and interchangeable isolation backends. The important shift is from “sandbox as a security feature” to **sandbox as a schedulable, recoverable and observable Agent workload primitive**.

Current infrastructure chain:

`Harness → Sandbox → Runtime / Control Plane → Portable Authority → Runtime Policy Enforcement → Kubernetes-native Agent Workload Primitive`

Watch next: cross-provider Sandbox API compatibility, E2B-compatible gateways, snapshot/suspend-resume semantics, and whether Agent frameworks standardize pluggable sandbox providers.

## 2026-10-07 — Agent work becomes reproducible, not merely executable

`tester-army/e2e` 将自然语言驱动的 Web/Mobile 操作与显式断言、后续确定性重放结合，展示从「Agent 能完成动作」到「动作能被复验并纳入 CI」的转变。同期 `tigerless-labs/autoharness` 把 Skill 的在线生成与治理做成生命周期；`CopilotKit/OpenDots` 在此前 OpenMuse 基础上继续整合持久 per-agent computer、审批和后台任务。

新增评估维度：Agent 操作的重放命中率、断言稳定性、技能复用与变更可审计性。这与 10 月 6 日 Kubernetes-native Sandbox Control Plane 属于互补层次，不能用一个层面的 Star 热度替代另一个层面的工程验证。

## 2026-10-09 — Persistent workspace meets human-takeover control plane

`paperclipai/paperclip` v2026.1005.0 将 per-agent 文件跨任务持久化、GitHub Skill 安装快照、MCP 连接器、Browser Use Cloud 实时观察/人工接管、多 Harness runner 组合成 Agent 任务控制面。它与 Kubernetes-native Sandbox 互补：前者偏任务、文件、工具与人机协同治理，后者偏基础设施 sandbox workload 调度。

新增验证维度：状态恢复与并发文件冲突、技能供应链快照、浏览器接管授权与审计、Agent/人类控制权交接。Source: https://github.com/paperclipai/paperclip/releases/tag/v2026.1005.0

## 2026-10-10 — Cross-tool semantic and temporal policy enforcement

Strands Box v0.1.0 (2026-10-07) combines OS sandbox grants with an out-of-agent Dogwood default-deny policy engine. Controlled Shell/Python, egress gateway and MCP broker share an event history: a later HTTP request can be denied based on an earlier file read. Unlike OCI permission packaging or Kubernetes workload scheduling, the new axis is **history-aware cross-tool authorization**.

**Boundary:** Direct Agent filesystem calls are governed by OS grants, not individual Dogwood policy decisions. Developer preview is Apple Silicon macOS only; Linux planned. No independent security benchmark.

Sources: https://github.com/strands-agents/box ; https://strandsagents.com/blog/strands-box-the-big-picture/

## 2026-10-13 — Multi-harness team runtime needs explicit recovery semantics

`mvschwarz/openrig` v0.6.9/0.6.10 uses YAML-defined team seats, persistent agent identities, queue and daemon state, cross-host messaging, and recovery of Claude/Codex sessions. A remote send whose outcome is unknown is explicitly `Delivery UNCONFIRMED`; a partly restored seat is not reported as fully restored. Unlike Paperclip task control or Kubernetes sandbox workload scheduling, this is **multi-harness team orchestration with explicit delivery/recovery semantics**.

Watch: idempotency, duplicate execution after network timeout, persistent identity and access policy for cross-host seats. Sources: https://github.com/mvschwarz/openrig/releases/tag/v0.6.9 ; https://github.com/mvschwarz/openrig/releases/tag/v0.6.10

## 2026-10-17 — Versioned Sandbox config, snapshot fidelity, and Actor egress identity

Substrate v0.5.0 引入多版本 SandboxConfig、WorkerPool sandboxClasses、SnapshotFidelity 梯度与 preferred_fidelity；Actor JWT 可在 egress gateway 签发并注入网络策略，未配置策略时默认拒绝 DNS，系统入口默认拒绝。其与 Kubernetes Agent Sandbox 的 CRD/调度层互补，重点是 **versioned workload configuration → recovery fidelity → actor identity → controlled egress**。升级存在 Breaking Changes，安全性质需要实测而非仅看 release notes。

Source: https://github.com/agent-substrate/substrate/releases/tag/v0.5.0

## 2026-10-18 — Multi-harness workspace control requires host ownership and per-chat permissions

Orca v1.4.227/229 integrates per-native-chat Claude/Codex permission modes, desktop/mobile/SSH workspaces, explicit remote-host CLI control, and host-scoped workspace association. The critical runtime invariant is that a project on host A must not be confused with an identical-path project on host B. This complements OpenRig delivery/recovery and Paperclip task control rather than replacing them. Release notes describe fixes, not independent isolation validation.

Source: https://github.com/stablyai/orca/releases/tag/v1.4.229

## 2026-10-19 — Safer defaults and conditional automation

Ruflo v3.57.0 将 Codex 初始化默认权限改为 workspace-write/on-request/cached，要求显式开启高信任模式；本机 MCP bridge 检查 loopback Host 与 Origin 白名单，并强化策略账本的独立锚点校验。这是在 Harness 配置、MCP 入口和审计账本三层实施最小权限治理。需验证旧配置迁移与权限回归。

Rakazo 10 月 18 日主分支提交新增 RoutineWatch：监控文件、命令或集成工具结果的指纹，变化后才启动 Agent；检查失败则暂停并报告。形成 scheduled polling → deterministic change detection → conditional agent execution 的路线。该能力尚非正式 Release，需评估漏报、误报与延迟。

Mozilla Otari v0.28.0 要求显式声明可用模型供应商，未声明返回 424；本地无密钥模型也须注册。它与 Ruflo 工具权限互补：分别控制可调用的模型和 Agent 可执行的工具。升级是 Breaking Change。

Sources: https://github.com/ruvnet/ruflo/releases/tag/v3.57.0 ; https://github.com/elie222/rakazo/commit/4429327e918e555ec91b43eb5c974a81b72cc8c4 ; https://github.com/mozilla-ai/otari/releases/tag/v0.28.0


## 2026-10-20 — MicroVM sandbox lifecycle and cross-harness model routing

Perplexity SPACE combines Firecracker microVMs with async sandbox lifecycle, data-plane output streams, warm pools, snapshots and operator egress policies. The 2026-10-19/20 commits narrow network-policy exceptions and validate sandbox identifiers. Unlike Substrate's actor identity and recovery fidelity, this emphasizes an HTTP-compatible execution substrate and deployable network controls; changes are not yet a tagged release.

Magpie v0.1.1294 exposes a local cross-harness model gateway as an Ollama-compatible endpoint, following v0.1.1293's arbitrary Git-sourced Skills support. This complements Otari's provider allowlisting: policy says which provider may run; routing says how models and protocols are connected. Test credentials, subscription authorization and tool-call fidelity independently.

Sources: https://github.com/perplexityai/SPACE ; https://github.com/perplexityai/SPACE/commit/c17d28284d10 ; https://github.com/yetone/magpie/releases/tag/v0.1.1294

## 2026-10-21 — Recursive harness optimization, concurrent source control, and P2P agent messaging

Google Research Harness² makes the **harness itself** the optimization target: task-local Propose–Probe–Compose contrasts candidate configurations and task-to-task evidence updates a persistent improvement harness, without changing model weights. This differs from skill-only self-learning. Its executor is not sandboxed by default and network access must be constrained before trusted evaluation.

gitai v0.3.0 makes **multi-agent source control a server-side concurrency and verification problem**: compare-and-swap landing, changeset log, storage checkpoints, and explicit resolution proposals. Model-generated conflict resolutions can auto-land only after exact-tree tests pass. Storage migration is breaking and multi-host claims remain unverified.

Reason Network v0.12.1 adds a different layer: **cross-host/team P2P agent presence and messaging with human approval**, rather than task scheduling. Trust, membership revocation and offline message integrity deserve separate audits.

Sources: https://github.com/google-research/harness2 ; https://github.com/feder-cr/git-ai/releases/tag/v0.3.0 ; https://github.com/reason-machines/reason-network/releases/tag/v0.12.1

## 2026-10-22 — Durable execution is more than chat-history recovery

Vercel durable-harness uses Workflow SDK World to persist each agent session, in-flight turn, model call and tool call as a workflow event log. The design targets crash recovery across machines without re-executing non-repeatable tool effects. Claude Code/Codex execute in per-session sandboxes, with virtual workspaces for other harnesses. Unlike OpenRig's team seat recovery or Substrate's snapshot fidelity, this is **event-sourced tool execution with explicit replay/idempotency boundaries**. Experimental 0.0.x; crash-injection, replay safety and exactly-once effects have not been independently verified.

Source: https://github.com/vercel-labs/durable-harness ; https://vercel.com/docs/agent-harnesses

## 2026-10-23 — Mandatory sandbox resource budgets and protocol-level agent messaging

Substrate v0.6.0 makes CPU/memory limits mandatory for Actors, verifies image layers by diffID before caching, separates per-Actor snapshots and uses dedicated GCS snapshot identities. Compared with v0.5.0's versioned SandboxConfig and Actor JWT, the boundary advances to **enforced resource budgets → artifact integrity → snapshot/credential isolation → authenticated ingress**. This is a breaking upgrade; no independent tenant-isolation test is implied.

SCP (@scp-dev/core@0.10.1) proposes a spec-led message layer for Claude/Codex/OpenCode/pi: harness hooks/MCP, per-machine brokers, relay and optional mesh, turn-level delivery and hibernated-session wakeup. It differs from Reason Network's P2P presence layer by explicitly defining delivery hooks and bindings. It is not yet a proven interoperable standard; test duplicate delivery, revocation and crash recovery.

Sources: https://github.com/agent-substrate/substrate/releases/tag/v0.6.0 ; https://github.com/scphq/scp ; https://scp.dev/spec

## 2026-10-24 — One-time wake claims and server-side agent reference boundaries

SCP Broker 0.9.0 turns dormant worker recovery into a **revive record → one-time wake ticket → original endpoint reclaim** flow; the worker can keep its mail, groups and address after a stop/remove. Background Claude workers can be stopped after 600 seconds of inactivity under restricted conditions, and resumed when addressed. This makes session identity and delivery state explicit, but does not independently establish exactly-once semantics.

gitai 0.4.0 applies exact branch resolution across operation RPCs and prohibits agent writes to internal refs at the server layer. Operator-only repository creation separates infrastructure authority from task agents. Together, the changes illustrate **cross-harness lifecycle identity** and **server-enforced source-control authority** as complementary control-plane invariants.

Sources: https://github.com/scphq/scp/releases/tag/%40scp-dev/broker%400.9.0 ; https://github.com/feder-cr/git-ai/releases/tag/v0.4.0


## 2026-10-25 — Portable sandbox enforcement and human-aware durable teams

NVIDIA OpenShell v0.1.5 publishes a versioned Sandbox Protocol for independently implemented backends, makes supervisor policy push optional (vendor says ~100 ms versus ~10 s polling), adds OCSF authentication-denial events and OTLP export, and requires Kubernetes annotation/label allowlists. Unlike the September announcement of out-of-agent enforcement, this release makes **backend compatibility, policy propagation and audit export** concrete upgrade surfaces. The project reappeared on GitHub Trending's daily page (rolling 893 stars-today display); this is not a verified calendar-day Star delta.

Anthropic Sandbox Runtime v0.0.81 hardens Windows process-tree isolation with a write-restricted token, AppContainer egress fencing, safer stdin pipe handling and explicit loopback installation. This is a Windows-only update, not a new macOS/Linux security claim. OpenRig v0.7.0 adds human quiet hours and away modes, partial team restoration and clean agent environment inheritance. Together they suggest **sandbox policy + portable backend + human availability + partial recovery** are distinct production-runtime requirements.

Sources: https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.5 ; https://github.com/anthropics/sandbox-runtime/releases/tag/v0.0.81 ; https://github.com/mvschwarz/openrig/releases/tag/v0.7.0

## 2026-10-26 — Per-seat identity and bounded managed-agent controls

OpenRig v0.7.1/0.7.2 adds per-seat terminal intervention and typing guards, dedicated Claude/Codex credential homes, and handover-acknowledged runtime switching. Existing seats keep the former full-control preset; upgrades and downgrades require explicit permission review, especially for Claude tool rules and Linux D-Bus access. This extends Oct 25's quiet-hours/recovery story to **per-seat identity, least privilege and controlled harness replacement**.

Ruflo v3.63.0 adds opt-in managed-agent MCP capabilities, explicit budgetCents, host-gated per-session control/interrupt, and signed advisory-learning records. Official notes say the Anthropic Managed Agents beta path has **not** been live-tested; evidence is only partly bound to execution, so the signed record is not proof of correct behavior.

**Shift:** team scheduling → identity + policy + budget + verifiable control action + recoverable handoff. Test interrupted switches, revoked accounts, budget exhaustion and tampered verification records.

Sources: https://github.com/mvschwarz/openrig/releases/tag/v0.7.1 ; https://github.com/mvschwarz/openrig/releases/tag/v0.7.2 ; https://github.com/ruvnet/ruflo/releases/tag/v3.63.0
