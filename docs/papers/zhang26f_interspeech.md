# CoRE: Contrastive Evidence-Aware Rescoring for Multiple-Choice Audio Question Answering

- 论文编号：656
- 报告人：Yiqiang Cai
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26f_interspeech.pdf

## 问题
LALM 做多选 AQA 时常被问题/选项的文本先验主导，忽视声学证据。静音对比等干预易引入伪影；解码级对比也不贴选项打分协议。

## 方法
免训练插件 **CoRE**：将波形切成 40 ms 块，随机置换并按概率时间反转，破坏长程时序同时近似保留短时声学；在统一选项似然打分下对比原音频与反事实音频的选项 logits 得证据增益 \(\Delta\)；用 JSD 冲突与单向熵降的几何平均门控 \(\beta\) 做凸插值重打分。评 Qwen2-Audio / Kimi-Audio，DCASE 2025 Task 5（BQA/TSQA/CQA）与 AIR-Bench SoundQA。

## 实验与结果
相对 Default、提示工程、AAD、CoRE-Silence，CoRE 全面最优；如 Qwen BQA 从 30.0 到 40.7，Kimi BQA 43.3→51.9。SSM 验证置换+反转对全局相关破坏最大、局部统计几乎不变。门控消融显示自适应几何平均优于固定 \(\beta\) 或单信号门。

## 结论
信息性反事实音频 + 证据感知门控可在测试时缓解模态偏置；每例多一次前向，拟扩展到生成式 AQA。

## 点评
把视觉对比解码改造成“打乱时序但不抽走音频”的负条件，更贴多选 AQA。强在协议统一与消融完整。局限：CQA 增益较小、\(\tau\)/反转概率固定、对生成答案未验证。
