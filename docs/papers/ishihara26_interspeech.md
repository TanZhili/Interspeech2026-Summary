# Sub-band Cepstral Analysis of Speaker-Specific Information: A Case Study of Japanese Word /saN/

- 论文编号：303
- 报告人：Shunichi Ishihara
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/ishihara26_interspeech.pdf

## 问题
说话人区分信息在频谱上分布不均；既往子带研究多看连续语流或依赖滤波组，难灵活定位。辅音（擦音/鼻音）上说话人敏感子带位置与强度仍不清楚，法医声纹比对需要可解释的频谱粒度。

## 方法
对全日警科研所 306 名成年男性日语 /saN/（两会话各两遍）下采样到 16 kHz，提 14 维线性频率 CC，经线性变换得 band-limited cepstral coefficients（BLCC），在 0–8 kHz 用 0.6 kHz 宽、0.2 kHz 步进共 38 个子带。用多元核密度估计似然比并 logistic 校准，六折交叉验证，以 \(C_{\mathrm{llr}}\)（及分解）与 EER 评估。实验 1 逐子带；实验 2 融合 2–4 个子带并与全带 LFCC 对照。

## 实验与结果
全带：/a/ \(C_{\mathrm{llr}}\)=0.388 最好，/N/ 0.435，/s/ 0.681 最弱。子带均 \(C_{\mathrm{llr}}\)<1，但 7–8 kHz 普遍偏弱。敏感区大致：/s/ 约 1–2 kHz（另有 ~4、6.5 kHz 局部）；/a/ 最强约 5–6 kHz，另有 ~1.1、2.5 kHz（近 F2/F3）；/N/ 主要在 <4 kHz，尤其 ~0.5–1 kHz。融合四个优选子带可接近全带性能。

## 结论
说话人信息频谱分布不均且随音段变化；/a/、/N/ 强于 /s/；敏感子带并不总与发音/声学直觉一一对应。局限：仅男性、音段少；未来拟扩人群与 Mel/LP 等分析。BLCC 便于在案件中聚焦相关子带并解释结果。

## 点评
把“哪段频谱在说话人比对里值钱”做成可扫的 \(C_{\mathrm{llr}}\) 曲线，对法庭科学可读性比黑盒嵌入更友好。/s/ 在 1–2 kHz 的强线索与高能区直觉不完全一致，提示共现元音或语言因素——作者也谨慎未过度因果化。方法省去重分析信号，适合法医场景里反复试子带组合。
