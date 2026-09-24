# Activation Steering for Accent Adaptation in Large Audio Language Models

- 论文编号：2166
- 报告人：Ting Dang
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26h_interspeech.pdf

## 问题
口音是 ASR 误差主因之一；主流适应靠微调，却不清楚口音信息编码在哪一层、能否在激活空间直接控制。大音频语言模型全参/启发式 PEFT 成本高且可能纠缠语义。

## 方法
把口音视为隐表示中可解释子空间：用文本匹配的标准–口音对，在各编码器层估 mean-shift 方向，注入后测与口音对齐程度，得到层敏感度剖面。推理时在选定层对隐状态加归一化转向向量 α·d̂（前向 hook，不改权重）。在 VCTK（多母语口音）与 L2-ARCTIC（印地/阿语/西语）上，说话人与转写与抽取集严格隔离。

## 实验与结果
敏感度：早期层弱、中层（约 15–19）可控、过晚层不稳；层 31 注入常大幅升 WER。中层转向：母语口音平衡子集上 ΔWER 最高约 30%，非母语约 5%；α 增大峰值更高但深层更易塌缩。相对 PEFT：小样本时转向有竞争力，大数据微调仍更强（正文比较）。八口音一致降 WER。

## 结论
口音信息集中在中层编码器；无参激活转向可在推理期降低多口音 WER，为可解释、可扩展的口音适应提供路径。

## 点评
把 LLM steering 迁到语音编码器，并用层扫 + α 扫给出可操作窗口，解释性与实用性兼具。依赖配对同文标准–口音语料估方向；非母语增益较小、强 α 易塌，部署需按口音校准层与强度。
