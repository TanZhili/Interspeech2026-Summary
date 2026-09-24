# YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech

- 论文编号：386
- 报告人：William Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26d_interspeech.pdf

## 问题
开源语音总量与专有数据差距大，且多为 16/24 kHz 单声道，难支撑全频带编解码、空间音频、立体声增强等；现有大规模集语言常严重偏英语。

## 方法
发布 YODAS v3：>1.1M 小时、147 语、48 kHz 多通道 OPUS、CC BY 3.0。按语言从维基构建关键词并搜 CC YouTube，优先新上传、去重相对 v2；保留最高质量音频、原语字幕（人工极少，约 3.7%）与非英语的英文字幕、描述与时间戳。分析语言/时长/有效带宽/有效声道；基线训 ASR 与 DAC 编解码。

## 实验与结果
22 语>10k 小时、73 语>5k；英语占比 <2%。约 92.5% 有效带宽>32 kHz，71%（约 780k 小时）为真多声道。ASR（OWSM v4 初始化）：更宽松 CTC 过滤通常更好，说明字幕可直接用。48 kHz DAC 在域内/LibriTTS 上 STOI 与说话人相似度优于低采样率及 AMUSE 等基线。

## 结论
提供首个百万小时级、真高带宽立体声且语言更均衡的开源弱标注语料，可直接支撑 ASR 与高保真编解码研究。

## 点评
采集侧按语言关键词与新视频优先，从源头缓解英语垄断；带宽/声道有效性检验比名义 48 kHz 更可信。弱标签依赖 YouTube ASR/locale，长视频与 Shorts 混杂，下游仍需任务向清洗。
