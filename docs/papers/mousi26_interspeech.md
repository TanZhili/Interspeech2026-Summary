# Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models

- 论文编号：1980
- 报告人：Nadir Durrani
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/mousi26_interspeech.pdf

## 问题
语音优先多模态助手应对语义等价的文本与口语查询给出一致的视觉 grounding 判断；现有评测多看单通道准确率，难揭示文–语与跨语决策不一致。

## 方法
构建 10150 个文化 grounding 对比三元组（18 MENA 国图像：1 条支持陈述 Q+、2 条似真不支持 Q−），经需图过滤与人工校验；英–阿翻译 + XTTS 男/女声合成，并加噪声/混响。定义对比不稳定性 CI：在至少答对一条的三元组中，未能全对的条件比例。评 Qwen2.5-Omni 3B/7B、Qwen3-30B-Omni、Phi-4-multimodal。

## 实验与结果
口语相对文本抬高 CI，阿拉伯语更甚（如 Q2.5-3B 阿语文本 CI 0.43→口语 0.71）；英语较稳。放大模型降 CI 但不能消掉跨模态/跨语差距。SNR 降低时阿拉伯语 CI 升更陡。联合文–语输入相对纯音频降 CI，仍不及纯文本。聚合 Q+/Q− 或 F1 可能仍高而 CI 暴露碎片化失败。

## 结论
模态不是中性通道；对比不稳定性揭示准确率掩盖的文–语与跨语不一致。公开基准与 CI 度量供后续稳健性评测。

## 点评
用条件三元组指标补足独立陈述准确率，诊断视角清晰。语音为合成；图像–文化先验与翻译质量仍可能纠缠。对语音助手可靠性评测有直接参考价值。
