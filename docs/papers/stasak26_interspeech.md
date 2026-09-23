# CalliOpeNLP: A Standalone Digital Health Voice Data Collection Research Tool

- 论文编号：1783
- 报告人：Brian Stasak
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stasak26_interspeech.pdf

## 问题
临床嗓音数据采集常依赖当面人工操作，易受交互偏差（Hawthorne 效应、治疗性提示不一致）、无关闲聊拉长录音、事后才质控、以及商业工具收费/数据外传等问题，缺少开源、可本地部署的自动化方案。

## 方法
发布 Python 开源工具 CalliOpeNLP：先采集人口学信息，再用 pyttsx3 合成语音 + 屏幕文字引导 18 项临床验证嗓音任务（Cape-V 短语、计数、Happy Birthday、最大发声 /a/ /s/ /z/、音高范围、Rainbow Passage、My Voice 等）。sounddevice 按任务计时录音（7–45 s，44.1 kHz），自动命名标签；Whisper tiny（可换 large）本地转写；对“朗读”任务用 Levenshtein 与 FuzzyWuzzy token-set-ratio 与金标准比对，阈值默认 0.70 时提示警告并允许重录；会话结束生成报告。表演性任务暂不自动合规评分。

## 实验与结果
正文为工具设计与流程说明，未报告大规模用户试验数值；强调 tiny 模型约 <3 s/任务、全程离线无第三方传输，并给出 GitHub 发布地址。合规阈值与最优设定称仍在进一步测试。

## 结论
作者认为自动化可统一指令与任务顺序、近实时合规反馈、减少人工切分与交互偏差，便于多站点一致建库；工具面向临床嗓音生物库，也可扩展到非医疗语音采集。表演性任务自动合规与阈值标定仍是后续工作。

## 点评
把“采集协议 + 本地 ASR 合规”做成可改参数的开源流水线，切中临床嗓音建库的实际痛点。强在离线隐私与任务级自动切分标签；弱在尚无系统可用性/合规准确率实验，且表演性任务依赖示例回放而非自动评分，ASR 在病理嗓音上误差会直接影响合规判定。
