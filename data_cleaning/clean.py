import pandas as pd
import ftfy
import html
import re

def clean_dataset(input_file, output_csv, output_xlsx):
    df = pd.read_csv(input_file, sep=None, engine='python', on_bad_lines='skip')
    initial_rows = len(df)

    # 1. إزالة الأسطر التي تعتبر رؤوس مكررة أو قيم خطأ خطيرة
    df_clean = df[~df['source_en'].astype(str).str.contains('source_en|#REF!|TBD', na=False)].copy()

    # 2. تنظيف النصوص والترميز المكسور وكيانات HTML
    def clean_text(text):
        if pd.isna(text):
            return text
        text = str(text)
        if text.strip() in ['#REF!', 'TBD', '###', 'NaN', 'None']:
            return None
        text = html.unescape(text)
        text = ftfy.fix_text(text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    for col in df_clean.columns:
        df_clean[col] = df_clean[col].apply(clean_text)

    # 3. حذف الصفوف الفارغة
    df_clean = df_clean.dropna(subset=['source_en', 'target_ar'], how='all')

    # 4. توحيد التصنيفات وحالة الأحرف
    if 'domain' in df_clean.columns:
        df_clean['domain'] = df_clean['domain'].str.lower().replace({'mktg': 'marketing'})
    if 'status' in df_clean.columns:
        df_clean['status'] = df_clean['status'].str.lower()

    # 5. توحيد صيغ التواريخ
    if 'last_edited' in df_clean.columns:
        df_clean['last_edited'] = pd.to_datetime(df_clean['last_edited'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 6. إزالة التكرارات التامة والشبه تامة
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.drop_duplicates(subset=['source_en', 'target_ar'], keep='first')

    # 7. حفظ النتائج
    df_clean.to_csv(output_csv, index=False)
    df_clean.to_excel(output_xlsx, index=False)
    print("✅ تم تنفيذ التنظيف بنجاح بواسطة clean.py")

if __name__ == '__main__':
    clean_dataset('/Data_A_legal_termbases_RAW.xlsx', 'dataset_A_legal_termbase_CLEAN.csv', 'dataset_A_legal_termbase_CLEAN.xlsx')
