# QAMO: Quality-aware Multi-centroid One-class Learning For Speech Deepfake Detection

- 论文编号：1098
- 报告人：Eng Siong Chng
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/truong26_interspeech.pdf

## 问题
单中心一分类（OCL）把真实语音压到一个质心，易过度简化；真实语音质量（自然度）跨样本差异大，且 MOS 可廉价估计，却常未被显式建模。

## 方法
QAMO：用 Scoreq 预测 MOS，阈值为高低质量两级；为真实类学多个质量感知质心，并用质量分类损失拉开；推理时对多质心距离做集成打分，无需质量标签。接在 XLSR-Conformer-TCM / Nes2NetX 上；增强样本视为低质量。

## 实验与结果
XLSR-Conformer-TCM + QAMO：21DF 1.63%、ITW 5.21%、FoR 3.45%，优于 WCE、OC-Softmax 与先前质量感知系统。消融去掉质量分类或改用 max-score 推理均变差。UMAP 显示高低质量真实/伪造子空间更清晰。

## 结论
按质量多中心建模真实类，比单中心 OCL 更能保留类内变异并改善未见场景检测。

## 点评
用 MOS 代理代替说话人身份做多中心（相对 SAMO）更可部署。τ=2.5 二分与增强=低质量是粗近似，但与 MOS 分布位移一致；ITW 5.21% 是亮点数字。
