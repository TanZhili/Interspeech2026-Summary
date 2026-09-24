# What Do Deepfake Speech Detectors Actually Hear?

- 论文编号：123
- 报告人：Vojtěch Staněk
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26_interspeech.pdf

## 问题
深度伪造语音检测器常只给分数，难说明证据在时间何处、依赖何种线索；同性能模型是否学到不同决策逻辑。

## 方法
对 WavLM Base+ 时齐帧表示做 Integrated Gradients，相对 bona fide 质心基线，层/维求和得时间归因；人工标注最高归因区的线索类型与局部性。检测器：AASIST、CA-MHFA、SLS，联合微调 SSL+后端。在 ASVspoof 5 上取 100 条（高置信正确/错误与边界）做语义标注，并用静音/高能音素/频谱/压缩掩码做因果验证。

## 实验与结果
EER：AASIST 4.06%、CA-MHFA 5.26%、SLS 3.98%；三分数 LR 融合 3.77%。语义上 AASIST 偏非语音/环境，CA-MHFA 偏局部音素伪影，SLS 偏词界与谱完整性。掩码：静音扰动重创 AASIST（FARb→99.99%）；压缩使三者 FRR 升。重压缩与 YourTTS(A28) 主导高置信错误。

## 结论
相近性能可依赖互补线索；IG+人工语义+掩码验证可回答“侦测器实际听什么”，并提示压缩伪影是共性弱点。

## 点评
把可解释性从定性例子推到结构化标注与因果消融，证据链完整。子集仅 100 条、标注主观；融合增益有限因共享压缩失败模式。
