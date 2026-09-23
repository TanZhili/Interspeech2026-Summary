# Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers

- 论文编号：455
- 报告人：Yunjie Zhou
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26_interspeech.pdf

## 问题

语音增强常作为实时语音服务前端，对抗样本研究较多，但后门威胁研究不足。既有音频后门多针对分类、并假设推理时可主动注入人工触发；增强模型是被动处理用户流，攻击者通常无法稳定改推理输入，故传统触发模型不现实。

## 方法

提出 CleanTrigger：把训练集中高纯度干净目标语音本身当作触发，使模型在遇到自然干净高 SNR 语音时激活恶意行为，无需推理期外加信号。Ouroboros 在黑盒数据投毒威胁模型下，按 SNR 排序毒化高 SNR 样本（默认毒化率 10%），将输入—目标改为（干净语音，恶意目标如静音），保留低 SNR 样本以维持正常去噪。在 VoiceBank-Demand、WSJ0-CHiME3 上攻击 MP-SENet、SEMamba、CMGAN、FlowSE；对比 BadNets（固定正弦触发）。指标：ASR（触发时输出近静音比例）与非触发噪声输入的 PESQ 相对变化。另测滤波/微调防御、物理录音触发与短语篡改扩展。

## 实验与结果

10% 毒化下 ASR 多近 100%，PESQ 降幅通常小于或可比 BadNets；生成式模型主任务受损往往更小。2% 毒化已可高 ASR；高 SNR 毒化优于随机/低 SNR。常见滤波难以在去后门与保质量间兼顾；有限干净数据微调后 ASR 仍可很高。物理世界 60 条干净人声触发：FlowSE ASR 100%、MP-SENet 96.7%。短语篡改（目标句经 TTS）在 CMGAN 上 ASR 84.15%、FlowSE 46.24%。

## 结论

清洁语音自指触发可使增强模型在被动场景被后门激活，成功率高、主任务损伤相对可控，并对简单过滤与微调有韧性。作者呼吁针对性防御与跨数据集验证；范围限于成对数据训练的增强模型。

## 点评

抓住增强系统“被动、无外部触发”的威胁模型缺口，把后门从分类迁移到回归前端，对供应链数据投毒风险有警示意义。高 SNR 优先毒化体现攻击—效用折中设计。作为学术安全研究，其启示是增强服务需审计训练数据与部署干净输入路径；文中结果亦显示简单微调难清后门，防御需专门设计。
