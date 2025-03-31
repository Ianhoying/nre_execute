import streamlit as st
import subprocess
import os

# Streamlit UI 구성
st.title("🚀 부동산 크롤링 실행")
st.write("GitHub에서 최신 크롤링 코드를 가져와 실행합니다.")

if st.button("크롤링 실행하기"):
    st.write("✅ GitHub에서 최신 코드 가져오는 중...")
    
    # GitHub에서 최신 코드 가져오기 (로컬 Git 저장소가 있어야 함)
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    st.text(result.stdout)
    
    # 크롤링 코드 실행 (Python 스크립트 실행)
    st.write("🛠 크롤링 실행 중...")
    result = subprocess.run(["python", "crawl.py"], capture_output=True, text=True)
    
    # 실행 결과 출력
    st.text(result.stdout)
    st.write("🎉 크롤링 완료!")
