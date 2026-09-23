# Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics

- 论文编号：2912
- 报告人：Naohiro Tawara
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tawara26_interspeech.pdf

## 问题
LLM 系 CASR 在单说话人基准上表现好，但在重叠、远场、说话人数变化下相对模块化流水线的稳健性不清；cpWER/tcpWER 对语义影响与文本规范化过于敏感，且难分离重叠区错误。

## 方法
系统对比：单通道 DiCoW、多通道 NTT CHiME-8 DASR (S)、任务型 LLM（VibeVoice、Voxtral MTv2）、通用多模态 Gemini 3.0 Flash；数据为 MX6、NSF1、DiPCo。提出 tcpSemER（在 tcpWER 对齐上用 MiniLM 句向量相似度替代 Levenshtein），并将 tcpWER/cpWER 按重叠/非重叠区分解（贡献与区域归一化）。多通道 LLM/DiCoW 用逐通道识别 + MOVER 融合。

## 实验与结果
两说话人 MX6：VibeVoice/DiCoW 可竞争；复杂场景模块化明显更强（如 NSF1 tcpWER：NTT 15.0 vs DiCoW 24.6 vs VibeVoice 36.6；DiPCo 上 Voxtral 失败、Gemini 很差）。SemER 有时显示 LLM 更多是表层差异。重叠区贡献占 NSF1 总错误约 90%；VibeVoice 重叠删除多。MOVER 缩小差距（MX6 上甚至优于挑战最优 tcpWER 10.9）。说话人数↑时错误↑，NTT 计数最准。

## 结论
重叠处理仍是 CASR 主瓶颈；任务型 LLM 在两说话人上可竞争且 tcpSemER 相对友好，但随说话人数与声学难度急剧退化；通用 LLM 受说话人/时间归因拖累；原生多通道 LLM 值得探索。

## 点评
把“谁说了什么何时”拆成语义与重叠两个评价轴，比单纯报 WER 更能解释 LLM 流畅输出的假象。tcpSemER 仍继承 tcpWER 对齐，且与人类语义判断尚未验证；评测更偏诊断框架而非新识别模型。
