# Efficient Decision Layer

## Signal

kev 与 laya 在同一时期快速上升，值得关注的不是单个项目，而是一个架构信号：

> Agent 的每一步不一定都需要大型生成模型。

高频、结构化的分类、评分、路由、是否升级处理等任务，可以尝试交给更小、更快的模型；大型模型只处理复杂推理与生成。

## Possible architecture

```text
Input
  ↓
Small Decision / Routing Model
  ├── simple → deterministic tool / workflow
  └── complex → LLM reasoning
                 ↓
              Skills
                 ↓
          Sandbox / Runtime
```

这类设计若得到验证，可能显著降低科研自动化 Agent 的成本和延迟。
