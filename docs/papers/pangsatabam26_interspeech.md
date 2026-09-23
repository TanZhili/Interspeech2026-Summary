# Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur

- 论文编号：2304
- 报告人：Hoomexsun Pangsatabam
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/pangsatabam26_interspeech.pdf

## 问题
曼尼普尔邦多数部落语言使用改编拉丁文正字法，方言与拼写不统一，缺乏可用 TTS 语料；既有 Indic 资源几乎不覆盖 Tangkhul、Maring 等藏缅语。

## 方法
工作室教材/故事/圣经译本文本，单说话人棚录（各一名标准方言女声），经 VAD 切分（2–8 s）、22.05 kHz 重采样与 LUFS 响度归一，得到 Tangkhul 9.58 h、Maring 10.79 h。字符级训练 Tacotron 2 与 FastSpeech 2（ESPnet），声码器用 Griffin–Lim 或 StyleMelGAN。开放预处理管线。

## 实验与结果
StyleMelGAN 相对 Griffin–Lim 显著降 MCD；FastSpeech2+SM 总体更优（如 Tangkhul Blind MOS 3.06、Maring 3.51）。Maring 听感受方言差异影响大；Tangkhul 变音符字符化易致短时不可懂。英语预训练模型因忽略声调等差异无法替代。

## 结论
约 10 h 棚录语料即可为拉丁文低资源声调语言建立可用基线；同脚本不保证跨语迁移。未来拟共享音素空间与实时部署。

## 点评
资源与管线贡献大于模型创新，对“无原生文字”情境务实。方言听感与变音符建模暴露了字符级正字法的脆弱点；单说话人限制表达多样性。
