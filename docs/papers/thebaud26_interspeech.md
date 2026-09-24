# Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation

- 论文编号：2670
- 报告人：Yuzhe Wang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thebaud26_interspeech.pdf

## 问题
现成 speech-aware LLM 是否编码可用于 ASV 的说话人身份；若不足，能否用轻量增强补上而不牺牲自然语言接口。

## 方法
提出模型无关评测：API 模型用提示置信分，开源模型用 Yes/No token 似然比。在 VoxCeleb1 测多种现成 LLM。进而将冻结 ECAPA-TDNN 嵌入经投影注入 TinyLLaMA 1.1B / Ministral 3.3B，配合 LoRA，使模型在自然语言格式下做验证。

## 实验与结果
现成模型 ASV 弱（EER 常 >20%），但性别等粗属性准确率可达约 92–98%，说明抓的是粗粒度副语言而非细粒度身份。注入 ECAPA + LoRA 后接近专用 ECAPA 余弦基线；仅训连接器、冻结 LLM 时 Vox1-O 升至 5.48% EER，表明需适配骨干以解读说话人表示。

## 结论
隐式预训练不足以支撑可靠 ASV；显式注入强说话人嵌入 + 参数高效适配是可行路径，但训练与推理成本远高于专用系统。

## 点评
与“纯提示做 SV”路线形成对照：评测协议清晰，增强方案务实。API 置信分粗糙、解析失败率高限制公平对比；成本问题仍是落地主障碍。
