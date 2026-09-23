# Preserving the Iranian Turkic Language: Community-Driven ASR Datasets and Benchmarking for South Azerbaijani

- 论文编号：1516
- 报告人：Jalil Nourmohammadi Khiarak
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/farsi26_interspeech.pdf

## 问题
南阿塞拜疆语（South Azerbaijani, AZB）使用阿拉伯文正字法，母语者逾 1500 万，却几乎没有公开标注语音数据；与北阿塞拜疆语（拉丁文）听感相近但正字法迥异，预训练 ASR 与标准化基准均缺失，严重制约低资源 ASR。

## 方法
构建三套社区驱动数据：（1）Community：从阿拉伯文书籍切句并规范化（数字/符号展开、去标点、统一 Unicode 等），14 名母语者（7F/7M）手机朗读，约 1.3 万句、超 25 小时；（2）External：由北阿塞拜疆语音（BHOSAI 伪标签库与 VoxLingua107）经 Whisper-large-v3 伪标后，由出版方语言专家转写/校对为阿拉伯文南阿塞拜疆正字法，约 25 万句、447.64 小时量级；（3）AZB ASR GoldSet：独立社区采集的更具挑战评测集，约 3021 句、17.49 小时。基准模型含 MMS-1B（唯一预训练含 AZB）及 Whisper Tiny/Base/Small 及其波斯/阿语/土耳其语/北阿塞拜疆语微调后再在 Community 上微调等共八套设定。

## 实验与结果
正文报告：全量数据训练整体更好；语言特定微调对极低资源设定关键；跨语微调有时优于仅在 Community 上微调的 Whisper-Small。Community 微调的 MMS 在 GoldSet 上最好，但在 External 上仍有限；MMS 的 CER 低于 Whisper，作者归因于非自回归与无显式自回归 LM。错误分析指出阿拉伯文音位/正字歧义、极短句不稳与数字转写是主因。抽取文本在 GoldSet 提示设计描述处截断，完整数值表与更多实验细节未见。

## 结论
作者发布首批公开南阿塞拜疆语大规模 ASR 数据、八模型基准与错误分析，并视社区采集—微调—系统评测流程为其他低资源语的可复用蓝图。边界是 External 声学仍来自北变体、正字法靠人工转写对齐。

## 点评
做法抓住“同族语有数据、目标语缺阿拉伯文对齐标注”这一脚本鸿沟，用伪标+专家转写扩规模、再用社区金标与 GoldSet 压测。比单纯爬取更稳；脆弱点是声学–正字法错配、书读风格与 GoldSet 自发风格差距，以及全文截断导致无法核对具体 WER/CER 数字。
