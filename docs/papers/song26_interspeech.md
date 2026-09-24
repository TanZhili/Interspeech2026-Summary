# CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion

- 论文编号：48
- 报告人：FeiBao Song
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/song26_interspeech.pdf

## 问题
非平行 VC 存在训测失配：训练时常从同说话人取样内容与音色，推理却需任意组合；FreeVC 等未充分覆盖内容–音色交叉，泛化不足。

## 方法
CFLOW-VC 基于 FreeVC/VITS：WavLM 先验 + 说话人编码器后验 + Mel-Style 风格编码器；用 flow 可逆性做 cycle training（CTS）：源先验经逆 flow 注入目标音色再循环回源，配合 StarGAN 式对抗、双向 KL、循环 KL 与 HiFiGAN 重建损失；先验侧加 GRL 说话人分类促解耦。WavAugment 加噪声/混响增强。两阶段：backbone 预训练 500k → 冻结后验与解码器后 CTS 200k。

## 实验与结果
VCTK 训练（109 说话人，16 kHz）。Clean/Noise/Accent 三测集相对 DiffVC、Diff-HierVC、StarGANv2-VC、FreeVC：Clean 上 SIM 73.5%、UTMOS 3.948；Noise 上 WER 12.09%、SIM 73.89%、UTMOS 3.911，显著优于基线；Accent 亦最优。主观 MOS 在三集均为最高（Clean 4.39）。消融：去 CTS 大幅变差；去风格编码器伤 SIM/UTMOS；去增强伤噪声鲁棒性。

## 结论
将归一化流与 StarGAN 式循环一致性结合，可在非平行设定下缓解训测失配，提升音色相似度、表现力与噪声/口音鲁棒性。

## 点评
核心是把 CTS 做在高斯先验/后验上而非 mel，降低对抗训练难度，思路清晰。仍依赖预训练说话人编码器与 VCTK 规模；去 CTS 单独加风格编码器反而劣于 FreeVC，说明循环损失才是解耦关键，组件耦合较强。
