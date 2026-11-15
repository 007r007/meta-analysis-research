# AI Collaboration Log

> **给用户（人）的调度看板** — Claude Code 和 Codex 不会主动知道对方在做什么。你负责分配任务、锁定文件、合并结果。

---

## Current Goal

<!-- 写清楚当前要完成的任务，一句话 -->

等待导师对修改说明(revision_note_to_supervisor.docx)的反馈，收到后启动修订

---

## Active Lock

| 文件 | 锁定者 | 开始时间 | 预计完成 |
|------|--------|---------|---------|
| （例）.claude/CLAUDE.md | Claude Code | 14:30 | 14:35 |

**规则**：同一时间一行只能有一个 AI 的名字出现在某文件行上。有 Lock 在时，另一个 AI 只能审阅/规划，不能编辑。

---

## Claude Code Actions

<!-- Claude Code 的分析、建议、已修改的文件、结论 -->

| 日期 | 做了什么 | 涉及文件 |
|------|---------|---------|
|      |         |         |

---

## Codex Actions

<!-- Codex 已修改的文件、运行过的命令、测试结果 -->

| 日期 | 做了什么 | 涉及文件 |
|------|---------|---------|
|      |         |         |

---

## Open Questions

<!-- 还没决定的问题，等用户拍板 -->

- 

---

## Collaboration Rules (Quick Reference)

| Rule | Description |
|------|-------------|
| Split | Claude Code = think + analyze + write + Git；Codex = code-gen + inline-complete + single-file edit |
| Mutex | Only one AI edits files at a time |
| Declare | Announce file lock in Active Lock section before editing |
| Report | Log changes in the corresponding Actions section after editing |
| Verify | Human runs `git diff` to review changes |
| Revert | If wrong, `git checkout -- <file>` to undo |
