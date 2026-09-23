# Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties

- 论文编号：458
- 报告人：Rodrigo Nieto
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nieto26_interspeech.pdf

## 问题
ASR 方言偏差研究多聚焦英语，西语与法语等全球语言的系统差距机制不清；Common Voice 等资源多为朗读标准文本，难以暴露形态与话语标记等方言特征。

## 方法
从 Apple Podcasts 构建约 20 小时、性别平衡、按国家方言分层的评测语料（西语 5 种、法语 5 种，共 10 方言、129 说话人），人工转写保留方言正字法。评测七个模型（含 Whisper v2/v3、Otter、GPT-4o-Transcribe、Wav2Vec2、Qwen2-7B、SALMONN-7B）。对 Whisper v3：JSD word-shift 做词汇分析；用 pyannote 与 Whisper L16 说话人嵌入做方言分类与声学距离–WER 相关；LoRA 微调并分别冻结编码器/解码器定位误差源。

## 实验与结果
方言间 WER 差异显著（西语 Kruskal–Wallis H=179.24；法语 H=63.18）。西语：阿根廷/多米尼加最好，智利最差，并非人口规模单调；法语：欧洲变体整体优于加拿大与非洲。性别差距因方言而异。词汇侧见 voseo“矫正”、区域词与 pues 等话语标记失败；声学侧方言–性别分类准确率西语约 83–86%、法语约 67–77%，与 WER 相关。微调：冻结编码器接近全 LoRA，冻结解码器几乎无增益，显示偏差主要在解码器。

## 结论
西法 ASR 误差系统反映相对训练分布的语言/声学距离；公平 ASR 需建模方言语言特征。语料与诊断框架可复用于其他语言。

## 点评
把基准、JSD 错误词与解码器定位串成因果链，比单纯报 WER 更有解释力。播客语体与门控发布限制外推到全部语域；小数据 LoRA 无法消除差距，也点出仅靠轻量适应不够。
