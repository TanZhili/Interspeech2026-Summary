# Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models

- 论文编号：3181
- 报告人：Nikita Kuzmin
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kuzmin26b_interspeech.pdf

## 问题
端到端全双工对话模型（SALM-Duplex、Moshi）持续把用户语音送入 LLM，隐藏状态是否泄漏说话人身份尚未被系统审计；亦缺适配流式对话的匿名方案。

## 方法
按 VPC 2024 lazy-informed 协议，用 ECAPA-TDNN 探针各层/均值池化隐藏状态，报告 EER 与 Linkability。提出两路 Stream-Voice-Anon：Anon-W2W 在波形前端匿名再送原编码器；Anon-W2F 用可匿名离散编码器替换连续前端并微调 LLM（SALM-Duplex 上演示）。分析层深与对话轮次对泄漏的影响。

## 实验与结果
无匿名：Moshi 离散 EER 6.4%、SALM 离散 11.2%、连续 28.5%。W2W：Moshi 36.9%、SALM 连续 34.6%；W2F：41.0%（相对离散基线 11.2% 超 3.5×）。Linkability 在前几轮急升；匿名后 10 轮仍相对可控。质量：sBERT 保留约 78–93%（文中相对降幅约 7–22%）；FRL <0.8 s，但 RTFx 由数十–数百倍降至约 1.6–2.5。

## 结论
全双工 LLM 隐藏状态普遍编码说话人身份；波形与特征域流式匿名可显著抬升 EER，W2F 最接近机会水平。需在质量与延迟上继续优化。

## 点评
把隐私探针从静态 SSL 推进到 always-on 对话骨干，问题设定有时效性。评估仍用朗读 VPC 数据而非自然对话；探针为下界，更强攻击者可能进一步压低 EER。
