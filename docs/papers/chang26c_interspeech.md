# USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding

- 论文编号：1296
- 报告人：Heng-Jui Chang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26c_interspeech.pdf

## 问题
SSL 编码器多偏单域；USAD/SPEAR 等跨域蒸馏覆盖与评测仍有限，且监督式编码器往往更适合作音频 LLM 前端。需要同时吸收 SSL 与监督教师、覆盖 speech/audio/music，并在可控算力下扩到约 10 亿参数。

## 方法
USAD 2.0：域感知蒸馏——输入域与教师匹配时提高权重（ω=10，软权重仍保留错配教师）；教师为 WavLM、ATST-Frame、MuQ，数据含多语语音约 116K h、通用音 21K h、音乐 13K h。USAD 2.0+：以 SSL 学生初始化，二阶段蒸馏 Whisper Large-v3 与 Audio Flamingo 3 编码器末层。扩容：帧率 50→25 Hz，并用 depth up-scaling 将 XLarge（32 层）扩到 XXLarge+（48 层，约 1036M）。

## 实验与结果
HEAR 上 USAD 2.0+ XLarge+/XXLarge+ Avg 84.4，优于先前单编码器 SOTA；MARBLE 上无监督 Large 75.8，有监督变体保持竞争力；XARES-LLM Track B 上 XXLarge+ 达 0.624。消融：去域感知蒸馏 PR PER 升至 13.3；无音乐教师 NSynth Acc 从 70.3 掉到 49.1；二阶段从 SSL 初始化优于从头；depth up-scaling 优于均匀复制/新顶层。25 Hz XXLarge 推理快于 50 Hz Large，峰值显存约 2.4 GB。

## 结论
域感知三域 SSL 蒸馏 + 监督二阶段 + 高效深度扩展，得到跨域均衡且适合作 LLM 前端的通用编码器，并在学术预算内扩到 1B。

## 点评
路线是“多专家蒸馏成单前端”，域权重与音乐教师补齐先前 USAD 短板，监督二阶段对准 LLM 语义对齐。强在 HEAR/LLM 评测一致抬升；MARBLE 上有监督变体略低于部分无监督分数，说明对齐 LLM 与保留细粒度音乐表征之间仍有张力。
