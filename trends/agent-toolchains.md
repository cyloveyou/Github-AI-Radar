# Domain Agent Toolchains and Verifiable Artifacts

## 2026-10-08 — Evidence-first domain tools + validation of generated artifacts

REA 5.0.0 通过 MCP 把 Ghidra / Hopper / IDA、APK/JADX、网站运行时证据、JS/Electron 和固件分析接入 Coding Agent，并通过证据定位与限制说明约束结论；其 GitHub Trending 当日热度显示该专业场景正在加速。diagram-design 的跨宿主图形 Skill 则通过几何、数据守恒和结构一致性 CI gates，推动产物从“可生成”走向“可验收”。

**Emerging pattern:** Specialized toolchain → Agent integration → Evidence provenance → Verification gates → Reusable artifact.

本趋势不同于 Sandbox / Runtime 的隔离和调度问题，也不同于 10-07 的 Skill 自学习：关注的是领域知识调用后，成果是否可复核。独立性能与可靠性验证仍不足，不能以 Star 替代准确率。

Sources: https://github.com/morluto/rea/releases/tag/rea-agents-5.0.0 ; https://github.com/cathrynlavery/diagram-design

## 2026-10-09 — REA 6.0: tighter tool contracts and renewed breakout

`morluto/rea` 于 2026-10-08 发布 v6.0.0：MCP 本地文件输入改为绝对主机路径（breaking change），扩展 ELF、Windows PE、LLDB、crash、历史浏览器证据和 EVM 分析。10-08 与 10-09 两次 GitHub REST 快照净增 9,147 Stars（非自然日增量），属于已收录项目的二次爆发，不重复视为新项目。

Source: https://github.com/morluto/rea/releases/tag/rea-agents-6.0.0

## 2026-10-10 — REA canonical Evidence and typed provenance contracts

REA v6.2 / v6.3 makes canonical Evidence, profile-bound observations, producer and transaction identity, typed WebMCP schema hashes, event journals and inline evidence contexts required parts of analysis outputs. Missing provenance is rejected rather than silently repaired. Two official GitHub REST snapshots approximately 24.35 hours apart show +19,960 Stars, which is a snapshot delta, not calendar-day growth.

The direction is **Agent toolchain → typed observations → provenance/integrity contract → auditable comparison**. These are breaking changes; archived evidence may need recapture, and independent accuracy benchmarks are not yet established.

Sources: https://github.com/morluto/rea/releases/tag/rea-agents-6.2.0 ; https://github.com/morluto/rea/releases/tag/rea-agents-6.3.0

## 2026-10-12 — Bounded evidence retrieval and runnable visual artifacts

REA 6.4.0 把大型分析的保留证据改为可按摘要/选定视图读取，JS 分析隔离在带内存和超时上限的独立进程，并在资源不足时保留已知事实、明确标记未知项。相较 10-10 快照，约 47.47 小时净增 57,571 Stars（非自然日增量），但 Star 不能代表部署或准确性。

新项目 Anatomy v1.0.0 用 SVG/WebGL/3D 和几何审计制作交互式技术示意图；answer-me-with-html v0.5.0 将 Agent 复杂回答打包为可离线交互的 HTML，包含 ER 图、变更标记和远程预览。与已收录 diagram-design 一起形成 **可运行产物 + 自动检查 + 人工复核** 的互补路线。形式验证不能替代科学正确性。

Sources: https://github.com/morluto/rea/releases/tag/rea-agents-6.4.0 ; https://github.com/wheresryan22/anatomy/releases/tag/v1.0.0 ; https://github.com/QingYunA/answer-me-with-html/releases/tag/v0.5.0

## 2026-10-13 — Agent artifacts reach CAD/engineering handoff

`earthtojake/text-to-cad` connects agent Skills/MCP to local CAD generation, STEP/GLB/STL/3MF export, engineering drawings, DFM checks and fabrication workflows. This extends the earlier diagram-design/Anatomy emphasis on inspectable visual outputs toward **engineering-format artifacts and manufacturing handoff**. DFM checks cannot substitute for mechanical verification, tolerancing or independent engineering review. Source: https://github.com/earthtojake/text-to-cad

## 2026-10-14 — Agent-native video artifacts and manifest-based distribution

HyperFrames 将 HTML/CSS 与可寻址动画时间轴渲染为 MP4，提供跨 Coding Agent 的 Skills 和渲染 CLI，把可验证 Agent 成果物从图表、CAD 扩展到 **可重复执行的时间型媒体**。v0.8.155 修复 FFmpeg 边缘黑条并验证编码参数，但不是重大发布；跨平台逐帧一致性仍需独立测评。

Cursor 官方 plugins 仓库以 `.cursor-plugin/plugin.json` 为插件声明入口，形成 Skills、连接器与工作流的分发层。官方目录不等于第三方插件权限已独立审计。

Sources: https://github.com/heygen-com/hyperframes ; https://github.com/heygen-com/hyperframes/releases/tag/v0.8.155 ; https://github.com/cursor/plugins
