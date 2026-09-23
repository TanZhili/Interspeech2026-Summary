# Towards Event-Robust Acoustic Scene Classification

- 论文编号：2350
- 报告人：Bohan Hu
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/cai26d_interspeech.pdf

## 问题

真实声学场景中前景事件会随时空、季节变化（event shift），而现有 ASC 数据集多为相对干净、事件构成稳定的录音，难以评估模型对未知前景事件的鲁棒性。跨城、跨设备、时变等基准也未专门覆盖这一因素。

## 方法

提出 Event-Shifted Acoustic Scene（ESAS）基准：以 CochlScene 为背景、FSD50K 为事件池，用 BEATs 检测背景中已有事件并过滤，再以 GPT-4 做场景–事件语义分组，将候选事件分为 Known / Unknown；训练与验证仅含背景与 Known 混合，Unknown 仅出现在测试集。混合协议：10 s、44.1 kHz、每段 1–10 个事件类、时间位置随机、时间拉伸 [0.8,1.15]、音高移位 [-3,3]、场景–事件 SNR ∈ [-15,+15] dB。评估按 background-only / known-event / unknown-event 三档准确率，以分离“混合本身”与“分布外事件”两类失效。

## 实验与结果

ESAS 约 211 h、13 场景类、76,081 段；测试集三类样本约 1:1:1。基线含 TF-SepNet、BC-ResNet、GRU-CNN、CP-Mobile、BEATs、PaSST。背景准确率约 78–84%；引入 Known 事件后明显下降（如 TF-SepNet 降约 14.7%）；Unknown 条件下轻量 CNN 可降最多约 22 个百分点，预训练 Transformer 仍降约 7–9 点。事件数增至 10 时轻量模型可跌至 50% 以下，BEATs/PaSST 仍约 68–70%。低 SNR 下 TF-SepNet/BC-ResNet 可至 37.42%/43.21%，Transformer 约 67%。

## 结论

作者认为现有 ASC 对未知前景事件与密集多声部干扰脆弱，轻量 CNN 尤甚；ESAS 旨在推动面向 event-robust ASC 的研究，尤其是能应对不可预测噪声的轻量结构。

## 点评

贡献主要在问题定义与可控合成基准，而非新分类器：用 Known/Unknown 拆分把“声学混合难”和“事件分布外”分开测，比单一整体准确率更有诊断价值。合成依赖 LLM 语义过滤与固定混合协议，真实场景中事件–场景耦合与录音条件更复杂，外推时需谨慎；预训练大模型相对更稳，也提示轻量部署路线仍缺针对性防御机制。
