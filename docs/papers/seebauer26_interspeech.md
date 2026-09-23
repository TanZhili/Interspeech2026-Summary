# Application context in speech synthesis evaluation: A problem and a solution

- 论文编号：747
- 报告人：Fritz Seebauer
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/seebauer26_interspeech.pdf

## 问题
合成语音评测常在“中性”孤立句上做 MOS，假定质量可模块化、与应用无关；生态效度不足，且跨场景比较可能混淆系统差异。

## 方法
80 名德语母语者，4 任务×4 系统拉丁方：学习对话、寻物导航（WoZ）、自由对话、听短故事；系统为 Tacotron2+WaveNet、VITS、Auralis/XTTS-V2、Orpheus。实体公寓与其 Unreal 数字孪生并行。评总体质量、听努力度、自然度等与短版 UEQ。贝叶斯层级模型检验任务、系统及交互；ROPE 判定实际等价。

## 实验与结果
导航任务在总体质量、听努力度、自然度等上显著更高；任务×系统交互在听努力度、语调、音质、愉悦度等上超出 ±10 ROPE。部分维度（UEQ、外向性等）更接近等价。VR 与实体条件统计可比（RQ3）。

## 结论
应用语境显著且系统依赖地改变合成语音评分；未指定场景的系统对比可能混淆。数字孪生可作为更生态评测的可行路径。

## 点评
交叉设计直接冲击“中性评测可迁移”假设，对工业选型很实用。VR 等价是降低成本的亮点。任务顺序固定、系统含未知商用数据，因果解释需谨慎。
