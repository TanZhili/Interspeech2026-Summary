# HRTF-guided Binaural Target Speaker Extraction with Real-World Validation

- 论文编号：807
- 报告人：Yoav Ellinson
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ellinson26_interspeech.pdf

## 问题
双耳 TSE 若仅用 DOA 或 enrollment，常破坏 ILD/ITD，造成视听位置不一致；基于个体 HRTF 的条件化若只针对单听者又难泛化。需要跨听者、以 HRTF 为显式空间先验、并做去混响的双耳提取。

## 方法
目标为提取直达路径 BRIR 调制的双耳目标语（M=0），以直达 HRTF hhrtf(θ,ϕ) 为线索。骨干为 NBSS：对混合物与 HRTF 分编码后在潜空间逐元素相乘调制，再经 P=8 个 NBC2 块，线性解码复谱。损失为双通道平均 SI-SDR + STFT MAE，末段仅 SI-SDR 微调。训练用 WSJ0 + SofaMyRoom 仿真 BRIR（T60∈[0.2,0.8] s，SIR∈[−5,5] dB），789 个实测 HRTF（ARI、SONICOM 等）训练/验证，7 个未见受试测；对比同骨干的 DOA-BDE。

## 实验与结果
仿真 2000 样本：Proposed SI-SDRi 15.770、PESQ 3.03、ΔITD 0.044 ms、ΔILD 0.349 dB，全面优于 DOA-BDE（13.881 / 2.74 / 0.982 / 0.479）。HATS 真实录音（T60=0.37 s，角距 20°–90°）：平均 NISQA Proposed 3.22 vs DOA-BDE 3.14，角距越大分数越高；即便 HRTF 库角分辨率导致最近邻失配仍保持优势。

## 结论
在多样实测 HRTF 上训练、推理用目标方向 HRTF 条件化，可跨听者保持双耳线索并提升感知质量；真实 HATS 验证有效，角量化误差下仍稳健。

## 点评
核心是把“方向线索”从 DOA 标量升级为完整双耳滤波形状，使提取与空间重建耦合，天然利于 ITD/ILD。代价是依赖可用 HRTF 库分辨率与目标方位已知；对近距离或与库几何不符的场景，最近邻条件可能成瓶颈。
