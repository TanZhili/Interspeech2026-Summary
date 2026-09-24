# Articulatory Dynamics using Physical Vocal-tract Models

- 论文编号：840
- 报告人：Takayuki Arai
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/arai26_interspeech.pdf

## 问题
声道可视化与建模对语音学、教学与病理重要，但静态物理模型难以呈现动态协同发音；可编程动态物理模型（尤其线性凸轮对应 Articulatory Phonology 手势分数）对调音动态的仿真能力尚缺系统检验。

## 方法
使用带鼻腔与 VP 耦合旋钮的 VTM-UT30-D9，以线性凸轮实现手势分数式时序控制。实验一：按 LA、TBCD、TRCD、VEL 等 tract variables 产出 [bɑb]/[bɑm]，测量语谱与不同 VP 开度下 [ɑ] 的冲激响应。实验二：对 nonsense [ɑbɹɑ] 系统改变 −LA 与 TBCD 起始间距 d（Step 0–7，每步 10 次，共 80 次），用 wav2vec 2.0（Matlab speech2text）判断是否识别为辅音簇，并做趋势与相邻步检验。

## 实验与结果
[bɑm] 在元音后段出现鼻化相关抗共振；随 VP 旋钮 0°→45°，极–零对逐步插入，F1 可被零点抵消。对 [ɑbɹɑ]，d 增大导致 [b] 与 [ɹ] 间插入类 schwa；ASR 在 Step 0–1 几乎总判为辅音簇，Step 6–7 为 0%；Cochran–Armitage 显示正确率随步数显著单调下降（χ²=42.538, p<0.001），相邻步仅 Step1→2 经 Bonferroni 校正后显著。

## 结论
动态物理模型能按 AP/TD 手势分数实现鼻化协同与时序重叠，并复现目标缺失 schwa 式插音；线性凸轮是连接手势时序与声学输出的直观实验平台。

## 点评
把抽象 gestural score 落到可听、可测的机械声道上，对教学演示与协同发音机制论证都很有说服力。实验设计以时序参数扫描为主，量化指标依赖外部 ASR 对“是否听出插音”的二值判断，对感知边界的解释需结合人耳实验进一步确认。模型块数与几何简化也限制了对真实舌形多样性的覆盖。
