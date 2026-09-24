# Unified Audio-Visual Modeling to Recognize Which Face Spoke When and What in Scenarios with On- and Off-Screen Participants

- 论文编号：1592
- 报告人：Naoki Makishima
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/makishima26b_interspeech.pdf

## 问题
多说话人音视频说话人归属识别（AVSASR）需同时回答谁在何时说了什么；既有序列化方法假设说话人始终可见，而真实场景常有遮挡或画外说话人，强制关联会致错。

## 方法
在 [12] 的 Transformer 编解码序列化建模上扩展：目标序列含起止时间 token、文本与视频 token；新增 `[None]` 表示画外/不可见说话人，避免强制绑到某一脸轨。语音与多路嘴部视频分别编码，拼接后加片段嵌入再解码。在 LRS3 上仿真 2–3 人重叠混合，训练覆盖各类 on/off-screen 组合（I=3）。

## 实验与结果
指标 WER、VWER（谁说了什么）、VTER（谁在何时说）。全可见时 Proposed 与专用 AVSASR 接近（如 2 人 WER/VWER/VTER：25.4/27.9/3.6 vs 25.8/28.8/3.2）。含画外时 Proposed 明显更好：2 人 VWER/VTER 30.4/3.5，优于 AVSR+唇动检测（34.8/6.4），而旧 AVSASR 因错绑严重退化（括号内参考值更差）。画外+多人时 WER–VWER 差距拉大，音视频同步仍难。

## 结论
`[None]` token 使统一模型在含画外说话人时优于强制可见假设与分离流水线，全可见时几乎不损失。

## 点评
改动小但对准真实会议/隐私场景的关键假设漏洞。证据基于仿真混合与 5 fps 嘴部裁剪；作者也承认画外时靠音视频同步仍难，VWER 差距增大是主要边界。
