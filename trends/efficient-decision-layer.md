# Efficient Decision Layer

## Signal

9 月 24 日，kev 与 laya 同期上升给出的初始信号是：

> Agent 的每一步不一定都需要大型生成模型。

到 10 月 3 日，这条路线已经得到更强的独立确认：Strands Labs 公开 `strands-decider`，Cloudflare 发布 Clef / Clef-flash。重点已从泛化的 “small model” 转向专门的 **Decision Model / System-1 Layer**。

## Architecture shift

```text
Input / State
    ↓
System-1 Decision Model
    ├── routing / tool selection
    ├── argument checks / guardrails
    ├── scoring / triage
    └── confidence gate
             ├── high confidence → deterministic tool / workflow
             └── low confidence  → LLM reasoning
                                      ↓
                                   Skills
                                      ↓
                               Sandbox / Runtime
```

## Why it matters

- **Bounded output:** 选择、评分、置信度替代自由文本生成，更适合高频结构化判断；
- **Lower latency/cost:** 不必让大型 LLM 承担每一次 routing、classification 和 guardrail；
- **Hybrid agent:** 大模型集中处理复杂推理，decision model 处理重复决策；
- **Training loop:** Cloudflare 已把 AI Gateway 数据、RL sandbox、trainer 与重新部署串成闭环；
- **Operational control:** calibrated confidence 可以直接成为自动执行、升级大型模型或人工复核的门限。

## Radar milestones

- **2026-09-24:** `jaredpalmer/kev` + `NandhaKishorM/laya` — small decision-layer signal.
- **2026-10-03:** `strands-labs/strands-decider` + Cloudflare Clef/Clef-flash — System-1 decision model becomes an explicit agent architecture layer.

后续重点观察：benchmark 是否稳定、是否出现跨 harness 的 decision API、是否与 sandbox policy / runtime enforcement 直接结合。

## 2026-10-26 — Routing optimization moves into the model gateway

Experiential offers an OpenAI-compatible local gateway and a separate hosted service, with model/provider routing, per-user/agent budget and access constraints, and trace-driven router optimization. This complements the decision-model route (Strands Decider / Clef): a decision policy can be implemented at the traffic gateway rather than inside every Agent. The Oct 25 GitHub v0.7.220 record was restored from an existing PyPI release and is **not** evidence of a fresh algorithm launch.

**Next test:** fixed request set, identical provider costs and quality labels, per-agent budget enforcement, trace opt-in/out and actual data egress. “Zero markup” and optimization gains are project claims, not verified results.

Sources: https://github.com/experientiallabs/experiential ; https://github.com/experientiallabs/experiential/releases/tag/v0.7.220

## 2026-10-30 — Hardware-adaptive local inference joins Agent runtime economics

Magnitude's inference engine tunes kernels per model/hardware and exposes local model serving for Coding Agents. Its 2026-10-29 CLI 0.2.14 adds hardware-specific speed ordering, download resilience and a project-reported ~13% lower per-token CPU decode time for one Q4 Qwen3.5 4B/M4 Pro configuration. This is an inference execution layer, not a new reasoning algorithm; benchmark on identical hardware, quantization, context and model output before accepting broad 2x claims.

Sources: https://github.com/magnitudedev/magnitude ; https://github.com/magnitudedev/magnitude/releases/tag/%40magnitudedev%2Fcli%400.2.14
