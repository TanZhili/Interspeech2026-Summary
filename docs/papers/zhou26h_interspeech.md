# FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech

- 论文编号：2280
- 报告人：Zhiyong Wu
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26h_interspeech.pdf

## 问题
可控 TTS 或靠参考语音（灵活差）或靠文本描述（细粒度不足）；近年联合方法仍松耦合——参考只管音色、文本粗改全局风格，跨模态协作弱。绝对属性对也不利于相对参考做增量控制。

## 方法
FineCombo-TTS：Speech Attributes Extractor（FACodec 音色 + Mel-Style 残差风格）得统一属性嵌入 E_a；CFM Speech Variance Predictor（1D UNet）在 T5 描述与源属性条件下学参考→目标变换；TTS 骨干自回归多层声学 token + DAC。两阶段：先训骨干与属性抽取，再训 Variance Predictor。构造 FineEdit 三元组〈源语音, 控制描述, 目标〉，覆盖韵律/情感/音色配对子集。推理支持联合、仅参考或仅描述；多 CFG（文本与描述掩码训练）。

## 实验与结果
相对同数据重训的 VoxInstruct-Joint：韵律控制 MOS-I 更高、Controlled Accuracy（速度/音高）更好、Uncontrolled Variation 更低、SECS 70.20 vs 56.79。情感准确 85% vs 47%；音色控制 MOS-I 3.75，FPC/Emotion-S 更优。消融：加强描述 CFG 提情感准确；残差风格编码器改善零样本 MCD/SECS。

## 结论
统一属性空间 + CFM 方差预测 + FineEdit 相对控制数据，实现参考锚定与文本精控的协同可控合成，优于松耦合联合基线。

## 点评
关键不在硬解耦属性，而在“相对变换”数据与 CFM 条件流；用 Controlled Accuracy / Uncontrolled Variation 把“改对目标、别动其他”测清楚。基线靠改 VoxInstruct 拼接参考，对比公平性尚可。局限是配对数据大量合成/自动标注，真实用户指令分布外推未充分验证。
