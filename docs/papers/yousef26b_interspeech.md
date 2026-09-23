# The Interspeech 2026 NeckVibe Challenge: Voice Disorder Detection via Real-World Monitoring of Neck-Surface Vibration

- 论文编号：3049
- 报告人：Ahmed Yousef
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yousef26b_interspeech.pdf

## 问题
诊所短时评估难以反映日常用嗓；麦克风 ambulatory 记录易受环境干扰。需用颈表加速度计（ACC）大规模监测，推动超越简单线性分类与全日汇总特征的 VH（嗓音过度功能）检测。

## 方法
发布 NeckVibe Challenge 数据：582 人（PVH/NPVH 与匹配对照）一周日常监测，约 46,400 小时；智能手机采颈表 ACC（11,025 Hz），帧级 50 ms 提取 14 维可解释嗓音特征（SPL、CPP、H1–H2、spectral tilt、L/H、IBIF 气流相关量等）及发声/歌唱/暂停掩码。任务1：PVH vs 其余；任务2：NPVH vs 其余。80%/20% 按受试者分层划分，主指标 AUC。基线约 PVH AUC 0.82、NPVH 0.78。

## 实验与结果
6 队完成提交。Task1 全队超基线，最佳 AUC 0.93（SR），其次 0.92（DD）。Task2 更难，4 队超基线，最佳 AUC 0.86（SM、VA）。顶尖方法共性：日内时间窗或 Δ/ΔΔ 动态特征、特征比、XGBoost/CatBoost/逻辑回归、语音–歌唱上下文分离、以及 MIL/CNN 等时序建模。讨论后半抽取略有截断。

## 结论
挑战表明捕捉日内变异与关系型特征可提升 ambulatory VH 检测；NPVH 分离更难且队间差异大。结果有助于理解真实用嗓与 VH 病理的关系，并推动个性化嗓音管理。

## 点评
作为数据挑战组织文，贡献在大规模 ACC 特征发布与双任务设定。参赛结果清楚指向“不要只做全日均值”——时间结构与特征交互更关键；同时 Task 定义（vs 全部非目标类）与既往文献（vs 匹配对照）不完全等同，跨文数字对比需谨慎。
