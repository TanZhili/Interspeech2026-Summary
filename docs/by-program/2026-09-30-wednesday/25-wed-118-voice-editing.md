# Voice Editing

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 7 - Oral 2）
- Area：7
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。不添加摘要未写明的机制细节。

## 技术趋势

本场聚焦语音/音频的可控编辑：终身发音适配、属性匿名化中的隐私—质量权衡、噪声标签下的鲁棒属性编辑、参考语音与文本描述联合控制、基于文本的内容编辑，以及开放式自然语言指令编辑。

一条主线是“改什么、保什么”的分解：FlowEdit 在冻结 flow-matching TTS 上把发音纠正存为潜在条件编辑与 Hopfield 情景记忆；另一条用幂等性目标提升对噪声年龄/性别标注的编辑鲁棒；文本编辑则主张在语义空间改内容、由 Flow Matching 解码器保声学连续，并用自一致性奖励巩固感知一致。

联合控制与开放编辑方面，FineCombo-TTS 学习统一声学表示并以 CFM 方差预测器做参考到目标的细粒度变换；Bagpiper-Edit 把编辑重写为富字幕改写，实现免配对数据的零样本跨语音/音乐/声音编辑。匿名化工作则量化年龄与性别属性偏移对身份抑制与自然度的不同斜率，指出存在适度修改的最优匿名区。

## 技术内容

### 终身发音适配与属性编辑鲁棒性

**FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS**（论文 2764；presenter：Nityanand Mathur）  
部署后 flow-matching TTS 对 OOV 专有名词发音错误需重训才能修正。FlowEdit 在冻结模型上优化文本嵌入空间的 token 级扰动，并写入 Modern Hopfield Network 情景记忆；推理时经相似度门控软注意力检索，支持模糊形态匹配。在 18 个语系、312 个多语专有名词基准上，目标词音素错误率相对零样本基线相对下降 92.7%，通用语音质量不变；单卡约 15 秒完成纠正。

**RIVET: Robust Idempotent Voice Attribute Editing**（论文 395；presenter：Dareen Alharthi）  
大规模数据中年龄/性别等标注常噪声不一致，导致条件生成编辑不稳定。RIVET 引入幂等性目标（f(f(x))=f(x)）作隐式正则，降低对错误标注敏感。在受控标签噪声与天然噪声的 GLOBE 上，相对标准训练提高编辑成功率并更好保持说话人身份。

**Privacy and quality trade-off in real-time speaker anonymization via editing of age and sex attributes**（论文 2741；presenter：Waris Quamer）  
在流式语音合成中隔离年龄与性别属性修改，用说话人余弦相似度与 DNS-MOS 做线性回归量化对隐私与质量的影响，并以听感测试验证。结果显示隐私（身份）随修改增大下降快于质量下降，存在适度属性变化即可有效抑制身份且自然度损失最小的最优匿名区。

### 联合可控合成与内容/开放式编辑

**FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech**（论文 2280；presenter：Zhiyong Wu）  
针对仅参考语音或仅文本描述不够灵活、以及松耦合联合方法把音色与全局风格割裂的问题，学习统一声学表示，并用基于 CFM 的 Speech Variance Predictor 在文本描述引导下建模细粒度参考→目标变换；构建显式编码源—目标属性变化的 FineEdit 配对数据以支持相对属性控制。实验显示灵活、精确且富表现力的可控 TTS。

**Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards**（论文 1186；presenter：Yong Ren）  
主张在稳定语义空间编辑内容，声学由 Flow Matching 解码器实现；提出 Self-Consistency Rewards Group Relative Policy Optimization，以预训练 TTS 为隐式评判，并加可懂度与时长约束。相对 SOTA 自回归与非自回归基线，在可懂度、鲁棒性与感知质量上一致提升。

**Bagpiper-Edit: Zero-Shot Open-Ended Audio Editing via Rich-Caption**（论文 631；presenter：William Chen）  
将开放式编辑重写为富字幕改写：用户请求译为编辑后字幕，再以原音频为声学锚生成目标，无需配对编辑训练数据。跨语音、音频与自由形式编辑评估显示与原音频一致性良好，多数情形接近专家模型表现。

## 本场要点

- 终身发音纠正可在冻结 TTS 上以潜在编辑+联想记忆完成，避免全量重训。
- 幂等性约束提升噪声属性标签下的编辑稳健与身份保持。
- 年龄/性别匿名存在隐私下降快于质量下降的最优工作区。
- 参考语音与文本描述可通过统一表示与 CFM 方差预测实现细粒度联合控制。
- “改内容、保声学”与自一致性奖励改善文本驱动语音编辑的感知连续。
- 富字幕改写解锁零样本开放式跨域音频编辑。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 2764 | FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS |
| 2741 | Privacy and quality trade-off in real-time speaker anonymization via editing of age and sex attributes |
| 395 | RIVET: Robust Idempotent Voice Attribute Editing |
| 2280 | FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech |
| 1186 | Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards |
| 631 | Bagpiper-Edit: Zero-Shot Open-Ended Audio Editing via Rich-Caption |
