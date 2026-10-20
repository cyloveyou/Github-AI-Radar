# Browser & Computer Use

BrowserSkill 与 CUA 代表了 Agent 执行层的两级扩展：

**Web API / Scraping → Browser Session → Full Computer Use**

真实科研工作流往往跨越登录网站、终端、QGIS、Panoply 和本地文件，因此 Computer Use 很有潜力。但能力越强，越需要 Sandbox、Permission、Audit 与 human-in-the-loop。


## 2026-10-20 — Physical iPhone control and model-specialized browser loops

ESP32 iPhone Agent's 2026-10-15 main-branch redesign replaces a runtime computer with an ESP32-S3 AirPlay receiver/USB HID board plus an on-device iPhone app. Initial firmware flashing and app build still require a Mac; the computer-free claim applies only to runtime. The redesign is not the v0.1.0 release. Run trace export and interruption recovery make physical device testing more inspectable.

Scout separates browser actions, screenshot interpretation, planning and extraction into configurable model roles; it can use cloud, local Chromium or CDP browsers. Its GitHub repository is an upstream mirror and has no release; claimed page reach is self-measured. Evaluate action replay, browser credentials, and cloud-vs-local privacy boundaries.

Sources: https://github.com/onehumanbeing/esp32-iphone-agent/commit/f911d841c0f6 ; https://github.com/outcrawlai/scout
