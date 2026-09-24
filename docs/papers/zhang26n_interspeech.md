# SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios

- 论文编号：1023
- 报告人：Eng Siong Chng
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26n_interspeech.pdf

## 问题
会议场景音量差异大时，SE 与 AGC 级联会互相拖累：AGC 在前放大噪声，AGC 在后依赖 SE 质量且易放大残噪；SE 又易过抑远场/小声。公开 AGC 数据与标准化响度评测也不足。

## 方法
SE-AGCNet：STFT 后先 SE（MP-SENet 骨干，对过抑 bin 将 SE 损失加权 \(\times10\)），目标为干净但音量不平衡；再对 RMS 归一化幅度做 AGC（Conv2D→BiLSTM→转置卷积），目标为干净且音量平衡；ISTFT 用 AGC 幅度 + SE 相位。AGC 损失对“目标静音却预测有能”再 \(\times10\)；\(L_{total}=L_{MP\text{-}SENet}+\lambda_{AGC}L_{AGC}\)（\(\lambda_{AGC}=0.9\)），先预训 SE 5 epoch 再联合。配套 SE-AGC-DataGen 从 LibriTTS 构造 LibriAGC（音量扰动 + DNS 噪声）；响度用 LUFS / St LUFS / LRA，目标约 −23 LUFS、LRA 约 3–6。

## 实验与结果
LibriAGC：SE-AGCNet PESQ 3.00，LUFS/St LUFS ≈ −23.7/−23.9，LRA 3.86，Whisper WER 6.88，优于 MP-SENet (SE)+pyagc 等。真实 MMCSG / AliMeeting-far：响度回到约 −23，MMCSG WER 13.86/30.36，AliMeeting CER 34.43，优于级联与单模型同时学 SE+AGC。

## 结论
联合优化使 SE 保小声、AGC 调响度，比级联或单网络硬学两任务更稳，并改善下游 ASR；模块可挂接其他 SE 骨干。

## 点评
把会议“远近音量”与增强绑在同一端到端目标里，并引入 ITU/EBU 响度指标，评测比只看 PESQ 更贴场景。依赖自建仿真与固定 −23 LUFS；多通道只取第一路，复杂声学仍待扩展。
