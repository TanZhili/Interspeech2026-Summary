# SPOT-TSE: Spatial Point-Guided Target Speech Extraction

- 论文编号：3266
- 报告人：Taewon Ryu
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/ryu26c_interspeech.pdf

## 问题
可穿戴设备上的空间目标语音提取常用固定区域（距离/方位区间）条件化：边界附近标签突变敏感，且仅用距离或方位在空间重叠（同距或同方位）时歧义；区域选择也可能保留整段区间内多源而非精确点源。

## 方法
SPOT-TSE 用连续空间点查询 q=(d_q,θ_q) 条件化多通道提取。SQE：归一化距离/方位经傅里叶特征映射再投影得 z_q，经 FiLM 注入 Mamba 版 TF-GridNet（BiMamba/Mamba 替换 LSTM 以降算力）。输入为多通道 STFT 与 ILD/IPD/CDR。训练用广义高斯邻近权重构造软目标，降低边界刚性；并以 hard-negative 采样（方位近而距离远，或反过来）迫使联合使用两维线索。推理仍按查询点条件化。

## 实验与结果
7 麦智能眼镜阵列仿真（Project Aria），D1→D3 几何难度递增。D3（随机房间+麦位）上 SDR 11.05 dB、WER 0.22（混合物约 −4.64 dB / 1.05）。消融：去掉方位查询或 SQE 性能崩溃；hard-negative 主要帮方位混淆子集；软目标提升整体与边界附近表现。相对 LSTM TF-GridNet，MAC/s 从 40.19 降到 10.54（约 −74%），SDR 相当。

## 结论
点引导空间条件化配合软目标与难负采样，可在重叠/边界模糊场景提升选择性与 ASR 可用性，并降低可穿戴算力；未来需加强距离建模与真机验证。

## 点评
把“选区域”改成“选点+软监督”，直接对准区域法的边界与重叠痛点；傅里叶 SQE 与双轴 hard-negative 设计合理。目前全仿真，真机阵列标定误差与头部运动下的点查询稳定性仍待检验。
