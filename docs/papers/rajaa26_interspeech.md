# DualTurn: Learning Turn-Taking from Dual-Channel Generative Speech Pretraining

- 论文编号：2424
- 报告人：Shangeth Rajaa
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rajaa26_interspeech.pdf

## 问题
生产级 ASR–LLM–TTS 流水线有工具调用与推理能力，但轮次切换仍依赖静音超时，延迟高且易打断；语音到语音（S2S）模型能隐式学到轮次动态，却难把能力迁移到模块化流水线。现有端点/VAP 多为单通道或把现象坍缩成二值语音活动，无法区分 backchannel、打断与真正 turn end。

## 方法
DualTurn 用冻结 Mimi codec 编码双通道 24 kHz 音频（连续 512 维嵌入，12.5 Hz），经通道 MLP 拼接后接入 Qwen2.5-0.5B。Stage-1 在约 453 h 对话音频上做双通道下一帧生成式预训练（深度预测器随后丢弃）；Stage-2 在每通道挂 6 个分类头，自监督从 VAD 对齐得到 EOT、HOLD、BOT、BC、VAD、FVAD 标签（4 s 前瞻），稀疏信号用 focal loss。信号可用启发式或多项式 logistic regression 映射为五类 agent action（ST/CL/SL/CT/BC）。推理步长 240 ms，CPU 约 78 ms。

## 实验与结果
预训练数据含 otoSpeech（289 h）与 Switchboard（220 h，138 session 测试集留出）。Switchboard 上 DualTurn（LoRA）agent action wF1 0.633，高于 VAP（LR-6）的 0.389；BC F1 0.349 vs VAP 的 0.000。词级 turn 预测 AUC 平均 0.930（启发式）/0.963（LR），高于 3.1B 音文模型的 0.880。相对 VAP 提前约 220 ms 预判 turn 边界，中位相对 turn end −360 ms vs −140 ms。消融表明 Stage-1 预训练是 BC 能力主因；连续 Mimi 优于离散码本；Stage-2 保留生成损失或加入 ASR 目标会伤稀疏信号。

## 结论
双通道生成式预训练 + 显式 turn-taking 信号微调，可在无人工标注下缩小静音端点与 S2S 级轮次动态的差距，并支持 CPU 实时运行；作者指出当前约 453 h 仅为英语双人对话，多语/多方扩展是自然下一步。

## 点评
把 S2S 式“预测对方下一帧”当作表征学习，再接到可解释的 agent action，路径清晰，也解释了为何无预训练时 0.5B LLM 几乎不比 8M LSTM 强。BC 召回提升大但精度仍低（0.282），作者也提醒不宜单独作触发；4 s 标签定义与生产策略如何对齐仍需实测。
