# Speech signal analysis

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：5
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场以语音表征中的因子化与潜结构综述开场，随后聚焦对齐与音节级分析：多语种词级强制对齐、无声说话脸视觉强制对齐、语言无关音节工具包，以及时长感知软标签的监督音素切分。共同主题是把时间结构从硬边界假设推进到可学习动态规划、最优路径与不确定边界建模，并服务多语种/低资源场景。

综述对比自上而下施加结构（因子化目标、蒸馏、瓶颈/可控变量）与自下而上发现结构（探测、扰动、潜空间运算、重合成）及其在可控生成、声转换、域迁移等中的应用。实证工作则把 MMS 与无监督音素边界融合进可学习 DP，把视觉对齐写成帧—音素相容格上的单调最优路径，并用软高斯脉冲替代硬边界以刻画切分标注不确定性。

## 技术内容

### 表征结构综述与多语词对齐

**Factorization and Latent Structure in Speech Representations**（Survey Talk；Matthew Wiesner）  
综述如何在语音表征中施加与发现结构：自上而下包括因子化训练目标、模型蒸馏与显式瓶颈/可解释控制变量；自下而上包括探测、受控扰动、潜空间算术与重合成。讨论其优劣，并概述可控生成与编辑、声转换、域迁移、高效建模与多说话人分离/归因等应用。

**Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming**（论文 296；Joseph Keshet）  
对齐编码器融合 MMS 与 UnSupSeg 表示并估计长时上下文词边界概率；对齐解码器为可学习动态规划，结合段特征推断最终边界。在 TIMIT、Buckeye 迭代训练上优于 MFA 与基于 MMS 的对齐；荷兰/德/希伯来等未见语言上不低于既有方法，显示有潜力扩展到 MMS 支持的 1100+ 语种而无需再训。

### 视觉对齐、音节工具与软边界切分

**V-Align: Visual Forced Alignment via Phoneme to Video Optimal Path Traversal**（论文 560；Souvik Ghosh）  
将视觉强制对齐表述为帧—音素相容格上的最优单调路径遍历，学习软遍历后验并用动态规划恢复离散边界。两阶段训练：阶段 1 无显式边界监督已具竞争力；阶段 2 用词级监督精炼。LRS2/LRS3 上 MAE 与帧准确率达 SOTA。

**findsylls: A Language‑Agnostic Toolkit for Syllable‑Level Speech Tokenization and Embedding**（论文 820；Héctor Javier Vázquez Martínez）  
模块化语言无关工具包，统一经典音节检测与端到端音节化接口，支持切分、嵌入与多粒度评测，标准化如 Sylber、VG-HuBERT 等方法并可重组组件。在英语、西班牙语及低资源 Kono（中部曼德语）手注数据上演示可复现音节级实验。

**Duration-Aware Soft Targets for Text-Independent Supervised Phone Segmentation**（论文 2568；Raghavan Ramesh）  
用软目标替代硬边界：在硬边界两侧放置与邻段时长成比例标准差的零均值半高斯脉冲，边界两标准差内用高斯值替换硬标签。基线 BiGRU 在 TIMIT 测试 R-val 91.53%；域外与多语数据上相对硬目标有统计显著提升。

## 本场要点

- 表征结构可用自上而下施加或自下而上发现，服务可控生成与迁移。
- 可学习 DP + 多语 SSL 表示推动词级强制对齐跨语种泛化。
- 无声音频时可用视觉最优路径做音素—视频对齐。
- 音节级研究需要统一工具与评测协议，覆盖低资源语言。
- 音素切分应显式建模边界标注不确定性（时长感知软标签）。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| （Survey） | Factorization and Latent Structure in Speech Representations |
| 296 | Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming |
| 560 | V-Align: Visual Forced Alignment via Phoneme to Video Optimal Path Traversal |
| 820 | findsylls: A Language‑Agnostic Toolkit for Syllable‑Level Speech Tokenization and Embedding |
| 2568 | Duration-Aware Soft Targets for Text-Independent Supervised Phone Segmentation |
