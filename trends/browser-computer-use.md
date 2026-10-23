# Browser & Computer Use

BrowserSkill 与 CUA 代表了 Agent 执行层的两级扩展：

**Web API / Scraping → Browser Session → Full Computer Use**

真实科研工作流往往跨越登录网站、终端、QGIS、Panoply 和本地文件，因此 Computer Use 很有潜力。但能力越强，越需要 Sandbox、Permission、Audit 与 human-in-the-loop。


## 2026-10-20 — Physical iPhone control and model-specialized browser loops

ESP32 iPhone Agent's 2026-10-15 main-branch redesign replaces a runtime computer with an ESP32-S3 AirPlay receiver/USB HID board plus an on-device iPhone app. Initial firmware flashing and app build still require a Mac; the computer-free claim applies only to runtime. The redesign is not the v0.1.0 release. Run trace export and interruption recovery make physical device testing more inspectable.

Scout separates browser actions, screenshot interpretation, planning and extraction into configurable model roles; it can use cloud, local Chromium or CDP browsers. Its GitHub repository is an upstream mirror and has no release; claimed page reach is self-measured. Evaluate action replay, browser credentials, and cloud-vs-local privacy boundaries.

Sources: https://github.com/onehumanbeing/esp32-iphone-agent/commit/f911d841c0f6 ; https://github.com/outcrawlai/scout

## 2026-10-21 — Programmatic GUI actions and cross-device Computer Use

OpenGCUA v0.1.2 is an early research preview combining accessibility trees, app APIs, shell and GUI actions; a code-action agent expresses repeated interface operations as programs. Its public deliverables include OSWorld integration examples, model trajectories, preliminary macOS harness and cross-device SDK. The author's OSWorld-v2 partial-score gains are not independent full-task success rates.

This differs from ESP32 iPhone Agent's physical HID approach and Scout's browser-specialized model loop: **one agent chooses the interface abstraction**, rather than committing to one input modality. Evaluate authorization, code execution boundaries and human takeover.

Source: https://github.com/Tongyi-MAI/OpenGCUA/releases/tag/v0.1.2

## 2026-10-22 — Browser agents as generators of verified RL tasks

Browser Use rl-env-use turns real web cases and later outcomes into code-checkable gold answers, filters ambiguous/leaky/saturated tasks, and exports RL environments with prompt hillclimbing. It is **task/evaluation environment generation**, not another GUI control method. The trial forecasting numbers and Qwen improvements are author-reported, with a high 0.75 constant-probability baseline; independent validation must check temporal leakage, calibration and gold-answer construction.

Source: https://github.com/browser-use/rl-env-use

## 2026-10-23 — Accessibility-first, cross-harness Computer Use

axuse uses CDP and DOM/accessibility trees with stable element references and diffed snapshots as a single MCP tool surface for multiple coding-agent harnesses. Unlike OpenGCUA's broad GUI/API/Shell routing, it prioritizes **structured UI semantics over screenshot loops**. Windows desktop support, opt-in macOS TCC access and X11/XWayland Linux support are project-reported; there is no tagged release. Validate browser-bridge permissions, prompt-injection containment and comparable task success/token/latency against screenshot baselines.

Source: https://github.com/ctoldigital/axuse
