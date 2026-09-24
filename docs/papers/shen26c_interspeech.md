# Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends

- 论文编号：1972
- 报告人：Xingyu Shen
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/shen26c_interspeech.pdf

## 问题
SE 作 ASR 前端时常引入伪影伤识别；BSRNN 类 band-split 前端依赖时序/跨带 RNN，块内串行、并行效率差，且 Observation-Adding（OA）系数常需开发集手调。

## 方法
并行 Time–Band Mixer（PTBM）：子带嵌入后堆叠 \(L\) 块，每块并行做 (1) Temporal ConvMixer——门控膨胀深度卷积做带内时间混合；(2) Cross-Band Attention——每帧对 \(K\) 子带自注意力；门控融合 + 残差。重建为 mask-plus-residual \(\hat S=M\odot X+R\)。Learned OA（LOA）：用能量比与对数幅度差统计量经小 MLP 预测 \(\omega\)，\(s_{LOA}=\omega x+(1-\omega)\hat s\)；先训 SE（MR-STFT+SI-SNR），再冻 SE、用网格搜索 oracle \(\omega^*\) 回归训 LOA。V4 子带划分（\(K=23\)），默认 \(L=12\)。

## 实验与结果
DNS Challenge 与 CHiME-4、冻结 Whisper Tiny/Medium/Large：相对 BSRNN 与 Zhao 等轻量 band-split，WER 全面更低，前端仅 0.96 M / 0.58 GMAC/s。消融：去 TCM 或 CBA 均升 WER；无 OA 差于固定 OA，LOA 最好且免开发集调 \(\omega\)；\(L=12\) 性价比优于 6/9，相对 15 增益收益有限。

## 结论
并行时–带混合可替代块内 RNN 做高效 ASR 前端，LOA 自适应混合观测与增强以抑制伪影，在合成与真实噪声上稳定降 WER。

## 点评
目标对准“下游 ASR 而非听感”，LOA 把人工 OA 自动化很实用。LOA 为 utterance 级、非全流式；训练仍无 ASR 梯度，极端失配时可能不如适配器式前端。
