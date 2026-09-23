# ProWhistress: An Enhanced Dual-Stream Transcription Architecture for Prosody-Aware Sentence Stress Detection

- 论文编号：1303
- 报告人：Hujian Gu
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gu26b_interspeech.pdf

## 问题
无对齐句重音检测中，Whisper 深层表征偏语义、削弱细粒度韵律；普通话重音数据稀缺，现有英语中心方法难直接迁移。

## 方法
ProWhistress：冻结 Whisper 隐式流 + 可训声学编码器（抽中间层）双流；经额外解码块、瓶颈交叉注意与门控残差融合后做 token 级重音分类。另建 SinoStress-Syn（约 12 h，层级 LLM 标注重音+TTS）与 SinoStress-Real（约 3 h 真人）。

## 实验与结果
英语 TinyStress-15k F1 0.959（Whistress 0.909）；零样本 Expresso/EmphAssess 亦显著优于基线。普通话 Syn F1 0.958、Real 监督/零样本约 0.870/0.869，Sim-to-Real 几乎不掉。消融确认双流互补、编码器第 9 层最佳、瓶颈融合优于全维注意。

## 结论
显式声学流缓解语义–韵律权衡，并在中英基准与零样本真实语音上领先；填补普通话句重音数据缺口。

## 点评
门控残差把“补回声学细节”做成可控注入，零样本稳定是亮点。合成重音靠音高/音量/语速规则，复杂对比焦点等仍可能简化；真实集说话人少，泛化边界需更大真人数据验证。
