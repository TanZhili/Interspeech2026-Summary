# Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction

- 论文编号：706
- 报告人：Doyeop Kwak
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kwak26_interspeech.pdf

## 问题
常规 AV-TSE 深度融合音视频并重学分离，但野外 AV 数据噪声大，可能压低相对纯音频分离骨干已达的保真度；视觉更适合解决置换歧义而非再练分离。

## 方法
Plug-and-Steer：冻结预训练音频分离骨干（Conv-TasNet、DPRNN、TF-GridNet、MossFormer2），仅用轻量视觉模块预测 Latent Steering Matrix（C×C 线性变换），在分离块潜特征上把目标说话人锚到指定通道。对比后验选择与残差微调。

## 实验与结果
末块插入 LSM 保真率最高（如 TF-GridNet 99.91%）。LRS2-2mix：LSM 保持接近原 AO 的 DNSMOS/NISQA，而全量残差微调常抬 SI-SDRi 但伤感知分。可训参数约 1.5–2.0M，远小于全微调。

## 结论
分离与选择解耦后，可用极少参数把强 AO 骨干变成 AV-TSE，并保住声学先验与感知质量。

## 点评
“视觉只负责选人”视角清晰，规避 noisy AV 监督拖垮工作室级分离质量。表中 SI-SDRi 有时低于残差微调，但感知指标更稳，取舍合理；依赖骨干本身已解耦说话人通道。
