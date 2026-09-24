# AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR

- 论文编号：2047
- 报告人：Eugen Beck
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beck26_interspeech.pdf

## 问题
公开英语 ASR 基准多为短切分、朗读/准备语料，且缺少显式方言标注，难以评估对话式、长时、多口音场景；大型开源模型还可能污染公开测试集。呼叫中心类应用尤其需要自发交互、命名实体与领域词汇下的稳健评测。

## 方法
发布 **AppTek Call-Center Dialogues** 评测语料（非训练用）：角色扮演的 agent–customer 对话，覆盖 14 种英语口音、16 类服务场景；专业人工逐字转写（含犹豫、截断等标记）与多轮 QA；另有约 5 小时译成中/德/日/西供 IWSLT 盲测。对多种开源 ASR，在人工切分、AppTek 切分、Silero VAD、固定 30s/60s 切分下按会话聚合 WER 评测。

## 实验与结果
规模：128.6 小时、156 说话人、873 通话、约每口音 8–11 小时。多数模型人工切分 WER 最低；Qwen3-ASR 在 60s 固定切分上更优。Silero 设置下口音间差距大，en SG/CN/GB SCT/IN 普遍偏高，en AU/US General 偏低；强弱口音差距常超 10% 绝对，且平均 WER 好不意味着口音稳健性好。无外部切分时仅少数模型可用。

## 结论
该语料从零采集、未用公开网页材料，便于可复现的长时对话与口音评测；边界检测与口音多样性仍是开放问题，平均准确率提升不能自动转化为口音稳健性。

## 点评
贡献主要在「干净评测基准」：新数据、口音标签、切分消融协议三位一体，对 conversational AI 部署很有针对性。局限也写得很清楚——角色扮演非真实通话、性别不平衡、口音自报+离散标签、无正式 IAA——解读结果时需按「所代表说话人样本」而非整口音社群。
