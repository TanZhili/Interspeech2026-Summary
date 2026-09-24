# Bridging the Speech AI Accessibility Gap for Deaf and Hard of Hearing People

- 论文编号：3001
- 报告人：Christian Vogler
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/glasser26_interspeech.pdf

## 问题
聋人/听障（DHH）用户常有“聋口音”并依赖语音 AI，但 STT/TTS/STS 多按健听数据训练；许多 DHH 无法充分听清合成输出以自检，文本又丢失韵律与副语言信息，造成可用性与信任缺口。

## 方法
立场论文：三位可发声的聋人手语者基于亲身经验，提出设计框架 UVG（Usability、Verifiability、Graceful Degradation）与 FATE（公平、问责、透明、伦理）。分别分析 STT（聋语音识别差、幻觉风险、多人会议壁垒）、TTS（无法验证情感/韵律、需保留可理解的个人声音身份）、STS（口音重说与手语口译再配音两场景）及数据/隐私/社区边缘化风险。

## 实验与结果
无新模型实验；引用既往：聋音在受限数字识别仍可有约 13% WER，人类可懂度与 ASR 表现相关性弱，商业 ASR 对 DHH 持续欠佳。强调失败时应停止并告知而非幻觉填词。

## 结论
语音 AI 须以 DHH 为中心设计：可非听觉验证、优雅降级、个性化且可理解的声音身份，并避免无社区参与的数据采集与部署。

## 点评
把“听不清就不能验输出”这一常被忽略的可验证性写成一等公民需求，对 TTS/STS 尤其尖锐。UVG+FATE 可作产品清单。作为立场文缺少量化新基线，但场景拆解（混会、口译配音性别/族裔错配）对工程优先级很有指导性。
