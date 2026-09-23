# Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models

- 论文编号：1111
- 报告人：Chun-Yi Kuan
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kuan26_interspeech.pdf

## 问题
TTA 在 FAD/CLAP 等全局指标上已强，但多事件与时间顺序指令常失败；现有偏好数据多靠 CLAP/启发式/人工，缺可扩展的指令级正确性监督。

## 方法
用 ALLM 作细粒度裁判，判定目标事件是否存在与时间序是否正确；经基准与人工校验后，将满足/不满足样本构造成偏好对做 DPO。提出 S3Bench：叙事多事件指令约 1200 例（2–4 事件，LLM 生成叙述，仅评测不用训练）。

## 实验与结果
ALLM 与人在存在/时序判断上高一致（协议约 89.8%/93.5%）。DPO 后在既有基准与 S3Bench 上事件完整度、时序与联合指令遵循准确率提升，同时保持音频质量竞争力。

## 结论
作者认为 ALLM 细粒度反馈可规模化改进 TTA 指令遵循，并提供叙事评测基准 S3Bench。

## 点评
把理解侧 ALLM 接到生成侧训练信号，打通“能听懂指令→能生成符合指令”。依赖 ALLM 偏置；S3Bench 叙述由 LLM 生成，可能与裁判同族。相对 Baton 人工标注更可扩展，相对 CLAP 更对准事件/时序。
