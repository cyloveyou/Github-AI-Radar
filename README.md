<div align="center">

# 🤖 GitHub AI Radar

### Track what is actually changing in open-source AI.

**面向科研与开发工作流的 GitHub AI 开源趋势雷达**

[Daily Reports](./daily/) · [Trend Notes](./trends/) · [Weekly Reviews](./weekly/) · [PDF Archive](./pdf/) · [Methodology](./docs/METHODOLOGY.md) · [Maintenance](./docs/MAINTENANCE.md)

![Status](https://img.shields.io/badge/status-active-success)
<!-- RADAR_BADGES_START -->
![Tracked](https://img.shields.io/badge/tracked_projects-26-blue)
![Reports](https://img.shields.io/badge/daily_reports-9-blueviolet)
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
| **09-24** | **kev / laya** | Small Model · Decision Layer | 小模型开始承担 Agent 高频分类、评分和路由，形成“大模型复杂推理 + 小模型高速决策”的潜在分层 |
| **09-24** | **unreal-agent** | Async Agent Harness | 异步任务、可持久化与可 fork 会话历史开始进入 Harness 核心设计 |
| **09-23** | **Google ax** | Runtime · Orchestration | Agent 从单个 CLI 进程进一步走向可调度、可隔离的 Runtime |
| **09-22** | **agent-native** | Actions · Agent App | 一次定义 Action，同时服务 Agent、UI、HTTP、MCP、A2A 与 CLI |
| **09-22** | **ai-memory** | Context · Memory | 用 Git + Markdown 把 Agent 长期记忆变成可读、可 diff、可回滚的项目资产 |
| **09-20** | **CUA** | Computer Use | Agent 执行层从 Browser 进一步扩展到完整桌面与跨应用工作流 |
| **09-18** | **BrowserSkill** | Browser Agent | 真实 Chromium 登录态开始成为 Agent Skill 的一部分 |

➡️ [Browse all daily reports](./daily/2026/09/) · [Read PDF archive](./pdf/)

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

📖 [Agent Infrastructure](./trends/agent-infrastructure.md) · [Context & Memory](./trends/context-memory.md) · [Browser & Computer Use](./trends/browser-computer-use.md) · [Efficient Decision Layer](./trends/efficient-decision-layer.md)

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
| Tracked projects | **26** |
| Triggered daily reports | **9** |
| Trend notes | **4** |
| Weekly reviews | **1** |
| Historical PDF reports | **7** |
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
