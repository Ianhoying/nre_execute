import streamlit as st
import pandas as pd
import sys

sys.path.append("realEstate_crawler")

from crawler_p1 import execute, code  # 크롤링 관련 모듈 가져오기

def run_crawler():
    st.write("🏡 **부동산 크롤러 실행 중...**")
    
    total = pd.DataFrame()
    raw = pd.DataFrame()
    
    for gu_info in code:
        t, r = execute(gu_info)
        total = pd.concat([total, t], ignore_index=True)
        raw = pd.concat([raw, r], ignore_index=True)
    
    return total, raw

# Streamlit UI 구성
st.title("🏠 부동산 크롤러 대시보드")

if st.button("크롤링 시작"):
    total_df, raw_df = run_crawler()
    
    st.write("### 📊 수집된 데이터 (Total)")
    st.dataframe(total_df)
    
    st.write("### 📝 원본 데이터 (Raw)")
    st.dataframe(raw_df)
    
    # CSV 파일 다운로드 기능
    # csv = total_df.to_csv(index=False).encode('utf-8-sig')
    # st.download_button(
    #     label="📥 Total 데이터 다운로드",
    #     data=csv,
    #     file_name="total_data.csv",
    #     mime="text/csv",
    # )
