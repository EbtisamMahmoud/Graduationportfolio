import pandas as pd
import numpy as np

def clean_dataset_b(input_file, output_xlsx):
    # 1. قراءة البيانات مع استبعاد التعليقات
    df_b = pd.read_csv(input_file, comment='#', on_bad_lines='skip')

    # 2. تنظيف المسافات الزائدة
    for col in df_b.select_dtypes(include='object').columns:
        df_b[col] = df_b[col].astype(str).str.strip()

    # 3. تحويل المبالغ إلى أرقام
    def clean_amount(val):
        if pd.isna(val): return np.nan
        try: return float(str(val).replace('$', '').replace(',', '').strip())
        except: return np.nan

    if 'Amount' in df_b.columns:
        df_b['Amount'] = df_b['Amount'].apply(clean_amount)

    # 4. توحيد العملة للجنيه المصري (1 USD = 50 EGP)
    EXCHANGE_RATE = 50.0
    if 'Currency' in df_b.columns:
        df_b['Amount_EGP'] = np.where(
            df_b['Currency'].astype(str).str.upper() == 'USD',
            df_b['Amount'] * EXCHANGE_RATE,
            df_b['Amount']
        )
    else:
        df_b['Amount_EGP'] = df_b['Amount']

    # 5. إزالة التكرارات
    df_b_clean = df_b.drop_duplicates().copy()

    # 6. حفظ الملف المُنظّف
    df_b_clean.to_excel(output_xlsx, index=False)
    print("✅ تم تنظيف Dataset B وحفظها بنجاح!")

if __name__ == '__main__':
    clean_dataset_b('dataset_B_company_ledger_RAW.csv', 'dataset_B_company_ledger_CLEAN.xlsx')
