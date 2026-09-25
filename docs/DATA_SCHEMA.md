# Data Schema

`data/projects.json` 是 Radar 的项目主索引。

每个项目建议包含：

```json
{
  "owner/repo": {
    "name": "repo",
    "repo_url": "https://github.com/owner/repo",
    "categories": ["agent-runtime"],
    "first_seen": "YYYY-MM-DD",
    "last_reported": "YYYY-MM-DD",
    "reports": ["daily/YYYY/MM/YYYY-MM-DD.md"],
    "status": "watching"
  }
}
```

## Principles

- `owner/repo` 是稳定主键；
- 日期使用 ISO 8601；
- `reports` 必须指向仓库内存在的 Markdown 日报；
- 动态 Stars 等快照数据后续进入 `data/snapshots/`，避免覆盖历史观察；
- 不把未经验证的推测写进结构化数据。
