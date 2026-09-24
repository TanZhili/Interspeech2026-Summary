# DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention

- 论文编号：1627
- 报告人：Wenqiu Tang
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tang26b_interspeech.pdf

## 问题
语音角色扮演智能体（SRPA）若端到端微调，依赖角色专用数据、难泛化到未见角色，且音频–文本联合训练带来「模态对齐税」，损伤 LLM 推理与人设一致性；纯级联 LLM→TTS 又易丢情感推理，TTS 只做脱节渲染。

## 方法
**DeSRPA**：推理期干预、不更新参数的解耦框架：
1. **内部认知转向**（冻结 Qwen3-4B）：用 SAE 学稀疏控制向量，在残差流注入人格基向量、情境激活向量（Layer 15）与语言风格向量（Layer 20）；缩放系数结合 PDB 人格指标与人–LLM 协作标注。
2. **外部表达渲染**（冻结 StyleTTS 2）：从 ESD/CREMA-D 过滤高置信情绪样本，用风格减法 \(v_{\mathrm{acoustic}}^{(c)}=\mathbb{E}[S(x^{(c)})]-\mathbb{E}[S(x^{(n)})]\) 得说话人无关情绪方向；按 LLM 情绪标签与强度 \(\tau\) 做双路径融合注入风格空间并经扩散 style predictor 细化。

## 实验与结果
SpeechRole（72 英角色）与 OmniCharacter-10K（原神 10 角色）。多模态裁判均值 0.8379，开源最优、接近 GPT-4o Audio(0.8862)；EEA 0.701、SIM 0.886。消融去掉 LLM/Speech CV 分别伤人格/知识一致性与 EEA（降至 0.549）。OmniCharacter 人类评测：流畅、清晰、情感表达最高；Consistency/Immersion 逊于高度风格化的 OmniCharacter E2E（作者归因动漫夸张韵律 OOD）。

## 结论
作者认为双层推理期控制向量可在不微调下对齐「心智」与「嗓音」，提升人格/情绪一致性并缩小与专有模型自然度差距。

## 点评
路线明确反对「一切端到端」：把角色适配做成两侧冻结骨干上的向量算术，可扩展性好。风格减法解耦说话人与情绪方向，和 LLM 侧 SAE 人格向量形成对称设计。脆弱点：依赖外部过滤质量与裁判 LLM；TTFA 高于纯 E2E；对夸张 OOD 人设，固定 StyleTTS 2 风格空间仍可能不够。
