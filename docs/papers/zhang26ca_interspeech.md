# ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling

- 论文编号：2134
- 报告人：Mengke Zhang
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26ca_interspeech.pdf

## 问题
多模态 SER / Audio LLM 在声学与文本情感冲突（讽刺等）时出现“语义主导”，盲目信文本；标准语料过滤不一致样本加剧该先验，融合重加权无法修复已塌缩的声学表征。

## 方法
提出对抗合成基准 ASPIRE（EmotiVoice，四类冲突：极性/唤醒/效价对立、情绪掩蔽）及指标 SOP（文本相对声学的过自信惩罚）、LDD（声学—语义潜空间正交度）。ACR-Net：冻结 Whisper + LoRA 双流，Cross-Modal Attention 检不一致，Contrastive Decoupling Loss 把冲突表征推入正交子空间。

## 实验与结果
ASPIRE 上 ACR-Net ACC 76.5%、SOP 0.128、LDD 0.864，显著优于朴素拼接/张量融合/MCR 与仅 CMA。极性冲突上融合法 ACC<45%、SOP>0.5；ACR-Net 维持高 LDD。一致场景（EmoDB 等）仍具竞争力（如 EmoDB 88.5%），未因解耦而崩。

## 结论
显式表征解耦优于决策层重加权，可在声学—语义冲突下保住声学保真并压低语义过自信。

## 点评
诊断（SOP/LDD）与解法对齐清楚，把“语义捷径”做成可测压力测试。ASPIRE 为 TTS 合成，真实讽刺边界更模糊；与并发 FAS/CASE 的差异在对抗合成与表征级解耦，落地仍需真实冲突数据验证。
