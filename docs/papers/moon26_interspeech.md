# SLICE: Speech Enhancement via Layer-wise Injection of Conditioning Embeddings

- 论文编号：1715
- 报告人：Seokhoon Moon
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/moon26_interspeech.pdf

## 问题
真实语音常同时受加性噪声、混响与非线性失真；扩散 SE 在单退化上强，但噪声感知条件若只加在输入层，在复合退化上甚至不如无条件模型，且条件信号在深层残差块中被稀释。

## 方法
在 SGMSE+ / NCSN++ 上提出 SLICE：冻结 WavLM-Base 提特征，经投影得共享 \(h\)，再分三头（噪声 11 类 CE、\(T_{60}\) MSE、失真强度 MSE）监督；三路投影拼接后 MLP 得 \(c_{extra}\)，加到 timestep embedding，从而经全部残差块传播，无需改骨干。训练损失 \(L_{score}+\lambda\sum L_{aux}\)（\(\lambda=0.3\)），并做分支 CFG dropout。数据在 VoiceBank-DEMAND 上叠加合成混响与 soft-clip 失真。

## 实验与结果
同数据消融：layer-wise 在多退化上 ESTOI 0.80、SI-SDR 3.7、UTMOS 3.71；输入级 addition 仅 0.73 / 1.4 / 3.62，弱于无编码器（0.77 / 2.3 / 3.70）。相对仅噪声训练的 SGMSE+/NASE 等，多退化提升明显。噪声-only 上 UTMOS 最高（3.93）。野数据（VOiCES/DAPS/URGENT）上多退化训练是主因，编码器增益不如受控集显著。

## 结论
条件“怎么注入”与“有没有条件”同样关键：经 timestep 的逐层注入优于浅层输入相加，配合多任务退化表征可联合处理噪声/混响/失真。

## 点评
用受控对照把“注入深度”钉死，对条件扩散 SE 很有启发。混响仍拖累 SI-SDR；野数据上与无编码器差距缩小，说明编码器标定与域偏移仍是短板。
