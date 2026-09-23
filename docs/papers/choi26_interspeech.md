# Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR

- 论文编号：698
- 报告人：Woosuk Choi
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26_interspeech.pdf

## 问题
端侧部署 Whisper 时，INT/FP 量化格式与激活精度如何影响编码器–解码器 ASR 仍缺系统证据；LLM 上流行的 W4A16 与 NVFP4/MXFP4 是否迁移到 Whisper 不清楚。

## 方法
对 tiny.en/base.en 做 80+ 组 FakeQuant PTQ：INT8/4/3 与 FP8/FP4/NVFP4/MXFP4，扫激活精度、组大小与 SmoothQuant；LibriSpeech test-clean/other；比较面积文献中 FP vs INT 乘法器。给出 Pareto 与六条部署指南。

## 实验与结果
激活位宽主导：16→8 bit 约 +1–3% 绝对 WER；INT16 与 FP16 激活几乎无差别。NVFP4 W4A16 在 base.en 达 4.88%（距 FP32 0.07%、约 6.4× 压缩）；MXFP4 标准 PTQ 严重崩（tiny 可达 38–94%）。INT3 近不可用。Pareto：>约 36 MB 时量化 base 优于 tiny。

## 结论
保 16-bit 激活比抠权重更重要；NVFP4 是近无损 4-bit 首选；FP 激活路径因乘法器面积更小更适合 NPU。指南覆盖 20–80 MB 预算。

## 点评
工程向系统扫参，结论可直接指导格式选型。强在激活位宽与 NVFP4 vs MXFP4 的机制解释（E8M0 尺度过粗）；弱在仅 tiny/base、FakeQuant 非真机延迟，且未与 GPTQ/AWQ 权重敏感方法交叉。
