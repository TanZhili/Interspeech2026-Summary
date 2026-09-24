# On the Role of the Tongue Region in Ultrasound-to-Acoustic Mapping

- 论文编号：1071
- 报告人：Ibrahim Ibrahimov
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ibrahimov26_interspeech.pdf

## 问题
超声到声学映射常默认舌面是主要声学信息源，但帧内还有周围组织、阴影与伪影；标准 2D-CNN 是否真在用舌区特征尚未被严格检验。

## 方法
在 UltraSuite-TaL80 四名说话人上，帧到 80 维 mel 的说话人专用网络。自动舌区提取：ROI 掩膜 + 自适应高斯阈值 + 连通域，并以 IoU/质心位移做时序稳定。输入操纵：把舌区像素换成同帧背景采样（无舌轮廓）。再提出双编码器 + 交叉注意力门控，显式注入舌掩膜。基线为 13×13 核 2D-CNN；HiFi-GAN 合成后评 MCD/PESQ/MOSnet；Grad-CAM 可视化关注区。

## 实验与结果
去掉舌区后 MSE 略升但四说话人均无统计显著（p>0.05）。双编码器相对基线在 MSE 与感知指标上亦无一致显著增益（个别说话人基线更好）。Grad-CAM：基线激活散落在组织/阴影，提议模型稳定集中在舌区。整体合成质量仍远低于 vocoded original。

## 结论
在帧级 2D-CNN 设定下，预测并不 critically 依赖显式舌区像素，网络可能依赖更广图像统计；交叉注意力虽不抬客观分，但使表征更解剖可解释。未来需在时序模型中再检验舌动态的作用。

## 点评
用“挖掉舌区也不掉分”的操纵实验挑战领域默认假设，负结果本身有价值。局限在帧独立映射——协同发音与舌轨迹本该是时间结构；点评中应记住：可解释性改进 ≠ 当前指标提升。
