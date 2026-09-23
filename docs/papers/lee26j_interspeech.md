# WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models

- 论文编号�?43
- 报告人：Hanna Lee
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26j_interspeech.pdf

## 问题
基于 LLM 骨干的自回归 TTS 质量高，但全自注意力使计算与 KV cache 随序列线性甚至更糟地膨胀，长句与实时部署受限。剪层不改注意力本质；线性注意力/Mamba 需从头训且常掉质量；投机解码仍扛不�?cache 增长。作者假设：条件前缀（文本、参考音、系�?情感标签）提供全局语义与身份，生成声学 token 只需局部时序一致性，不必全序列注意力�?

## 方法
**WAND**（Windowed Attention and Knowledge Distillation）把预训�?AR-TTS 改成常数复杂度，不改主干结构�?
1. **全局 + 滑窗注意�?*：条�?token 全程可见；已生成声学 token 只看最近窗�?\(W\)，KV cache = 固定全局�?+ 滚动窗口 �?相对总长 \(T\) �?\(O(1)\)�?
2. **知识蒸馏**：学生用滑窗，教师全注意力；损失 \(L=L_{\mathrm{CE}}+\lambda L_{\mathrm{KL}}\)（Skew KL）�?
3. **课程缩窗**：余弦调度把窗口�?\(W_{\mathrm{start}}\) 收到目标 \(W\)，并对窗�?logits 用温�?\(\tau(t)\) �?mask，由软到硬�?

�?CosyVoice 2-0.5B（\(W=32\)）、IndexTTS 1.5（\(W=32\)）、SparkTTS-0.5B（\(W=64\)�?0 Hz 码率更高）上，仅�?LibriTTS train-clean-100 �?**53.8 小时**、单 epoch、单 A100 MIG 20GB 微调�?

## 实验与结�?
Seed-TTS-eval test-en / test-zh；效率按生成 10 秒音频计�?
- **质量**（test-en）：相对原模�?UTMOS/NMOS/SSIM 几乎持平或略升；WER 不升反降（如 CosyVoice 1.94�?.72，IndexTTS 0.98�?.91）�?
- **效率**：KV cache 最高降 **66.2%**（IndexTTS 38.44�?3.01 MB）；GFLOPs 降约 35�?7%，速度�?1.51�?.89×；每步延迟近常数，而全注意力随长度上升�?
- **跨语**：仅英数微调，test-zh CER 退化约 �?.1% 绝对（主系统）�?
- 注意力统计：前缀�?48�?5% 注意力质量；decode �?57�?3% 落在最�?\(W\)；前缀+局部共�?85�?1%。消融：CE+KL 与课程缩窗均优于直接硬窗或单损失�?

## 结论
WAND �?AR-TTS 的内存与每步算力从随长度增长变为近常数，在三套异构骨干上质量损失可忽略，并用少量数据实现跨语保持；作者认为这为「硬件不绑死的长时连续合成」铺路。边界是窗口 \(W\) 需随码�?注意力分布调（如 SparkTTS �?64），且仍依赖教师全注意力蒸馏�?

## 点评
抓的�?AR-TTS 里「注意力 sink + 语音局部相干」这一结构性冗余，用适配而非换骨干换取常�?KV。强在跨架构复现与极低数据量；脆弱处是极端超长或强跨句韵律依赖时局部窗可能不够，以及蒸馏仍需跑教师前向，适配阶段有额外成本�?
