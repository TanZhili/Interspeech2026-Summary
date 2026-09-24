# Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction

- 论文编号：919
- 报告人：Kenichi Fujita
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/fujita26_interspeech.pdf

## 问题
导演式“相对上一遍如何改”的 direction-following TTS 需要 (参考句, 指导语, 修改后句) 三元组，但大规模语料几乎没有这种相对风格配对。作者要可扩展地构造伪三元组并学习说话人保持的相对风格变换。

## 方法
用印象可控零样本 TTS 生成同脚本 pre/post 句对，经说话人一致性与语速过滤后估计 13 维印象向量差 ΔI，由 LLM 生成自然语言指导语，构成伪三元组。在固定骨干 TTS 的语音嵌入空间上训练方向条件风格精炼器（整流流匹配预测加性嵌入偏移）。另采集约 8.9 小时专业配音真实三元组。对比仅伪数据、仅真实、混合及不同说话人规模子集。

## 实验与结果
伪数据约 35 万三元组（127.6 小时）。客观：精炼不损害 UTMOS；伪数据与 Full 比仅真实录制在未见说话人上更稳地保持说话人相似。主观：Recorded AlignMOS 最高但 SMOS 较低；Pseudo-all SMOS 高而对齐略保守；Full 折中。伪数据 F0 变化幅度小于专业录音，解释了更保守的调制。

## 结论
伪三元组 alone 即可稳定做说话人保持的相对修改；与真实数据结合可提升方向对齐同时维持身份稳健。伪数据韵律变化偏小是当前局限。

## 点评
把“相对指导”从绝对风格标签中拆出来，并用印象差驱动 LLM 写导演语，数据管线可扩展。伪数据依赖印象可控 TTS 与同一印象估计器，存在分布收缩风险；客观对齐也用该估计器作代理，需主观 AlignMOS 交叉验证——作者已做，但伪–真韵律差距仍制约表现力上限。
