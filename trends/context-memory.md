# Context & Memory

长上下文并不等于有效上下文。近期项目显示两条路线正在形成：

- **Compaction / Context Engineering**：只把当前任务真正需要的信息送入模型；
- **Durable Memory**：把长期知识、决策和项目状态放到可审计、可版本化的外部存储。

代表项目包括 fast-jev-compaction 与 ai-memory。

对科研项目而言，理想状态不是让模型“记住一切”，而是把实验结论、数据口径、踩坑、参数决策和待办变成项目内可读、可 diff 的资产。
