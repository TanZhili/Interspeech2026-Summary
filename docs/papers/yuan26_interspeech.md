# STSR: High-Fidelity Speech Super-Resolution via Spectral-Transient Context Modeling

- 论文编号：27
- 报告人：Jiajun Yuan
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yuan26_interspeech.pdf

## 问题
语音超分需恢复至 48 kHz 的谐波与瞬态细节；级联或特征不匹配方案易糊高频；需端到端 MDCT 域高保真重建。

## 方法
STSR：有符号 MDCT 域端到端框架，建模频谱–瞬态上下文以对齐谐波；复合目标含频域对抗等。训练时随机截止频率 r∈[4,32] kHz 再上采样至 48 kHz。约 66.2M 参数，无额外声码器。

## 实验与结果
VCTK：4/8/16/24→48 kHz 平均 LSD 0.79，ViSQOL 随带宽升高；主观 MOS 4.20±0.06。HiFi-TTS 跨库平均 LSD 1.05，优于 NVSR、mdct 等对比。消融显示频域对抗与瞬态建模有贡献。

## 结论
统一 MDCT 超分在客观与主观上超过文中所列 SOTA，跨数据集仍稳。

## 点评
有符号 MDCT 避免幅相拆分带来的级联失配，设计干净。参数量不小；对比系统是否同训练预算需留意。瞬态/谐波可视化支撑“更锐谐波”主张。
