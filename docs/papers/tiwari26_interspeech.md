# "Say That Again": Visualizing Paralinguistic Cues with Prosody-Aware Diffusion

- 论文编号：2102
- 报告人：Shyamji Tiwari
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/tiwari26_interspeech.pdf

## 问题

文生图忽略副语言：同一句“Are you serious?”因音高、语速、情感语调不同，听者脑中画面不同，但现有音频条件生成常把语音当作单一向量，不分离韵律与环境声/说话人/词汇。作者希望把与情感相关的韵律特征显式抽取出并注入扩散生成。

## 方法

NovaDiffusion 三件套：(1) ProsodyCLIP：在 ESResNeXt 通用音频嵌入上拼接 F0/能量/语速/MFCC 等韵律支路，两阶段 InfoNCE（AudioSet 再 ProsoBench）并加情感辅助 CE；(2) 约 280M 蒸馏 U-Net（BK-SDM + 多尺度融合）；(3) 仿 IP-Adapter 的解耦交叉注意，把韵律嵌入与文本嵌入分开注入（默认权重 α=0.6）。数据管线 ProsoBench：汇合 RAVDESS、IEMOCAP、MSP-Podcast 共约 168K 带标注情感语音，韵律-MLP 校验剔除约 12%，再 CLIP 检索 + 人工核验配图，说话人独立 80/10/10 划分。推理可用 OLSS 少步采样。

## 实验与结果

RAVDESS（8 类，机会 12.5%）上 ECA 71.3%，相对 SonicDiffusion 48.2% 高 23.1pp（同数据重训 SonicDiff.† 仅 52.6%）。ProsoBench 上 ECA 68.5%。IEMOCAP 未见说话人：63.4% vs 41.7%。消融：去掉韵律支路 ECA 跌至 57.2%；仅 hp 仍有 58.9%；去掉 L_CE 为 62.6%。人工评测 Emotion Match 3.82 vs 2.94（p<0.001）。作者强调 ECA 依赖人脸表情分类，不覆盖无脸场景级情感；配图来自 CLIP 检索，学的是文化刻板视觉相关而非物理共现。

## 结论

显式韵律增强 + 解耦适配器可让扩散图更跟随语音情感相关韵律；范围限于与类别情感相关的韵律，完整韵律控制仍开放。局限包括通用音频支路仍含词汇信息、ECA 脸偏、ProsoBench 的 CLIP 配对偏见等。

## 点评

把“音频条件生成”拆成韵律抽取—视听对齐—解耦注入，问题抓得准：同一文本不同说话语气应对应不同画面。用独立 AffectNet 分类器算 ECA、并报告同数据重训基线，有助于说明增益来自韵律而非数据域。脆弱点是评测与训练都高度绑定类别情感与面孔刻板图像，ECA 上限受分类器准确率约束，对场景叙事与细粒度韵律（非情感）外推有限。
