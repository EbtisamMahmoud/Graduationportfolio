# تقرير مشروع التصنيف والتوصيف - Label Studio

## 1. ملخص المشروعين (Project Summary)

### **Project A — NER قانوني**
* **هدف المشروع:** استخراج والتعرف على الكيانات المسماة (Named Entity Recognition) في النصوص القانونية.
* **الكيانات المعتمدة:** `ORG`, `PERSON`, `COURT`, `LAW_STATUTE`, `CASE`, `JURISDICTION`, `DATE`, `MONEY`, `LEGAL_TERM`, `ROLE`.
* **إجمالي المهام المكتملة:** 18/18
* **الملفات المرفقة للتصدير:** 
  - `ls_task1_NER_legal_tasks.json`

### **Project B — تصنيف البرومبتات (Prompt Classification)**
* **هدف المشروع:** تصنيف الأوامر والبرومبتات وفق معايير التقنية، الجودة، والمخاطر مع ذكر التبرير.
* **إجمالي المهام المكتملة:** 18/18
* **الملفات المرفقة للتصدير:** 
  - `ls_task2_prompt_classification_tasks.json`
---

## 2. لقطات الشاشة والتحقق (Screenshots & Verification)

تم إرفاق لقطات الشاشة في مجلد `screenshots/` كالتالي:

### 1. نظرة عامة على المشاريع:
![شاشة المشاريع المكتملة](overview.png)

### 2. مشروع NER القانوني (Project A):
![مشروع A](project_a.png)

### 3. مشروع تصنيف البرومبتات (Project B):
![مشروع B](project_b.png)

---

## 3. ملاحظات ومعايير الجودة (Quality & Consistency Notes)

* تم التأكد من عدم وجود أي مهمة فارغة (Unannotated).
* تم الالتزام بتحديد الكيانات القانونية بدقة وفق دليل الكيانات المعطى بدون تداخل غير مبرر.
* تم كتابة التبرير (Reasoning/Rationale) لكل برومبت في Project B بشكل واضح ومتسق مع معايير التقنية والمخاطر.