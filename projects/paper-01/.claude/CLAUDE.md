\# Paper 1 项目配置



\## 项目信息

\- 标题：待定

\- 主题：待确定

\- 当前阶段：1

\- 记忆文件：../../shared/memory/paper-01-memory.md



\## 启动时自动执行

1\. 读取记忆文件

2\. 显示当前进度和待办事项

3\. 询问今天要做什么任务



\## 文件输出位置

\- 主题定义 → 01-topic/

\- 文献列表 → 02-search/

\- 筛选结果 → 03-screen/

\- 框架笔记 → 04-extract/

\- 数据提取 → 04-extract/

\- 统计分析 → 05-analysis/

\- 论文草稿 → 06-write/drafts/

\- 评审意见 → 07-review/

\- 最终版本 → 08-submit/



\## 工作结束时自动执行



每次工作结束，执行以下步骤：



1\. 更新记忆

echo "

\## $(Get-Date -Format 'yyyy-MM-dd') 更新

\- 今日完成：\[总结今天的工作]

\- 关键发现：\[重要信息]

\- 下一步：\[明天计划]

\- 进度：XX% → XX%

" >> ../../shared/memory/paper-01-memory.md



2\. 提交到 Git

cd ../..

git add .

git commit -m "Paper 1: \[今日工作总结]"

git push



3\. 提示用户

"✅ 记忆已更新并同步到 Git"

