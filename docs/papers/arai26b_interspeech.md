# Programmable Speech Synthesis without Computers

- 论文编号：3578
- 报告人：Takayuki Arai
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/arai26b_interspeech.pdf

## 问题
机械声道模型（VTM-UT 系列）可用滑块改变构型，但固定凸轮只对应单一短语；不用电脑/执行器时如何“可编程”地合成多短语动态语音。

## 方法
在 VTM-UT30-D6/D9（六块自下插入的构音滑块，D9 含鼻腔支路）上，用线性凸轮与旋转凸轮两种机构抬升滑块。可编程化：底板/基轴插入可互换异形板片（直角三角形/矩形/梯形等，或对应的斜坡/环扇），拼出任意凸轮轮廓；板片可拆装以换短语。目标高度以主声道高度 20 mm 为上限。

## 实验与结果
用两类凸轮合成同一英语短语 “I love you”；给出归一化时间上的六凸轮位移轨迹与频谱图，两侧共振峰轨迹大体相似。

## 结论
无需计算机即可用可编程机械凸轮驱动声道模型合成短语；线性与旋转方案输出相近。若有 Articulatory Phonology 轨迹，可扩展到任意短语；未来需更系统的轨迹设计。

## 点评
演示向工作，强调物理可解释的动态声道控制与“可插拔编程”。科学贡献在机构可复用性，而非语音质量评测；单短语、无听感/可懂度指标，与数字合成路线互补但规模扩展依赖手工轨迹设计。
