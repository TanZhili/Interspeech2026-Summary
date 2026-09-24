# Band-Limited Cepstral Analysis of Speaker Sensitivity in Forensic Voice Comparison

- 论文编号：1028
- 报告人：Shunichi Ishihara
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ishihara26b_interspeech.pdf

## 问题
说话人鉴别信息在频谱上分布不均；需在连续语流中定位敏感子带并量化其贡献，以增强法医声纹比对的可解释性。

## 方法
对 AusEng 500+ 中 162 名成年男性约 30 s 访谈语流提 14 维全带 LFCC，再用 BLCC 线性变换扫描 0–8 kHz：0.6/1.2 kHz 宽、0.2/0.4 kHz 步进。GMM–UBM（256 分量）+ 逻辑回归校准做 LR 比对；六折轮换 test/background/calibration。实验 1 单子带 C_llr；实验 2 融合最多四个 0.6 kHz 子带的 LR。

## 实验与结果
全带 LFCC：C_llr≈0.136。各子带 C_llr<1，均含有用信息；近 8 kHz（约 >7 kHz）最弱。0.6 kHz 配置下 0–0.6 kHz 最强（C_llr≈0.583），4–6 kHz 亦强；1–3.5 kHz 相对偏弱。融合分散、互补的强子带可显著低于全带基线；相邻最高频弱子带融合最差。

## 结论
BLCC 可灵活剖析子带说话人敏感度；男声澳英连续语流中低端与 4–6 kHz 信息最强，最高频最弱。未来需跨语言、女性与不同时长验证。

## 点评
相对重分析原信号的滤波子带法，BLCC 从全带 CC 线性投影更高效可控。16 kHz 采样服务科学扫描，与典型手机物证带宽不完全一致，外推实务系统需谨慎。融合结果说明不同频区编码不同说话人线索，而非简单冗余。
