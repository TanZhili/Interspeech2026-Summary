# Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification

- 论文编号：1130
- 报告人：Ming-Hsiang Hu
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/hu26c_interspeech.pdf

## 问题
用户自定义关键词检出（UD-KWS）学到说话人无关表示后，无法拒绝说对关键词的冒名者；文本相关 SV（如 PK-MTL）又绑死固定关键词，破坏零样本灵活性。需同时应对未见关键词与未见说话人（双零样本），且模型需适合边缘部署。

## 方法
提出 ZP-KWS：双分支解耦——冻结的 EfficientTDNN-Small（约 0.9M）说话人编码器（VoxCeleb2 预训练 + LibriPhrase GE2E 微调，短句嵌入稳定），与音素监督音频编码器（冻结预训练嵌入 + 可训 Conv1D–BiGRU，MFA 帧级音素对齐损失 Lalign）。文本经 G2P 后与音频经自注意力 Pattern Extractor/Discriminator 得到 putt；说话人余弦经标定线性层得 pspk。推理时乘法晚融合 pfinal = putt · pspk，可无重训切换 C-KWS / TB-KWS / TO-KWS。总损失 Lutt + Lphon + Lalign。

## 实验与结果
LibriPhrase Easy/Hard、Qualcomm、Google Speech Commands；关键词与说话人均未见。TO-KWS 上相对最强基线 PK-MTL，FRR@1%FAR 相对降幅最高约 60%（如 LibriPhrase Easy：29.47% vs 72.79%）；C-KWS EER 在多数集仍最优（Easy 2.38%）。消融：去掉 GE2E 后 TO FRR@1% 从 29.47% 升至 73.42%；去掉标定层 TO EER 恶化；总参数约 1.55M。

## 结论
功能解耦的 TI-SV + 音素监督 + 乘法门控，可在零样本关键词设定下加入生物识别安全，并在固定模型上切换严格度。未来关注噪声与失配下的置信度标定。

## 点评
把“关键词分数补偿说话人分数”的加性融合改为严格 AND，切中边缘误唤醒痛点；GE2E 短句微调是 TO 模式增益的主要来源。Hard 最小对上整体 FRR 仍高，说明音素混淆时 SV 只能互补、不能替代内容判别。
