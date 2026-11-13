# [위치] apps/part2.py 새 파일
import streamlit as st
st.title("심부전 환자 기록")
st.header("1. 데이터 소개")
st.subheader("어떤 환자들인가")
st.markdown("심부전으로 입원한 환자 **299명**의 기록입니다.")
st.caption("출처: UCI Machine Learning Repository")

# [위치] apps/part2.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write("변수는 12개, 결과는 사망 여부 1개입니다.")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
st.success("데이터를 불러왔습니다.")
st.info("왼쪽에서 나이 범위를 고르세요.")
st.warning("조건에 맞는 환자가 10명 미만입니다.")


# [위치] apps/part2.py — 맨 위 import 줄 아래에 끼워 넣기
# ▼ 이미 있는 줄
import streamlit as st
# ▼ 이 줄 아래에 새로 (0칸)
import pandas as pd
DATA = r"C:\Users\asia\Desktop\수업\apps\heart_failure_clinical_records_dataset.csv"
# [위치] apps/part2.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.error("파일을 찾을 수 없습니다.")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
st.header("2. 데이터 표")
df = pd.read_csv(DATA)
st.write(f"행 수: {len(df)} · 열 수: {df.shape[1]}")
st.dataframe(df.head(), width="stretch")


# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
st.header("3. 핵심 숫자")
all_rate = df["DEATH_EVENT"].mean() * 100
old = df[df["age"] >= 65]
old_rate = old["DEATH_EVENT"].mean() * 100
st.metric("전체 환자 수", f"{len(df)}명")
st.metric("전체 사망 비율", f"{all_rate:.1f}%")
st.metric("65세 이상 사망 비율", f"{old_rate:.1f}%",
delta=f"{old_rate - all_rate:+.1f}%p (전체 대비)",
delta_color="inverse")