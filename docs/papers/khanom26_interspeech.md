# SpiroPhonia: Non-Invasive Respiratory Health Assessment from Spontaneous Speech

- 论文编号：2571
- 报告人：Roksana Khanom
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khanom26_interspeech.pdf

## 问题
COPD 诊断依赖肺量计等临床设施，难连续居家监测。既有语音呼吸研究多靠朗读/持续发声等受控任务；自发对话是否含稳健、受试者无关的呼吸生物标志仍不清楚。

## 方法
SpiroPhonia：从公开访谈等收集英语自发语音，医师核验标签，201 人（102 呼吸疾病 / 99 对照，45–95 岁）。预处理切 10–30s、带通与轻降噪；提声学扰动（F0、jitter/shimmer、HNR、共振峰）、MFCC 统计、停顿时序特征；统计筛选后递归特征选择；可解释分类器（如 Linear SVM、Gradient Boosting）做受试者无关评测，并讨论筛查/端侧配置。

## 实验与结果
多组特征组间显著（如 RAP/DDP jitter、MFCC10、停顿率/每分停顿数）。最佳模型约 78% accuracy、80% F1、87% AUC（摘要）；表中 Linear SVM（5 特征）accuracy 约 78%、AUC 约 79%。作者称与受控录音方法竞争力相当，支持日常语音编码呼吸信息。

## 结论
自发语音可提供紧凑、可解释的 COPD 相关声学–频谱–时序标志，通向语音设备上的被动筛查。数据可应请求用于学术研究。

## 点评
把场景从实验室任务推到野生对话，并强调少特征可解释模型，部署叙事清晰。公开网络数据有选择偏差（谁愿意上镜谈病、录音质量），标签靠内容核验而非统一肺功能金标；与年龄/说话风格混杂需谨慎。适合筛查线索，不宜替代临床诊断。
