# Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis

- 论文编号：1015
- 报告人：Zuda Yu
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yu26b_interspeech.pdf

## 问题
流匹配语音生成面临两大瓶颈：语义 token 残留声学线索导致**音色泄漏**；ODE 路径弯曲与 CFG 双前向带来**推理延迟**。VQ 等瓶颈易伤可懂度；仅拉直轨迹或仅内化 CFG 往往顾此失彼。

## 方法
统一引导框架，两支柱：
1. **Data-guidance (DG)**：双阶段异构扰动——先用预训练 VC/TTS 对源语义 token 做跨说话人合成，再对中间波形做随机 pitch/energy 变形，得到声学不可靠但语言内容不变的条件 \(\tilde{c}\)，迫使模型从 token 取内容、从目标声学 prompt 取音色。
2. **Enhanced Model-guidance (MG)**：同一 batch 内先做内禀引导蒸馏，把 CFG 感知速度场写入网络（单前向即可对齐条件）；再用更新后的模型在线 ODE 仿真并做轨迹拉直，消除 CFG 开销并减少 NFE。

骨干：约 330M 纯 DiT（20 层，AdaLN 注入说话人），启发自 CosyVoice2；先在 Emilia 50k 小时匹配条件预训练，再在 60k 小时混合语料（含 30k 小时扰动对）上做统一优化。

## 实验与结果
VC（LibriTTS/Seed-TTS）：Unified（3 NFE）RTF 0.024，相对 10-step Base（RTF 0.078）约 **3.25×** 加速；Non-Parallel LibriTTS SIM 0.850，优于 Base 0.793，且超过 GT Parallel SIM 0.799。仅 DG 的 SIM 最高但无加速；仅 Enhanced MG 加速但 SIM 有损。TTS：同 CosyVoice2 LLM 后端下，Unified SIM（LibriTTS 0.888 / Seed-TTS 0.806）高于 Base，WER 略升但仍可比。

## 结论
数据侧异构扰动切断声学捷径，模型侧蒸馏+在线拉直去掉 CFG 并缩短轨迹，可在 VC/TTS 上同时提升零样本说话人相似与推理效率，并可作为现有 TTS 的高效声学 detokenizer。

## 点评
把「防泄漏」和「加速」放进同一训练环，比单独做 rectify 或单独做 CFG 蒸馏更完整。强在 3-step 无 CFG 仍保住甚至抬高零样本 SIM；脆弱点在依赖外部生成系统做交叉合成、在线 ODE 训练成本高（文中约 90h），以及强拉直可能轻微伤 WER。
