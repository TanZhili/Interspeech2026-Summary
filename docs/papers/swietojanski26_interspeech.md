# Segmental Attention Decoding With Long Form Acoustic Encodings

- 论文编号：341
- 报告人：Xinwei Li
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/swietojanski26_interspeech.pdf

## 问题
AED 在分段语料上训练时，交叉注意力会利用段边界「残缺上下文」作隐式绝对位置锚点；长时流式编码（LFE）消除这些边界线索后，因 key/value 置换不变性无法排序声学编码，表现为重复转写、难以发 EOS，自回归注意力解码崩溃。

## 方法
四项修改：
1. **交叉注意力绝对位置编码**：对每段 \(H_s\) 加段内复位的位置码，再进 cross-attention。
2. **声学上下文扩展 (AC)**：训练时为 LF 样本左右扩上下文，使段内编码成为真 LFE，但不对损失使用两侧无效帧。
3. **段拼接 (SC)**：拼接连续段与非语音邻域，丰富时长与 LFE 暴露。
4. **语义切分 (SS)**：CTC 头预测语义句界 token，触发二遍 AD，优于纯 VAD。

模型为 CTC-AED（Ours.base ~90M / Ours.small ~240M），编码器因果 Conformer + 可变 chunk，解码器固定约 18M。

## 实验与结果
TED-LIUM3 消融：基线 LFE 上纯 AD WER 达 295%；SC+AC+PE 后 AD 与 SFE 持平（约 5.0%）；加 SS 后 CTC-Att 达 4.3%。最终：Ours.small CAT@3.84s 在 Tedlium3 LF 3.9%、Earnings21 11.4%，短切分任务也不退化；相对同量级 Whisper 延迟更低、多数集合更优（部分集合作者注明非零样本）。

## 结论
AC 与段级 PE 互补，可关闭连续编码与分段编码的精度差距，使注意力解码器可对长时编码自回归使用；CTC 语义切分优于 VAD，混合 CTC-Att 更稳。

## 点评
问题诊断很扎实：把长时失败归因到「边界捷径消失 + 置换不变」，对策也对准这两点。强在系统消融清晰、部署上保留流式编码器与轻量解码器；脆弱点是强依赖训练侧 AC/SC 数据改造，且对伪标签 SpeechCrawl 质量敏感，语义 seg 标签本身也引入外部 Segment any Text 管线。
