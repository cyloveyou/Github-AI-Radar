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
