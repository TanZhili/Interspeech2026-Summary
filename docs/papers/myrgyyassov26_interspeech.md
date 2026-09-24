# Automated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and Ultrasound

- 论文编号：1664
- 报告人：Alisher Myrgyyassov
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/myrgyyassov26_interspeech.pdf

## 问题
超声常用于舌轮廓，颏舌骨肌（GH）对舌位与下颌重要，但成像与标注难、人工量厚度耗时且评定者间变异大，限制大规模语音与临床研究。

## 方法
SMMA 两组件：(1) 超声帧标准化后由 CNN 分割 GH（224×224），训练 50 epoch、Dice+Focal（0.8/0.2）、超声增广；比较 Attention UNet、UNet、UltraUNet、SwinUNet、DeepLabv3；(2) 对掩膜形态学后处理，骨架化取中轴，仅用骨架 25%–75% 分位段计算平均厚度（边界垂直距离×2），可选曲率与截面积。数据：11 名粤语者（5 男 6 女）1650 张标注图，按说话人 7:2:2；SuperSonic Aixplorer + SC6-1，30 fps，声同步。

## 实验与结果
分割：人工间 Dice 约 0.90–0.92；UltraUNet Dice 0.9037±0.0035、IoU 0.8263，选为骨干。厚度相对声学家：随机图 MAE 0.88 mm、r=0.707；高质量临床选图 MAE 0.53 mm、r=0.901。孤立元音 /a:/、/i:/、/u:/（各 6 次，共 198）：/a:/ 最厚 7.29±0.90 mm，/u:/ 6.65±0.79，/i:/ 5.95±0.84（ANOVA p=0.019；/a:/ vs /i:/ Cohen’s d>1.3）。男性在 /i:/、/u:/ 厚约 5–8%。重复 CV 5.06%。

## 结论
SMMA 可接近人工水平自动量化言语中 GH 厚度，元音模式与下颌下降激活一致；消除人工标注瓶颈，便于言语运动与吞咽/构音障碍评估。局限含 N=11、单语、单声学家真值、图像质量强影响误差。

## 点评
把“分割质量接近评定者一致性”和“骨架中段厚度”串成可复现流程，填的是 GH 语音学研究的方法空白，而非新声学特征。骨架均匀形态假设与孤立元音对齐较易；连续语流、不规则掩膜与病理样本是主要脆弱点，文中亦承认需音素对齐与质量阈值。
