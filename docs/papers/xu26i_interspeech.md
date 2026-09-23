# A barrier or a booster? Familiarity effects on Mandarin emotion prosody recognition using AI-powered voice cloning

- 论文编号：1038
- 报告人：Feng Xu
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26i_interspeech.pdf

## 问题
情绪韵律识别同时依赖声学线索与说话人身份。AI 克隆可复制熟悉音色，但情绪韵律仍有非自然细节；不清楚熟悉度会补偿合成缺陷，还是因“熟悉身份 + 人工来源”触发 uncanny valley、加重认知负荷。

## 方法
17 名普通话成人。陌生条件：播音专业女性录 14 句中性六字句的喜/怒/惧/悲，作为人类基线与 EPVC 源；熟悉条件：熟悉者只录中性句作目标音色，不做人类情绪基线。基于 F0 条件 SVC（seed-vc），用 \(F_t=c\cdot(F_s-\bar F_s)+\bar F_t\) 做可控唤醒迁移，专家筛选。被试内判断情绪类别；同步 Biopac 采集 HRV（mean HR、RMSSD、LF/HF）。GLMM/LMM；来源分析限陌生声音，熟悉度分析限 AI 声音。

## 实验与结果
人类相对 AI：Source 与 Emotion×Source 显著；除恐惧外，喜/悲/怒准确率与 RT 均显著优于 AI。HRV 各指标无显著来源效应，也无法用逻辑回归区分来源。AI 内熟悉度：Familiarity 与 Emotion×Familiarity 显著；高兴在熟悉音色上准确率更高；恐惧 RT 则陌生显著快于熟悉。HRV 对熟悉度同样无显著区分。全文结论段抽取截断，讨论已给出主要解释。

## 结论
人类情绪韵律识别整体优于当前 AI 克隆；熟悉度对 AI 情绪加工呈情绪特异：积极情绪可作自上而下补偿，恐惧等消极高唤醒可能引发更长的批判性评估。HRV 未反映自主神经层面的系统差；合成情绪解码受社会认知门控。

## 点评
把“音色克隆成功”与“情绪意图传递”拆开，并用熟悉度测试补偿 vs uncanny valley，问题设置清楚。恐惧例外与熟悉恐惧变慢是有信息量的边界发现。弱在熟悉者无人类情绪基线、HRV 全程不敏感，认知负荷主要靠 RT 推断；结论段文本截断，细节以讨论为准。
