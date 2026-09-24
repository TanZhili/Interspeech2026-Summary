# When Machines Speak Like Local Peers: Improving Conversational Experiences with Accent-Adaptive Voice Agents

- 论文编号：2197
- 报告人：Shubhangi S. R. Garnaik
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/garnaik26_interspeech.pdf

## 问题
公共场景语音助手对口音英语用户表现不均，损害可用性与信任。口音自适应回复（尤其带说话人脸视频）应如何安全部署仍缺系统证据。

## 方法
LocalMATE 机场场景端到端代理：WavLM 口音估计（印度/韩/西）+ 置信缓存；Whisper ASR；FAQ 嵌入检索；VEVO 口音条件 TTS + 同步说话人脸；低置信时置信门控回退。口音分类说话人独立评测；N=20 被试内用户研究比较正确/错误适配与回退策略。

## 实验与结果
口音估计：L2-ARCTIC 说话人独立准确率 85%；域外韩式 Speech Accent Archive 92.3%。用户研究：正确口音适配显著提高信心与信任、减少修复尝试（p<0.05）；错误适配降低信任并增加摩擦；置信门控回退可缓解并恢复信心。

## 结论
口音自适应能提升体验，但错误适配有害；置信门控是必要安全阀。

## 点评
把“适配收益”与“误适配成本”放在同一用户研究里，结论对部署很务实。场景限于 FAQ 机场助手与三种口音；信任指标自报、样本 N=20。TTS 口音迁移质量仍是体验瓶颈。
