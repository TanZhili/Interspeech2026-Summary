# Multilingual Speech 1
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Long - Oral / 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

跨领域长论文场从政策–治理框架、大规模合成多语语音问答数据，到社区驱动低资源 ASR 数据集、尼日利亚多语口语语料，再到同声传译的流畅度优化与时延指标元评测。技术与社会维度并置：谁的声音被机器识别，如何低成本扩展语种覆盖，以及实时翻译如何在低时延与自然语流间取舍。

数据与基准建设是主轴：MULTISPEECHQA / BENCH、南阿塞拜疆社区数据与 GoldSet、WazobiaSpeech 的自发口语与元数据。治理论文则提出 3M 伤害分类与参与式审计协议，把识别失败重新解释为隐含语言政策。同传侧 NaturalFlow 用模型内部信号减少块间静音；时延元评测揭示分割相关结构偏差，并提出 YAAL / LongYAAL 与 SOFTSEGMENTER。

瓶颈包括多语语音指令数据稀缺、阿拉伯文字歧义与删除型解码错误、脚本/自发比例、以及短时延追求导致的不自然停顿与指标不一致。

## 技术内容

### 治理框架与多语听解/低资源 ASR 数据

**Decolonizing Linguistic Policies in Automatic Speech Recognition: A Framework for Cross-Culturally Competent Speech AI**（论文 3351；presenter：Jay L. Cunningham）
论证低资源、原住民与非标准变体上的持续失败不仅是技术误差，也是再生产殖民语言等级的隐含语言政策。引入 Three Harms（Misrecognition / Misalignment / Mistrust）与七层情境模型，并提出参与式框架与最低审计协议，让受影响社区成为共设计、评价与治理伙伴。

**Turning Speech Language Models into Multilingual Listeners**（论文 2584；presenter：Tolúlọpẹ́ Ògúnrẹ̀mí）
针对 SLM 语种覆盖窄、多语语音指令数据稀缺，发布合成并经人工核验的 MULTISPEECHQA（约 9200 小时、23 语）与 MULTISPEECH-BENCH。级联系统优于开源权重 SLM 但未必优于全部闭源；用该数据细调 Qwen 2.5-Omni 可提升基准表现。摘要强调高质量合成数据是低成本改进路径。

**Preserving the Iranian Turkic Language: Community-Driven ASR Datasets and Benchmarking for South Azerbaijani**（论文 1516；presenter：Jalil Nourmohammadi Khiarak）
发布南阿塞拜疆首批社区驱动 ASR 数据（含大规模转写话语、社区采集集与 AZB ASR GoldSet），并基准 MMS 与多个 Whisper 族细调模型。全文数据与语种专用细调关键；错误分析指向阿拉伯文歧义与删除主导解码。

**WazobiaSpeech: A Large-Scale Multilingual Speech Corpus for Robust and Fair ASR in Four Nigerian Languages**（论文 3519；presenter：Ife Adebara）
伦理治理下的四语尼日利亚语料，强调多样社会语境中的自然发生口语（少量脚本保证覆盖），含口音、方言、语域、语码转换及人口与情境元数据。报告基线 ASR 与跨语错误分析，含声调敏感性细评。

### 同声传译流畅度与时延评测

**NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation**（论文 540；presenter：Dongwook Lee）
过低时延导致块状破碎语流与频繁停顿。流畅度感知优化利用语言多样性与时长时变等模型内部信号减少块间静音。摘要称在短/长基准上保持有竞争力的时延与翻译质量同时产生更自然语流。

**Better Late Than Never: Meta-Evaluation of Latency Metrics for Simultaneous Speech-to-Text Translation**（论文 575；presenter：Peter Polák）
首个跨语对与系统的时延指标综合元评测，揭示与分割相关的结构偏差；提出短式 YAAL、无分割 LongYAAL 与基于软词对齐的 SOFTSEGMENTER，并在 OMNISTEVAL 中实现。摘要称其优于常用时延指标。

## 本场要点
- 多语 ASR 失败被框架化为伤害类型与治理问题，而非仅 WER。
- 大规模合成+核验语音问答数据可低成本扩展 SLM 语种能力。
- 社区驱动与以自发口语为主的非洲/伊朗突厥语资源填补脚本语料偏差。
- 低资源错误常与文字系统歧义、解码删除相关。
- 同传需在时延之外显式优化听感流畅度。
- 时延评测本身需元评测与重分割工具才能可靠。

## 覆盖核对
`3351 | Decolonizing Linguistic Policies in Automatic Speech Recognition: A Framework for Cross-Culturally Competent Speech AI`
`2584 | Turning Speech Language Models into Multilingual Listeners`
`1516 | Preserving the Iranian Turkic Language: Community-Driven ASR Datasets and Benchmarking for South Azerbaijani`
`3519 | WazobiaSpeech: A Large-Scale Multilingual Speech Corpus for Robust and Fair ASR in Four Nigerian Languages`
`540 | NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation`
`575 | Better Late Than Never: Meta-Evaluation of Latency Metrics for Simultaneous Speech-to-Text Translation`
