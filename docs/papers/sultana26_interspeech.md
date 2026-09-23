# A Fine-Grained Acoustically-Aware Pre-training Encoder for Speech Quality Assessment

- 论文编号：1607
- 报告人：Donald S. Williamson
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/sultana26_interspeech.pdf

## 问题

主流 SSL 表征常追求对背景声学不变，并偏重长程上下文/说话人信息，而语音质量评估高度依赖噪声、混响等非语音细粒度线索；大模型也难部署在资源受限设备。作者希望用更小编码器显式嵌入声学细节以服务 MOS 预测。

## 方法

提出 FASQA 预训练：mel 谱经卷积后，用 Local Spectral-Temporal Encoding（LSpTE）与 Frame-wise Spectral Relationship Aggregator（FSpRA）做细粒度谱—时建模。多 worker 联合训练：波形/LPS/MFCC/韵律回归，LIM/GIM/SPC 等分类，并扩展噪声类型、SNR、谱能量区，以及新增 DRR 与窄带/宽带失真分类。下游冻结编码器、训 MOS 回归头；在 NISQA、TMHINT、COSINE 等上与 Dasheng、wav2vec2、HuBERT、PASE 及带声学 worker 的变体对比。

## 实验与结果

约 15M 参数的 FASQA Large 在 NISQA 上 MSE 0.281、LCC 0.859、SRCC 0.845，优于更大 Base SSL；TMHINT/COSINE 亦具竞争力。声学 worker 使 clean/noisy/reverb 聚类更清晰；去掉带宽与 DRR worker 会降低部分相关。小数据预训练仍有效，适合参数敏感场景。

## 结论

结合细粒度谱时编码器与噪声/混响感知 worker，可用远小于主流 SSL 的模型达到可比甚至更好的 MOS 预测，关键是显式保留质量相关声学线索而非追求声学不变。

## 点评

对准“质量评估需要的表征 ≠ ASR/说话人 SSL 默认目标”这一错位，用 Video-Panda 式细粒度模块 + 声学 worker 补洞。轻量是实战卖点。脆弱点是预训练数据规模相对较小、下游仍依赖冻结+小头，跨域极端失配时未必稳赢大规模 SSL。
