# ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

- 论文编号：2698
- 报告人：Masao Someki
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/someki26_interspeech.pdf

## 问题
基础模型时代语料达百万小时、模型达十亿参，实验工作流复杂；既有工具链在多数据集组合、大规模迭代、多节点训练与 PEFT 集成上工程开销大。

## 方法
ESPnet3：模块化架构 + 配置驱动数据集组合 + 统一 Python 工作流。引入 DataOrganizer 灵活拼数据，dataset sharding 控制内存；允许轻量 stage override 写配方逻辑。默认 BaseSystem 即可跑大规模预训练，并支持接入非原生 ESPnet 模型（如 Whisper）与 HuggingFace PEFT。

## 实验与结果
OWSM-V4 base（约 320k 小时）预训练：相对 ESPnet2，每 epoch 从 95.3→74.2 分钟（约 −21.1 分钟），多节点 GPU 利用率 >80%；RAM 与数据刷新开销大幅下降（约 35.9GB→73.1MB，刷新 311.5s→13.1s）。增强经 DataOrganizer 接入后 CHiME-4 WER 略降。WhisperLv3 在 FalAR 微调可用约 46 行接入新 HF 数据集（ESPnet2 手工约 374 行）；全参/LoRA 均可。

## 结论
ESPnet3 以更低工程成本支撑大规模语音基础模型训练与定制微调，并将公开释放与 checkpoint/日志。

## 点评
贡献在基础设施而非新识别算法：把“能跑大、好扩展”做成可测指标（epoch 时间、利用率、代码行数）。对社区复现大模型实验价值高；具体任务 SOTA 非本文重点。
