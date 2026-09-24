# GigaChat Audio: Time-aware Large Audio Language Model

- 论文编号：2343
- 报告人：Aleksandr Kutsakov
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kutsakov26_interspeech.pdf

## 问题
长录音上的 audio LLM 时间定位不可靠：时间戳不可解析、过粗或无依据；标准音频 token 流不显式承载时间，短训难外推到长音频。

## 方法
在 10B-A1.8B MoE 文本底座上接 encoder→subsampler→projector（160 ms 帧），在连续音频 token 间周期性插入 inter-timing（默认每 60 s，hh:mm:ss 或专用 timing token）。任务含 temporal grounding、按区间片段描述、带时间戳摘要。合成数据：YODAS2 英语音频经 WhisperX 对齐，切片 ~10 min 用 GPT-OSS-120B 生成并用全局 verifier 校验，按录音级划分 train/eval。

## 实验与结果
去 inter-timing 后长音频 TGr mIoU 53.8→14.2；每 7 s 锚点可到 65.2。时长混合训练对 0–120 min 外推优于单时长。专用 timing token 需更高 TG 数据占比才逼近明文时间戳。AMI 上 MAE 3.50 s（vs Qwen3-Omni 290.5）。发布权重与 10k+ 小时时序数据集。

## 结论
周期性时间锚点与多时长混合对长录音时间感知至关重要；稀疏到每分钟仍可插值到秒级中位误差。开源模型与数据以推动后续工作。

## 点评
把“何时发生”做成可验证的 interval 指标，并用级联合成缓解长音频标注成本。锚点频率与 token 开销的权衡清楚；摘要/描述依赖 LLM judge，且合成管线质量决定上限。会话主题为 SLU，但工作实质是长音频时序 QA。
