# Speech Entrainment in Multi-Party Conversations with a Digital Agent

- 论文编号：2851
- 报告人：Nicholas Mehlman
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/mehlman26_interspeech.pdf

## 问题
既有 entrainment 多研究人人二元对话；多人组与数字代理同场时，人类彼此及对人–机之间在局部/全局时间尺度上如何对齐仍不清楚，儿童–成人群体差异亦未知。

## 方法
采集成人组（30 场）与家庭组（10 场，儿童 8–14 岁）与 WoZ 数字代理（外星角色提问）的多人会话。用手工特征（幅度、PESTO 音高、VoxProfile 情绪）与 Whisper/Mimi/情绪嵌入测参与者–参与者(P2P)与参与者–代理(P2A)相似度。混合效应回归比较同轮 vs 跨轮（局部）及前 5 轮 vs 后 5 轮（全局）。

## 实验与结果
成人 P2P 局部 entrainment 几乎覆盖幅度、音高、情绪与嵌入；家庭 P2P/C2G 主要在情绪与嵌入，幅度/音高不显著。两组均无显著局部 P2A。全局：成人仅弱音高/Mimi 效应；家庭无显著 P2P 全局；儿童–代理在 Whisper 嵌入上全局收敛，但幅度发散（儿童音量随会话上升）。

## 结论
多人场景中人类间局部对齐强，对人–机局部对齐弱；与代理的收敛有限且依赖年龄/时间尺度，儿童更可能在语义表征上逐渐贴近代理。

## 点评
把数字代理嵌入真实多人场并分成人/家庭队列，填补人–机多党 entrainment 空白。局限是家庭场次少、代理固定访谈角色、会话前已有共处时间可能压低全局效应，嵌入可解释性有限。
