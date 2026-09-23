# Two-Level Uncertainty Suppression for Robust Meeting Diarization

- 论文编号：1956
- 报告人：Shuhei Asaka
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/asaka26_interspeech.pdf

## 问题
真实会议日志中，快速话轮与重叠造成边界模糊，局部活动估计不稳会传至聚类，导致全局说话人分配混乱。现有 EEND/EEND-VC 与声学表征增强未显式处理边界不确定性；且实际会议常为“部分已知说话人”，多数系统只假设全未知或全注册。

## 方法
基于 DiariZen 的 EEND-VC，提出两级不确定性抑制。(1) 分割：用 OWSM-Encoder（E-Branchformer，ASR/翻译监督）的语言学上下文，经上采样后以 FiLM（γ⊙h+β）调制 WavLM 中间层；再对多层级做可学习加权求和，送入 Conformer 做说话人活动估计。注入层对 (k,l) 由层间 Pearson 相关 + Hungarian 匹配选出对齐层，避免盲目搜层。(2) 聚类：Known-Seed Guided Clustering（KSGC）在 AHC 中，将已知说话人注册嵌入按复制因子复制后与估计嵌入联合聚类，通过抬高已知种子在质心中的权重稳定分配；含已知嵌入的簇多数表决标号，其余为未知。

## 实验与结果
数据：AMI、AliMeeting、AISHELL-4；原测试集评分割；改造测试集每人取 20 s 非重叠注册模拟混合已知/未知。对比 WavLM-base+/large、OWSM 替换、输出级融合（Weighted Sum / Concat+MLP / Gating）与 FiLM。FiLM single(5,8) 在未知条件下 AMI DER 14.1、AliMeeting 13.0，相对 WavLM-large 分别降 0.4 与 1.8 点。混合条件下 KSGC 相对标准 AHC 一致提升，AliMeeting 最大约 2.62 点（WavLM-large：19.6→17.6）；复制因子 AMI/AISHELL-4 为 5、AliMeeting 为 150。区域 DER 显示边界/内部区 confusion 下降；已知说话人数增加时 DER 进一步下降。

## 结论
在分割与聚类两端分别抑制局部边界与全局分配不确定性，FiLM 与 KSGC 在多会议语料上稳定降 DER，尤其利于重叠多、话轮快的场景。未来拟把已知说话人信息也引入分割阶段；双编码器带来的算力/显存开销待压缩。

## 点评
问题定义对准 EEND-VC 误差传播链：边界不稳 → embedding 差 → 聚类混乱，并用“语言学调制声学层”与“数据级复制种子约束”分别打两头，比只换骨干或只做输出融合更贴场景。FiLM 相关选层有设计依据；KSGC 几乎不改 AHC，工程友好。脆弱处在于双编码器成本、复制因子需按语料调、混合条件测试集因删段导致 DER 绝对变差需对照解读，且不确定性本身多为观测性指标而非直接方差测量。
