# Samsone: A Family of Open Small Audio Language Models for On-Device Inference

- 论文编号：763
- 报告人：Michal K. Grzeszczyk
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/masztalski26_interspeech.pdf

## 问题
LALM 规模大、成本高，隐私与低延迟场景需要可端侧运行的 Small Audio Language Models（SALMs，本文定义为 <1B）。现有 Pengi、Mellow 等 SALM 推理能力与真实手机部署、开源可复现实验仍不足。

## 方法
标准 ALM：Whisper-Tiny 编码器 → Mellow 式非线性 projector（两层 Linear+GeLU、残差与 LN）→ SmolLM2（135M/360M）解码。音频帧嵌入时序平均池化为每样本 50 token；可训练 SEP token 分隔多段音频与文本。尺寸优化：(1) 词汇削减（小写 ASCII、过滤稀有 token，去掉约 15042 词，降约 8.7M 参数）；(2) 深度剪枝（99M 版去掉最后 10 层，30→20 块）。变体：Samsone-99M / 134M / 356M。数据：ReasonAQA + AudioSkillsXL；对 ReasonAQA 多选题随机置换选项以纠正答案偏向；单阶段训 100 epoch（每 epoch 20 万样本），除 LM embedding 外全可训；XNNPACK/ExecuTorch 导出端侧权重。

## 实验与结果
MMAU：99M/134M/356M 平均 Test 约 58.13 / 61.33 / 62.00，均超 Mellow（53.34），134M 可与更大 LALM 竞争；MMAU-Pro 相对 Mellow 约 +34%–36%。ClothoAQA 与 entailment（CLE/ACE）上优于或持平 Mellow；AudioCaps SPICE 低于 Mellow（归因训练中 AudioCaps 占比更小），Clotho SPICE 更好。消融：换 AST、GPT-2 或线性 projector 均降 MMAU。Galaxy S25 Ultra：生成约 39–125 tok/s（356M→99M）。局限：重度 AQA 微调损害通用语言能力；以参数量代理效率、未做 GPU/NPU 硬件优化。

## 结论
开源 Samsone 系列在同尺寸 SALM 上刷新 MMAU 等表现，并给出手机实时推理与可扩展尺寸谱。未来可探索量化大模型与硬件加速。

## 点评
主线是“公开数据 + 词汇/深度剪枝 + 端侧导出”，把 SALM 从纸面精度推向可跑的 Android 应用，工程闭环完整。相对只堆更大 LLM 的路线，强调 <1B 与实机 tok/s。脆弱点在于 caption 并非全面领先、通用语言能力被 AQA 微调侵蚀，且效率叙事仍偏参数量而非精度–内存曲线。
