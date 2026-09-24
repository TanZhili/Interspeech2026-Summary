# Automatic pitch prediction from speech articulation: Where does the f0 information come from?

- 论文编号：1288
- 报告人：Beliz Ozkan
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/ozkan26_interspeech.pdf

## 问题
源–滤波理论认为 f0 与声道独立，但 SSI 文献能从舌超声/唇等预测 f0，形成理论悖论；需弄清信息来自何处、何种条件下可泛化。

## 方法
在 TaL（UTI+唇+音频）上复现/扩展：CNN+FC 编码器（唇 L、舌 T、L+T；及 MFCC 子集 M0:2/M3:12/M0:12）+ 1D CNN 解码器（1/3/7/17 帧上下文）。用读白训练、自发测试；按 Continuous Wavelet Transform + k-means 分词级突显度 P0–P2。9 说话人（TaL1 + 8 TaL80 fine-tune）。用 Grad-CAM、相关/RMSE（八度）与 LPCNet 重合成主观可接受性检验四假设。

## 实验与结果
T/L+T 优于仅 L；舌相关约 0.63–0.68（TaL1），Grad-CAM 无稳定舌骨/喉源注意→拒 H1（图像泄露声门）。时间上下文对 T/L+T 几乎无显著影响→拒 H2。自发相关从读白约 0.65–0.70 跌至约 0.38–0.39→确认 H3 过拟合。P2 词预测显著更好→确认 H4。38 人强制选择：高 P2 比例时 L+T 与 M0:12 可接受率达约 87.5%，局部韵律功能比全局轨迹更重要。

## 结论
UTI 可部分预测 f0，主要抓突显处的局部发音–f0 耦合而非可见声门；读白模型难泛化到自发。SSI 应重视真实会话数据，并侧重局部韵律功能而非复制全局 f0。

## 点评
把「能预测」拆成可证伪假设，比继续刷 RMSE 更有科学价值。H3/H4 对工程含义清楚：训练域与突显结构决定可用性；主观实验把「局部够用」落到感知。
