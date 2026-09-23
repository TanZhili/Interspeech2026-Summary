# The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS

- 论文编号：66
- 报告人：Kuan-Yu Chen
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26b_interspeech.pdf

## 问题
指令式 TTS（ITTS）评测性别偏见多做单属性探测，忽略社会地位、职业刻板与人格描述等线索的组合；现实提示下的 Binding Effect 会改写单维先验，掩盖交叉偏差。

## 方法
将控制空间解耦为 Social Status、Career、Persona（Big Five）三轴；Stage1 测单描述符的女性声学概率 \(P(x)\)（wav2vec2 性别分类器）；Stage2 构造双/三维组合，在 logit 空间量化相对加性基线的交互项 \(I\)。评 VoxInstruct、PromptTTS++、Parler Mini/Large；每描述符 100 条性别中性内容句。并比对文本编码器语义先验与训练数据人口分布。

## 实验与结果
单维上职业/人格常强偏女性；组合后出现显著 Binding Effect 与主导覆盖（如高地位+reckless 可翻转 nurse 的女性先验）。交互模式与预训练文本编码器语义先验强相关，不止训练数据倾斜。通用多样性提示难覆写这些组合偏差；上下文属性插入更可行。

## 结论
ITTS 性别偏差具组合依赖，需成分化诊断；偏见根源更多在文本编码器先验。缓解应面向组合动态而非单维提示。

## 点评
把交叉社会线索写入可控实验，比“测 nurse 是否女声”更贴近部署。依赖声学性别分类器作代理，音色/F0 与社会性别不完全等同；提示模板由 Gemini 生成，也可能引入额外先验。
