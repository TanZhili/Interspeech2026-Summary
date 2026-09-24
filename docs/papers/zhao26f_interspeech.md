# SA-HRTF: A Sound-Assisted Approach to Personalized HRTF Modeling

- 论文编号：1995
- 报告人：Qingyin Zhao
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26f_interspeech.pdf

## 问题
个性 HRTF 测量耗时；稀疏方向下仅靠解剖映射或检索增强（如 RANF）受限于小规模数据库与相似个体难找；纯信号法又常需额外设备且采集质量不稳。目标是在少量已测方向下更准地估计未见主体的 HRTF 幅度。

## 方法
SA-HRTF 双分支：主分支 CR-RANF 用 ITD 检索 K 个相似主体，将该方向参考 HRTF 幅度经 Conv1d 编码，与 ITD+方向经 RFF/FC/Conv 得到的辅助特征在条件残差模块中用 FiLM 仿射融合，再经 FC+LoRA 与转置卷积解码得初始估计；辅分支 SI-HRTF 对双耳波形 FFT 幅度经四层 Conv1d–ReLU–BN（第 2/3 层后加 SENet）与 AvgPool+MLP 得到补充估计；融合模块对两路拼接结果学频率相关权重 α，按元素加权后再经 Conv 精炼。三相均用 log-spectral distortion（LSD）作损失；相位用最小相位近似，本文只建模幅度。

## 实验与结果
公共数据 SONICOM（200 人，793 方向，48 kHz）训 CR-RANF；自定义双耳声由语音/白噪/音乐与 HRTF 频域相乘并加扩散场噪声（SNR 5/10 dB）训 SI-HRTF。划分 160/19/20，测点 q∈{3,5,7,9}。LSD：SA-HRTF 在 q=3/5/7/9 为 3.76/3.82/3.49/3.42，优于 nearest、ITD/LSD 选择、NIIRF、RANF、CR-RANF。声源类型中白噪最好（如 q=3 时 3.02），音乐次之，语音较差（缺高频，融合时主要保留低频并由 CR-RANF 补其余）。方位 ±5°、仰角 ±10° 偏差下 LSD 仍相对稳定。

## 结论
在稀疏测量下，用检索个体 + ITD/方向条件的 CR-RANF 与双耳声信号的 SI-HRTF，经频率自适应融合，可提升个性 HRTF 幅度估计精度与稳健性；实验显示优于若干已有方法，验证声辅助线索有效。

## 点评
贡献在于把“数据库先验检索”和“日常双耳声里的个体滤波线索”做成可学权重的频域互补，而不是只加更多测量点。白噪/音乐优于语音，说明辅分支高度依赖宽频谱激励；自定义合成双耳+固定 SNR、以及依赖 SONICOM 检索库规模，是落地到真实耳机/任意声场时的主要边界。
