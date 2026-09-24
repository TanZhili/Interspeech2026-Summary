# Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems

- 论文编号：2749
- 报告人：Matthew Hayden
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hayden26_interspeech.pdf

## 问题
零样本 TTS 常靠说话人相似度（SSM）宣称接近真人，但 SSM 可能掩盖口音问题。作者在 CosyVoice2 指令控情时观察到口音被意外改变，称之为 accent–emotion entanglement，需系统刻画并改进评测。

## 方法
以 CosyVoice2（指令“Make this sound x”+情绪参考）与 MaskGCT（仅情绪参考）为案例，在 MEAD 的 happy/angry/neutral 上合成。主观：口音 SMOS（30 名多国英语 L1）。客观：GenAID 口音嵌入 UMAP、到质心余弦距离、口音分布熵。多说话人扩展客观分析。

## 实验与结果
CosyVoice2 口音 SMOS 跨条件约 1.17–4.13、方差大；MaskGCT 多在约 3.4–4.3 且更稳。UMAP 显示 CosyVoice2 扩散到印巴/英爱/东亚非裔等区域，MaskGCT 紧靠北美参考。各说话人–情绪下 CosyVoice2 到质心距离均更大。两系统原报告 SSM 接近，但口音行为迥异。

## 结论
情感条件可诱发口音幻觉，标准 SSM 不足；应常规加入口音主观与针对性客观指标。作者推测根因可能在指令微调数据标注/分布，但因训练数据未公开无法确认。

## 点评
用“SSM 相近却口音分裂”的对照有力说明评测盲区，且点出情感–口音纠缠的刻板印象风险。案例限于两模型与有限说话人/句子；对 CosyVoice2 成因仍是推断。贡献主要在问题定义与评测范式，而非修复方法。
