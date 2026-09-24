# MSU-Bench: Towards Understanding the Conversational Multi-Speaker Scenarios

- 论文编号：3344
- 报告人：Zhaokai Sun
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/sun26j_interspeech.pdf

## 问题
LALM 把 SLU 推向端到端生成，但现有语音基准多为单说话人或孤立子任务，缺少对真实多说话人对话中“说话人中心理解”（身份绑定、关系、动机、交互）的诊断式评测。

## 方法
提出 MSU-Bench：两层 16 任务、2300 道四选一 QA。Tier1 说话人 grounding（识别/属性等），Tier2 多说话人推理（场景、结构、上下文）。数据来自电话、会议、播客、电影中英素材；Gemini 辅助质检与标注，火山 API 做 diarization/转写，人工复核。五种说话人指称：无索引（目标音频片段）、时间、转写、出场顺序、复合线索。干扰项标注错误类型（错说话人/幻觉/未知等）。零样本评测 6 个开源 + 3 个 Gemini 闭源模型。

## 实验与结果
总体准确率约 0.19（Qwen2.5-Omni）–0.77（Gemini-3-Flash）；开源最强 MiMoAudio 0.56。闭源全面领先。Time Index 普遍最难；Complex Index 常因多线索而更好。强模型错误以 wrong-speaker 为主（Gemini-3-Flash Tier2 约 0.67），弱模型更多选 unknown。人工验证：初始 QA 有效性 Tier1/2 为 95%/86%，人类与终标一致 98%/96%。

## 结论
MSU-Bench 暴露出时间定位与正确说话人归因是主要瓶颈；更强模型从“不会答”转向“答错人”。基准标注与脚本已公开。

## 点评
诊断式干扰项与指称方案让“差在哪”可读，而不只给总分。Gemini 参与造题又参与评测有偏好风险，作者用人审缓解，但仍需独立复现。选择题便于打分，开放生成场景下的说话人理解难度可能更高。
