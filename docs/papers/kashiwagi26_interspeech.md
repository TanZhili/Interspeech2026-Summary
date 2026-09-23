# Speaker-Aware Hypothesis Clustering and Merging for Target-Speaker-free and Target-Speaker Multi-Talker ASR

- 论文编号：1604
- 报告人：Yosuke Kashiwagi
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kashiwagi26_interspeech.pdf

## 问题
HCM 只在转写空间聚类假设，多说话人说相同/极相似内容时编辑距离失效；目标说话人设定下离散 speaker token（k-means）又难忠实利用 enrollment。

## 方法
保持 HCM 解码与离散 token 训练不变；对每条假设用对齐片段经 TitaNet 提 embedding，AHC 距离改为 \(D_{joint}=\bar{D}_{text}+\alpha D_{spk}\)（评测 L2 / cosine / 逆 PLDA）。目标说话人场景：enrollment embedding 与各簇质心比距离选簇，替代离散 token 提示。解码 top-N=20，簇内 ROVER 合并。

## 实验与结果
LibriMix 上与 text-only HCM 接近；VCTK identical-content：2spk WER 68.3→36.6（L2，相对降 46.4%），3spk 88.3→57.2。\(\alpha\approx0.005\) 时标准条件稳定、同文条件收益最大，过大伤识别。目标说话人：clean 2spk 18.7→14.4（约 23% 相对降），noisy 2spk 28.5→25.2；3spk noisy 双方均 >120%，差异有限。

## 结论
在假设空间联合转写–说话人距离，统一改进无 enrollment 与有 enrollment 的多说话人 ASR；同文条件下收益最大，标准 LibriMix 保持竞争力。

## 点评
改动集中在聚类一步，工程侵入小，却精准打中 HCM 的文本坍缩点。\(\alpha\) 敏感、三说话人噪声下任务本身过难；多假设解码与聚类的算力开销作者亦承认仍是部署瓶颈。
