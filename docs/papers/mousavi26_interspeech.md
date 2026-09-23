# Investigating Faithfulness in Large Audio Language Models

- 论文编号：1533
- 报告人：Pooneh Mousavi
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/mousavi26_interspeech.pdf

## 问题
LALM 可生成 CoT，但相对输入音频与最终答案是否忠实未知；音频条件可能带来幻觉、局部注意或忽视指令等问题。

## 方法
定义音频忠实三准则：无幻觉听、整体听、专注听，外加 CoT–输出忠实。对 Audio Flamingo 3-Think 与 Qwen2.5-Omni，在 SAKURA/MMAR/MMAU 上做音频干预（噪声 SNR、随机/引导掩蔽、对抗语音提示）与 CoT 干预（改写、填充、早答、注入错误）。用答案一致性与 LLM-as-judge 评 CoT 一致性。

## 实验与结果
极端噪声下模型仍常产生看似合理但未接地的推理；掩蔽与对抗提示可大幅改变准确率与一致性，显示对局部线索或注入答案敏感。CoT 常与最终答案一致，但对音频接地较弱，易受扰动。提示存在多模态脱节。

## 结论
LALM 的 CoT 更像与答案对齐的叙述，未必忠实反映音频决策过程；需干预式评测而非仅看准确率。

## 点评
把文本 LLM 忠实性干预迁到音频条件，问题设定重要。依赖 LLM 裁判与自动化解析 CoT，可能引入评判偏差；两模型样本也限制外推到闭源商用系统。
