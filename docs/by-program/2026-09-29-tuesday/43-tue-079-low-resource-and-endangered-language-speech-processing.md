# Low-Resource & Endangered Language Speech Processing

- 日期：Tuesday 29 September 2026；时间：16:30-18:30；形式：Oral；Area：9；论文数：5（含 1 场特邀报告）
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场从濒危语言总览出发，讨论短形式语料引导 ASR、通用音素识别配方、发音特征零样本分类，以及谱系先验自监督。特邀报告框定现状：语音 AI 约覆盖 100 种语言，其余五千余种多为低资源且多处濒危，而识别与合成可用于保存与复兴。

后续论文回应“从何入手”：词/短短语对齐比句级监督更易获得；大规模多语音素识别需要可复现配方；离散 IPA 标签不足以保证未见语音对立；语言家族感知预训练在数据受限时提升鲁棒，但不能替代大规模预训练。趋势是把语言学结构（音系、发音特征、谱系）显式写入数据与目标。

## 技术内容

### 总览与从短形式起步的 ASR

**Low-Resource & Endangered Language Speech Processing**（特邀报告；Tatsuya Kawahara）概述低资源/濒危语言语音识别与合成的方法、数据、训练、基础模型与用例，并介绍报告人团队的阿伊努语与琉球语相关项目。摘要未给出具体数值结果。

**Bootstrapping Endangered Language ASR with Short-Form Corpora**（论文 1302；Christopher Bartley）探索词或短短语级语音—文本对作为比句级语料更易得的入口。先在英语管道量化短形式替代的影响，再为 5 种类型多样濒危语言获取短形式数据以强制对齐长语音、构建句级集，并训练 ASR；相对 OmniASR、MMS、Whisper 等，以远低算力获得更好域外表现。

### 音素识别、发音特征与谱系先验

**An Empirical Recipe for Universal Phone Recognition**（论文 1462；Shikhar Bharadwaj）提出 PhoneticXEUS，大规模多语训练，多语 PFER 17.7%、口音英语 10.6%。在统一方案下跨 100+ 语言做消融，量化 SSL 表征、数据规模与损失目标影响，并分析语系、口音与发音特征误差模式；数据与代码开放。

**Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features**（论文 2246；Ryo Magoshi）在汉语送气与日语拍鼻音零样本分类上，排除这两语的 G2P-IPA 训练 PFM 表现差；基于连续发音特征向量的分类优于离散 token，尤其稀有音。时间聚合需按对立选择：送气宜单帧，鼻音宜音段聚合。

**Genealogical Priors in Self-Supervised Learning: Improving Speech Technology for Low-Resource Languages**（论文 2886；Elizabeth Granda）用 WavLM-Large 比较随机多语子集与语族感知子集预训练。语族感知在下游优于随机选择，尽管预训练收敛相近；二者仍低于原版 WavLM-Large，说明语言学组织在数据受限时增强鲁棒，但补充而非替代大规模预训练。

## 本场要点

- 特邀报告把濒危语言语音技术定位为保存/复兴工具，并梳理可用基础模型与案例。
- 短形式语料可启动对齐与 ASR，降低对句级监督的门槛。
- PhoneticXEUS 给出可复现的通用音素识别配方与跨语误差分析。
- 连续发音特征比离散 IPA 更利于未见语音对立的零样本分类。
- 谱系感知 SSL 在受限数据下有益，但不能单靠它替代大规模预训练。

## 覆盖核对

| id | title |
|---|---|
| （特邀） | Low-Resource & Endangered Language Speech Processing |
| 1302 | Bootstrapping Endangered Language ASR with Short-Form Corpora |
| 1462 | An Empirical Recipe for Universal Phone Recognition |
| 2246 | Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features |
| 2886 | Genealogical Priors in Self-Supervised Learning: Improving Speech Technology for Low-Resource Languages |
