# Audiovisual CXMI: Scene-based Context Tagging for Spoken Language Translation Evaluation

- 论文编号：2175
- 报告人：Dayeon Ku
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/ku26_interspeech.pdf

## 问题
句级指标难衡量上下文利用；文本 CXMI 能量化上下文，但缺视听线索，实验中甚至给人译打分低于机译，与人类判断相反。

## 方法
提出 AV-CXMI：镜头检测 + ResNet 场景边界，再用分离人声、ECAPA 说话人聚类与 Jaccard 重叠 refine 场景。从视频/音频用 GPT-4o（及音频变体）提取 SETTING/REL/TIME/MOOD，并用分类器得 DIALOG/POLITENESS；标签与前 k=2 句构成扩展上下文。mBART 式模型在匹配标签条件下比较有无文本上下文的交叉熵差。韩–英影视翻译上验证。

## 实验与结果
AV-CXMI 与人类判断 Pearson r=0.400（p<0.003），系统效应 η²=0.519（p<0.001），优于纯文本 CXMI；在 77.8% 样本上恢复预期系统质量排序，缓解“人译被文本 CXMI 低估”现象。

## 结论
场景级视听标签扩展 CXMI，使口语/影视翻译评测更能反映情境一致性与人类偏好。

## 点评
抓住评测与人类语用判断错位这一痛点，用结构化 AV 标签而非原始多模态特征，便于解释与复现。依赖 LLM 标注与自洽解码有成本与偏差风险；场景 refine 对音乐/多人重叠仍可能不稳。
