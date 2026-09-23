# Exploiting Neural Audio Codec Latents for Adversarial Audio Attacks

- 论文编号：3055
- 报告人：Ajita Rattani
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/bhattacharya26b_interspeech.pdf

## 问题

音频分类与说话人验证易受对抗攻击，但波形域迭代优化（PGD、C&W）延迟高，难实时；现有单次生成攻击常在波形空间、有可感伪影或架构沉重。需要在可感知质量与超低延迟间兼顾的生成式攻击，以评估实时威胁。

## 方法

在 DAC 连续潜空间（量化前）训练条件生成器：冻结编解码，生成器输出残差扰动并解码成对抗波形，经可微 STFT/Mel 预处理接入冻结受害模型。损失含任务对抗项、边界/几何 margin 与潜空间 L2；支持分类 CE 与 ASV 余弦嵌入目标；EMA 稳定推理。在 Speech Commands、声学场景、UrbanSound8K、LibriSpeech ASV 上对比 FGSM/PGD/C&W/FAPG/CGAN。

## 实验与结果

Speech Commands：无目标 ASR 96.58%、目标 77.65%，单样本约 6.7 ms，快于迭代与多数生成基线。UrbanSound8K：无目标/目标 ASR 约 99.11%/97.17%，约 3.9 ms。其他任务亦报告高成功率与数量级延迟优势（摘要称目标 ASR 最高约 99%、相对生成基线延迟可降约 24×）。白盒设定下跨 CNN/Transformer 受害模型有效。

## 结论

神经编解码连续潜空间可实现单次前向、低延迟、高成功率的生成式对抗音频，暴露实时流式系统风险；作者释放代码以支持安全评估。威胁模型为白盒可微管线。

## 点评

把攻击优化搬到压缩流形，同时追求隐身与实时性，对语音生物识别与命令识别的威胁评估有警示意义。作为学术安全研究总结其主张与实验结论；防御需关注编解码潜空间与前端可微链路。黑盒迁移与物理播放鲁棒性仍是开放问题。
