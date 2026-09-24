# Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech

- 论文编号：2909
- 报告人：Chibuzor Okocha
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/okocha26_interspeech.pdf

## 问题
儿童口吃语音在声学与结构上异于成人；ALM 能否在无显式说话人分离的混说访谈中做儿童聚焦语义推理、保留临床相关不流畅，尚不清楚。

## 方法
两任务：儿童向语义摘要（保不流畅、排除成人泄漏）；儿童语音蕴含（分层难度）。指令引导聚焦儿童。评测多款 ALM，辅以 Whisper/Granite ASR + 文本 LLM 级联与 transcript-oracle；LLM 裁判 + BERTScore；零样本提示变体。

## 实验与结果
摘要：Audio Flamingo 3、Kimi 总体较好（Overall 约 3.43/3.13）；Kimi 访谈 BERTScore F1 0.478。蕴含：Qwen2.5-Omni 最佳 ACC/F1 0.681/0.683；多数模型偏预测 entailment，矛盾类弱。难度从易到难 ACC 仅小幅下降（约 0.449→0.417）。提示工程收益有限。推理随不流畅与说话人干扰加重而明显变差。

## 结论
ALM 可从口吃儿童语音抽取高层语义，但在混说与高不流畅下忠实性与推理稳健性仍不足；需锚定转写基准以分离识别与推理误差。

## 点评
把“儿童焦点 + 保留不流畅 + 防成人泄漏”写进任务定义，比一般音频摘要更贴临床。LLM 裁判与偏 entailment 偏差会抬高表观分数；无说话人分离的设定现实但把难度堆叠，失败原因（声学 vs 指令遵循）仍需更细诊断。
