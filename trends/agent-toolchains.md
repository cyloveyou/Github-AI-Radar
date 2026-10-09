# Domain Agent Toolchains and Verifiable Artifacts

## 2026-10-08 — Evidence-first domain tools + validation of generated artifacts

REA 5.0.0 通过 MCP 把 Ghidra / Hopper / IDA、APK/JADX、网站运行时证据、JS/Electron 和固件分析接入 Coding Agent，并通过证据定位与限制说明约束结论；其 GitHub Trending 当日热度显示该专业场景正在加速。diagram-design 的跨宿主图形 Skill 则通过几何、数据守恒和结构一致性 CI gates，推动产物从“可生成”走向“可验收”。

**Emerging pattern:** Specialized toolchain → Agent integration → Evidence provenance → Verification gates → Reusable artifact.

本趋势不同于 Sandbox / Runtime 的隔离和调度问题，也不同于 10-07 的 Skill 自学习：关注的是领域知识调用后，成果是否可复核。独立性能与可靠性验证仍不足，不能以 Star 替代准确率。

Sources: https://github.com/morluto/rea/releases/tag/rea-agents-5.0.0 ; https://github.com/cathrynlavery/diagram-design

## 2026-10-09 — REA 6.0: tighter tool contracts and renewed breakout

`morluto/rea` 于 2026-10-08 发布 v6.0.0：MCP 本地文件输入改为绝对主机路径（breaking change），扩展 ELF、Windows PE、LLDB、crash、历史浏览器证据和 EVM 分析。10-08 与 10-09 两次 GitHub REST 快照净增 9,147 Stars（非自然日增量），属于已收录项目的二次爆发，不重复视为新项目。

Source: https://github.com/morluto/rea/releases/tag/rea-agents-6.0.0
