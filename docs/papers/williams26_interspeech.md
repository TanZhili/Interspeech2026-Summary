# AI Regulation and the Technical Language of Speech Synthesis

- 论文编号：210
- 报告人：Jennifer Williams
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/williams26_interspeech.pdf

## 问题
全球 AI 监管（如欧盟 AI Act、加州、中国等）对深度伪造与合成语音施加透明度义务，但法律用语多借图像/视频的“生成 vs 篡改”，且聚焦输出标注；忽视可移植的说话人嵌入模型及其在 TTS/VC/ASR/ASV 工作流中的独立生命周期。

## 方法
概念与历史梳理：说明语音合成直至 WaveNet 后才被重新框为 AI；梳理 TTS、VC、ASV、ASR 的长期交叉。对比法律中 AI system/model/service 与语音研究中“模型=可组合模块”的差异。表列 i-vector、d/x-vector、ECAPA、WavLM、PPG、wav2vec 等嵌入的外部性、可复用性与是否编码说话人身份。图示编码器–解码器–声码器、端到端、ASR 中介 VC、codec+LLM 等流程。兼论哲学（后人类/嗓音复制）与医学（嗓音假体）政策含义。

## 实验与结果
无定量实验。核心主张：仅监管输出无法覆盖说话人嵌入的创建、存储、转移与跨任务复用；“完全合成/部分合成”二分法难以刻画扩散/流式迭代与多模块管线。说话人嵌入处生物特征隐私灰色地带（不可唯一反演却可支撑识别）。

## 结论
政策语言需与语音合成的模型与工作流技术现实对齐，否则透明度义务会漏掉身份编码组件；语音科学家应帮助修订法律用语，兼顾文化妥当与技术可执行。

## 点评
把监管缺口钉在“可移植说话人模型”而非笼统 deepfake 标签，对立法沟通很有用。强在历史脉络与嵌入/工作流对照表；弱在偏政策批评、未给出可操作的监管条文草案或合规度量。
