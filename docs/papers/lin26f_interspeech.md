# Improving Streaming Speaker Diarization for LLM Based Multi-talker Speech Understanding

- 论文编号：1403
- 报告人：Ruizhi Li
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26f_interspeech.pdf

## 问题
智能眼镜多通道场景中，LLM 多为单通道输入；外部分离+简单 RMS 阈值说话人标注在噪声下不稳，且阵列几何因设备而异，难以一模型通吃。

## 方法
两阶段流式框架：NL-CMV 波束形成得几何无关方向表示；源分离输出 reference/self/other，多任务加分类头；第二阶段用 F0+RMS 上的 GBDT（或 SVM）标 Self/Other/Non-speech，再选提示驱动冻结 Gemma-3n 做归属 ASR/翻译。用 Conformer 替换 GRU，参数约 20M→5.5M；多设备共享下游、设备专用波束系数。

## 实验与结果
分离用仿真 Aria 类 5 麦数据训练；分类器用 1000 条真实多通道会话。IT/FR/ES–EN 真实评估：2-Stage MT 在多数指标最优（如 ES-EN Self/Other WER 7.77/9.05，SAER 0.21/0.45）；2-Stage Conf. 接近且更轻。翻译 Other BLEU（IT-EN）升至 57.04。多设备模型对 Device-A 降 WER，对 Device-B 接近专用模型。GBDT 各类 F1 更均衡（Self 91.4、Other 85.9、Non-speech 79.6）。

## 结论
分离+轻量统计分类优于单阶段与阈值式标注；Conformer 与多几何波束形成支持更高效、跨设备的流式归属理解。

## 点评
把空间处理从 LLM 解耦，适合眼镜部署；第二阶段依赖人工时间戳与 F0/RMS，极端噪声或多人旁听者可能仍难。仿真训分离、真实评下游的域差需留意。
