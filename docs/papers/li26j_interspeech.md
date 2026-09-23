# Towards Paradigm-General Suicide Risk Detection via Speech LLM

- 论文编号：666
- 报告人：Wen Wu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/li26j_interspeech.pdf

## 问题
青少年自杀风险语音检测常依赖单一诱发范式（流利、朗读、问答等），需为每范式单独建模；简单混合多范式联合训练又难稳定增益。

## 方法
以 Qwen2.5-Omni-7B 为骨干，提出 Mixture of DoRA Experts（MoDE）：路由器对多个 DoRA 专家加权，配合负载均衡 KL 与温度缩放；在 1223 名中国青少年、10 种 SEP、MINI-KID 标注上做二分类。对比 Whisper、分范式微调与联合微调。

## 实验与结果
联合微调下 speech LLM 多数范式优于 Whisper；MoDE 平均准确率 0.656，相对分范式 0.628 约 +4.5% relative。消融去掉温度或负载均衡均下降（无负载均衡会塌到单专家）。专家数先升后降；人工指定范式–专家先验反而不如自动路由。正文报告可泛化到未见范式并改善置信校准。

## 结论
轻量 MoDE 可将多诱发范式统一进单一 speech LLM，并优于分范式与朴素联合训练。

## 点评
抓住“范式互补但分布异构”用 MoE 式适配，比硬混数据更合理。医疗场景准确率仍中等，外推依赖受控采集与文化语境；未见范式泛化与校准细节需结合原文图表谨慎解读。
