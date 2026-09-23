# A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography

- 论文编号：1822
- 报告人：Yigitcan Özer
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ozer26_interspeech.pdf

## 问题
部分篡改语音（仅替换短片段）使被动检测器随伪造占比下降而不可靠，定位与恢复也难。需要不依赖大规模训练的主动防御。

## 方法
自嵌入隐写：干净语音把自身压缩表示嵌回波形；接收端提取参考并经编解码式重建 R(y)，再与收到信号 y 用 mel-log 谱上的 DTW（余弦距离）对齐，路径平均代价 s_DTW 作操纵分数。复用现有音频隐写方法，无需为检测任务训练。在 AV-Deepfake1M 验证集音频子集上，攻击替换同说话人 1–2 个词的重合成片段做概念验证。

## 实验与结果
正文报告该主动方案可与被动防御互补；操纵处 DTW 路径偏离对角线、累积代价升高。抽取文本对完整量化表覆盖有限，但强调无训练、数据高效。

## 结论
作者认为自嵌入隐写可为部分 deepfake 提供可部署的主动检测与恢复线索，补被动系统短板。

## 点评
把隐写从版权水印转到“自参考完整性校验”，对短局部篡改很对症且免训练。脆弱点在攻击者察觉并破坏/重嵌水印，以及压缩自嵌入引入的可听失真与信道鲁棒性权衡。
