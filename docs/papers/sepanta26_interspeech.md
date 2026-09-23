# From Game-Based Annotation to Representation Probing: Cross-Validated Prosodic Speech and Privacy Implications

- 论文编号：2459
- 报告人：Sia Vosh Sepanta
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sepanta26_interspeech.pdf

## 问题
情感语音库常标注人少、演员少、短句缺语境；游戏化采集能否产出可用韵律数据，以及语音–LLM 中间表示是否泄露情感/年龄等隐私属性，需要实证。

## 方法
Actor’s Challenge（GWAP）：玩家交替“试镜”按情境录中性句与“选角”匹配语境并打分，形成自验证。当前约 240 用户、1,018 录音、七类情绪。用 emotion2vec 嵌入 + 轻量分类器做 ASER，并与 RAVDESS、Emozionalmente 交叉；再以 Whisper→MEUSLI→EuroLLM 冻结管线探测情感与年龄泄漏。

## 实验与结果
4 类 ASER：AC 英/意 Acc 约 0.73/0.75，混合降至 0.60；RAVDESS 0.92。跨库到 AC 较差（约 0.32–0.40），AC→RAVDESS 可达 0.93。表示探测 7 类情感：LLM 隐状态 Acc 0.21，投影/编码器约 0.41–0.42，表明情感在中间层已可分。

## 结论
游戏化自验证可构建多语语境化韵律库；情感线索可被下游模型利用，但中间表示的情感/人口属性可探性带来隐私风险，发布与使用需谨慎。

## 点评
把标注一致性内置进游戏循环，并延伸到表示隐私，视角新。强在自验证与跨库对照；弱在规模仍小、参与衰减、态度韵律覆盖不足，ASER 数字更像可用性探针而非 SOTA 竞赛。
