<div align="center">

# 🤖 GitHub AI Radar

### Track what is actually changing in open-source AI.

**面向科研与开发工作流的 GitHub AI 开源趋势雷达**

[Daily Reports](./daily/) · [Trend Notes](./trends/) · [Weekly Reviews](./weekly/) · [PDF Archive](./pdf/) · [Methodology](./docs/METHODOLOGY.md) · [Maintenance](./docs/MAINTENANCE.md)

![Status](https://img.shields.io/badge/status-active-success)
<!-- RADAR_BADGES_START -->
![Tracked](https://img.shields.io/badge/tracked_projects-94-blue)
![Reports](https://img.shields.io/badge/daily_reports-33-blueviolet)
<!-- RADAR_BADGES_END -->
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## 🌐 What is GitHub AI Radar?

GitHub AI Radar 持续观察 GitHub 上**当前热门和快速上升的 AI 开源项目**，重点关注：

**Agent · Coding Agent · AI Tools · RAG / Context · Browser Agent · Computer Use · Local Models · Automation · Agent Runtime · Sandbox · Memory**

它不是 GitHub Trending 的简单搬运，也不追求机械日更。

> **只有出现真正值得关注的新项目、新爆发趋势、显著热度变化或技术路线转折时，才生成新的 Radar Report。**

我们的目标不是回答“今天哪个项目 Star 最多”，而是持续回答：

- 什么项目正在突然加速？
- 为什么它**现在**值得关注？
- 它代表了怎样的技术路线变化？
- 它对科研与真实开发工作流有什么价值？
- 连续几周之后，开源 AI 生态究竟往哪里走？

---

## 🔥 Recent Highlights

| Date | Project / Signal | Area | Why it matters |
|---|---|---|---|
| **10-27** | **JetBrains ThinkRail** | Coding Agent · IDE · Worktree | 相邻 REST 快照 +1,178 Stars；pi + SPEC.md 持久规范与 PR/CI 流程，首次收录 |
| **10-27** | **NVIDIA SkillSpector v2.13.1** | Agent Skills · Security Audit | 71 检测模式/17 类风险；误报、覆盖缺口与报告输出安全修复，首次收录 |
| **10-27** | **HarnessRouter v0.37.1–0.37.3** | Multi-Harness · Unified API | 工具流式可观测、MCP 路径修复与 Skill 误执行风险修复，首次收录 |
| **10-27** | **Agent Reach v1.6.0** | Browser Agent · Session | 专用登录浏览器、平台能力路由与会话迁移风险，首次收录 |
| **10-27** | **Omnigent v0.19.0** | Meta-Harness · Control Plane | MCP Registry/Gateway 策略、Git SSH 凭据代理及离线恢复，首次收录 |
| **10-26** | **Hallmark** | Coding Agent · Design Skills | 三层设计门槛、八宽度浏览器检查与重设计保真；首次收录 |
| **10-26** | **Impeccable** | Coding Agent · Browser Audit | 24 命令、62 确定性规则、CDP 实时检查；首次收录 |
| **10-26** | **Experiential** | Model Gateway · Agent Routing | 统一模型 API、身份/预算控制与轨迹反馈路由；首次收录 |
| **10-26** | **OpenRig v0.7.1–0.7.2** | Multi-Harness · Control Plane | 每席位权限/账户、跨 Harness 交接与升级回退风险 |
| **10-26** | **Ruflo v3.63.0** | Managed Agents · Runtime | 预算上限、白名单控制、签名建议学习；云端路径尚未实测 |
| **10-25** | **NVIDIA OpenShell v0.1.5** | Sandbox · Runtime · Audit | 版本化 Sandbox Protocol、可选策略 Push、OCSF 审计；二次上榜而非新项目 |
| **10-25** | **Paperclip v2026.1023.0** | Control Plane · Privacy | 私有任务权限、Break-glass 审计、未计价预算默认阻断；Operator 权限升级须审查 |
| **10-25** | **OpenRig v0.7.0** | Multi-Agent · Recovery | 人类 Quiet Hours、部分 Seat 恢复、干净启动环境与交付不确定性 |
| **10-25** | **Anthropic Sandbox Runtime v0.0.81** | OS Sandbox · Windows | Windows 受限令牌、AppContainer 出站与 stdin 端点修复；仅 Windows 更新 |
| **10-25** | **Cindy v0.1.115** | Multi-Harness · Desktop Agent | 跨 Harness 桌面客户端热度上升；开源范围不包含托管后端 |
| **10-24** | **Open Math Harness v0.41.0** | Scientific Harness · Formal Verification | 能力内核、并行数学探索和 Lean 证明检查；完整交互运行时仍依赖平台 |
| **10-24** | **OPAL** | Coding Agent · ML Training | 训练过程中由 Agent 重写 PyTorch 优化器；生成代码不在沙箱中 |
| **10-24** | **VVV v0.1.1** | Agent Tools · Video Artifacts | 可编辑 Remotion 模板、质检与跨 Agent 成果包 |
| **10-24** | **gitai v0.4.0** | Multi-Agent Source Control | 精确分支解析、服务端 Agent 权限边界与操作员建库 |
| **10-24** | **SCP Broker 0.9.0** | Agent Runtime · Session Recovery | 一次性唤醒票据与休眠 Endpoint 身份恢复 |
| **10-20** | **Perplexity SPACE** | Agent Sandbox · Firecracker | 微虚拟机生命周期、异步执行、warm pools 与网络策略；10 月 20 日提交级加固 |
| **10-20** | **Headroom v0.41.0** | Context · Compression · Proxy | 跨协议请求压缩、可恢复缓存与按 Agent 费用归因 |
| **10-20** | **ESP32 iPhone Agent** | Computer Use · iOS | ESP32-S3 AirPlay/USB HID + 同机 iPhone Agent；主分支新架构，尚非新 Release |
| **10-20** | **Magpie v0.1.1294** | Coding Agent · Model Gateway | Ollama 兼容入口、跨 Harness 模型路由和 Git Skills |
| **10-20** | **Scout** | Browser Agent · Model Routing | Browser hands/eyes/brain/extract 分工与云端/本地/CDP 运行 |
| **10-19** | **Ruflo / Rakazo / Graphify / TencentDB Memory / Otari** | Policy · Automation · Context | 默认权限、事件触发、代码图谱保真、记忆决策与供应商白名单 |
| **10-18** | **Orca v1.4.229** | Multi-Harness · Remote Workspaces | 原生会话权限、SSH/手机协作与跨主机所有权修复 |
| **10-18** | **Android Skills v1.0.15** | Domain Skills · Android | Google 官方 LiteRT、Compose 性能与车载开发技能 |
| **10-18** | **billion-context v0.1.198–199** | Context · Long-lived Agent | 增量摄取、状态持久化与会话恢复竞态修复 |
| **10-17** | **PageIndex v0.4.1** | RAG · Agent Tools | Flash 布局优先索引与本地/云端统一检索工具契约 |
| **10-17** | **Substrate v0.5.0** | Sandbox · Actor Runtime | 配置版本化、快照恢复保真度、Actor 身份与默认拒绝出站 |
| **10-17** | **XERJ rc.96** | Retrieval · Audit | 公开未通过的错误且自信检测门槛，区分来源签名与结论可靠性 |
| **10-16** | **XERJ signed corpus** | RAG · Agent Memory · Supply Chain | 签名 Agent 轨迹语料、时效校验与可追溯检索来源 |
| **10-16** | **Scientific Agent Skills** | Scientific Agent · Skills | 177 项科研技能与开放标准，强调科研工作流验证 |
| **10-16** | **VoiceStudio** | Local Models · MCP · Multimodal | 本地语音工具向 Coding Agent 的 MCP 接口扩展 |
| **10-15** | **iFixAi** | Agent Audit · Evaluation | 独立行为探针、跨供应商评判与评分可靠性修复，首次收录 |
| **10-15** | **Paperclip v2026.1012** | MCP · Delegated Authority | 外部助手经用户授权进入控制面，工具授权 fail-closed |
| **10-15** | **REA v6.5** | Evidence · Bounded Retrieval | 严格源文件范围、跨 bundle provenance 与分页证据 |
| **10-14** | **HyperFrames** | Coding Agent · Video Artifact | HTML/CSS/可寻址动画生成可重复渲染 MP4，Agent Skill 路由与编码参数校验 |
| **10-14** | **claude-mem v13.39** | Memory · Subagent Lifecycle | Codex 子 Agent 压缩后按线程标识恢复记忆时间线，避免重复注入 |
| **10-14** | **Cursor Plugins** | Coding Agent · Plugin Manifest | 官方插件目录以 Manifest 分发 Skills、连接器与团队工具 |
| **10-13** | **OpenRig v0.6.10** | Multi-Harness · Team Runtime | 持久 Agent 团队与跨主机消息、会话恢复、交付不确定性显式处理 |
| **10-13** | **Context Mode** | Context · MCP · Memory | 工具输出沙箱化、SQLite FTS5 事件索引与按需上下文路由 |
| **10-13** | **text-to-cad** | Coding Agent · CAD · Artifacts | 从图形生成走向 STEP/DFM 与制造交接的工程成果物 |
| **10-12** | **REA v6.4.0** | Evidence · Bounded Execution | 大型分析按需证据检索、独立受限进程和显式部分失败；两次 REST 快照再度显著加速 |
| **10-12** | **Anatomy v1.0.0** | Skills · Interactive Visualization | SVG/WebGL/3D 技术示意图附几何审计与浏览器检查 |
| **10-12** | **answer-me-with-html v0.5.0** | Skills · HTML Artifact | Agent 答案输出可交互 HTML，ER 图、变更标记和远程预览 |
| **10-10** | **Strands Box v0.1.0** | Sandbox · Temporal Policy | 跨 Shell/Python/MCP/HTTP 共享事件历史的语义授权，OS 隔离与外部策略组合 |
| **10-10** | **REA v6.2–v6.3** | MCP · Canonical Evidence | 证据身份/来源/完整性成为类型化契约，持续爆发但不重复视为新项目 |
| **10-09** | **Paperclip v2026.1005.0** | Agent Control Plane · Browser Use | 持久 Agent 工作区、Skill 快照与可接管浏览器统一到任务控制面 |
| **10-09** | **Hindsight v0.10.3** | Memory · Coding Agent | 将历史事实记忆与团队行为指导分离，强化跨 Harness 记忆治理 |
| **10-09** | **REA 6.0** | MCP · Evidence-first Toolchain | 路径输入契约破坏性升级，已收录项目出现可核验二次爆发 |
| **10-08** | **REA 5.0** | Coding Agent · MCP · Reverse Engineering | 专业分析工具聚合为带证据定位的 Agent 工作流，GitHub Trending 显著爆发 |
| **10-08** | **diagram-design** | Skills · Verifiable Artifact | 跨宿主图表 Skill 引入几何、数据守恒和导出 CI 校验 |
| **10-07** | **autoharness** | Self-learning Skills · Harness | 真实会话生成的 Skill 开始有合并、证据账本与归档生命周期 |
| **10-07** | **Agent Memory Repo** | Context · Memory Specification | Git/Markdown 记忆从单一实现进一步向跨 Agent 共享格式推进 |
| **10-07** | **tester-army/e2e** | Agent Testing · Browser/Mobile | 自然语言探索动作与确定性断言、后续重放结合 |
| **10-06** | **Kubernetes agent-sandbox** | Runtime · Control Plane | Sandbox 成为可调度、可预热、可恢复的 Agent workload primitive |
| **10-03** | **Strands Decider / Clef** | System-1 · Decision Layer | Agent 高频路由与评分开始从生成式 LLM 拆分为专用决策模型 |
| **09-29** | **NVIDIA OpenShell** | Runtime Policy Enforcement | 在 Agent 外部实施权限与运行时策略，强化隔离执行边界 |

➡️ [Browse latest daily reports](./daily/2026/10/) · [Read PDF archive](./pdf/)

---

## 🧭 Current Trend Map

```text
                         Open-source AI Agent Ecosystem
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
       Knowledge Layer          Execution Layer         Infrastructure
             │                        │                        │
       RAG / Context             Browser Agent               Skills
          Memory                Computer Use                Harness
             │                        │                     Sandbox
             │                        │                     Runtime
             └────────────────────────┼─────────────── Control Plane
                                      │
                              Decision / Routing
                                      │
                         Small & Efficient Models
```

### What we are seeing

近期项目并不是互相孤立的热点，而正在形成一条比较清晰的演进路线：

**Agent Framework → Skills → Context / Memory → Browser / Computer Use → Sandbox → Runtime / Control Plane → Efficient Decision Layer**

这意味着开源 Agent 的竞争焦点正在从“做出一个聪明的 Demo”，逐渐转向：

> **如何让 Agent 长期、可靠、安全、低成本地完成真实任务。**

📖 [Agent Infrastructure](./trends/agent-infrastructure.md) · [Context & Memory](./trends/context-memory.md) · [Browser & Computer Use](./trends/browser-computer-use.md) · [Efficient Decision Layer](./trends/efficient-decision-layer.md) · [Agent Audit](./trends/agent-audit.md)

---

## 🧪 Why this matters for research

这个 Radar 特别关注项目对**科研工作流**的真实价值。

例如，一个完整的科研 Agent 未来可能是：

```text
Literature / Data / Task
          │
          ▼
  Context & Memory
          │
          ▼
 Small Decision Layer
   ├── simple ──→ deterministic workflow
   └── complex ─→ LLM reasoning
                     │
                     ▼
                   Skills
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    Browser Agent         Computer Use
          │                     │
          └──────────┬──────────┘
                     ▼
             Sandbox / Runtime
                     │
                     ▼
          Results / Figures / Reports
```

在真实科研环境里，这可能对应：文献检索 → 数据下载 → 数据质量检查 → Python/GMT/QGIS 处理 → 绘图 → 结果验证 → 报告生成。

---

## 📊 Radar at a glance

<!-- RADAR_STATS_START -->
| Metric | Current |
|---|---:|
| Tracked projects | **94** |
| Triggered daily reports | **33** |
| Trend notes | **7** |
| Weekly reviews | **1** |
| Historical PDF reports | **31** |
| First observation | **2026-09-17** |
<!-- RADAR_STATS_END -->

> 这里的数字代表 Radar 已归档的数据，而不是整个 GitHub AI 生态的项目总量。

---

## 📚 Reports

### Daily Radar

日报是最细粒度的观察记录：

`daily/YYYY/MM/YYYY-MM-DD.md`

**没有实质变化的日期不会生成文件。**

➡️ [Open Daily Reports](./daily/)

### Weekly Review

周报不重复每日项目，而是寻找跨项目、跨日期的结构性变化。

➡️ [Open Weekly Reviews](./weekly/)  
➡️ [2026 W39 Review](./weekly/2026-W39.md)

### PDF Archive

Markdown 是 GitHub 上的主要阅读入口；PDF 用于固定版式归档、下载、打印和邮件分发。

➡️ [Open PDF Archive](./pdf/)

---

## 🗂 Repository Structure

```text
Github-AI-Radar/
├── README.md
├── daily/                 # Markdown daily radar
│   └── YYYY/MM/
├── weekly/                # Weekly trend synthesis
├── trends/                # Long-running trend notes
├── pdf/                   # Publication-style PDF archive
│   └── YYYY/MM/
├── data/
│   ├── projects.json      # Project registry
│   └── snapshots/         # Historical observations
├── scripts/               # Validation / automation utilities
├── docs/                  # Methodology & documentation
├── assets/                # Static assets
└── .github/workflows/     # CI / future automation
```

---

## 🎯 What gets into the Radar?

一个项目不会仅仅因为 Star 多就自动进入日报。

我们主要观察五个维度：

| Dimension | Question |
|---|---|
| **Novelty** | 是否出现新的技术或产品路线？ |
| **Velocity** | 增长速度是否异常？ |
| **Persistence** | 热度是否持续，而非一次性噪声？ |
| **Practicality** | 是否能进入真实科研/开发工作流？ |
| **Ecosystem Signal** | 是否能解释更大的 AI 生态变化？ |

详细口径见 [Methodology](./docs/METHODOLOGY.md)。

---

## ⚡ Update Policy

```text
Scan GitHub
     │
     ▼
Compare with previous observations
     │
     ├── No meaningful change ──→ Do nothing
     │
     ▼
New breakout / major change / trend shift
     │
     ├── Update daily report
     ├── Update project registry
     ├── Update trend notes
     ├── Archive PDF when available
     └── Surface the important signal
```

因此，**日期不连续是设计的一部分，而不是数据缺失。**

---

## 🛠 Utilities

一键执行常规维护：

```bash
python3 scripts/maintain.py
```

验证仓库结构：

```bash
python3 scripts/validate_repo.py
```

更新 README 自动统计：

```bash
python3 scripts/update_readme_stats.py
```

重建 PDF Archive 索引：

```bash
python3 scripts/update_archive_index.py
```

项目主索引位于：

```text
data/projects.json
```

---

## ⚠️ Data Notes

GitHub Star、Trending 排名和增长速度都是动态注意力指标，不等价于软件质量、研究水平或长期价值。

历史日报中的数值反映对应观察时刻的快照。Radar 更重视**增长数量级、持续性、项目内容和生态信号**，而不是对瞬时数字做过度精确的排名。

---

## 🤝 Contributing

欢迎提交值得跟踪的 AI 开源项目、趋势线索或数据修正。

请尽量说明：

- GitHub repository；
- 项目解决的问题；
- 为什么**现在**值得关注；
- 可验证的增长或技术信号；
- 对科研、开发或 Agent 工作流的实际价值。

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## 📄 License

仓库原创文字与代码采用 [MIT License](./LICENSE)。

第三方项目名称、商标、代码和链接归各自权利人所有。

---

<div align="center">

**GitHub AI Radar**

*Less noise. More signal.*

</div>
