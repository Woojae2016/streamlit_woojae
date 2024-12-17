import streamlit as st

# MBTI 데이터 딕셔너리 (직업 및 잘 맞는 사람)
mbti_data = {
    "INTJ": {
        "job": "과학자, 전략 컨설턴트, 데이터 분석가 ⚡",
        "partner": "ENFP❤️ - 당신의 창의성을 존중하며 균형을 맞춰줄 수 있는 파트너",
        "description": "계획적이고 분석적인 INTJ! 세상을 바꾸는 청사진을 그리는 당신은 복잡한 문제를 해결하는 데 뛰어난 능력을 가지고 있어요."
    },
    "INFP": {
        "job": "작가, 심리치료사, 교사 📚",
        "partner": "ENTJ❤️ - 당신의 이상을 현실로 만들어줄 추진력 있는 파트너",
        "description": "감수성이 풍부하고 이상주의적인 INFP! 당신은 사람들과 진실된 연결을 맺고 세상에 의미를 더하는 일을 선호해요."
    },
    "ENTP": {
        "job": "창업가, 변호사, 마케터 🌟",
        "partner": "INFJ❤️ - 당신의 에너지를 지혜롭게 이끌어줄 통찰력 있는 파트너",
        "description": "호기심 많고 재기발랄한 ENTP! 새로운 아이디어를 탐구하고 도전하는 것을 즐기는 당신은 진정한 혁신가예요."
    },
    "ISFJ": {
        "job": "간호사, 공무원, 회계사 👥",
        "partner": "ESFP❤️ - 당신의 헌신을 밝은 에너지로 감싸줄 따뜻한 파트너",
        "description": "책임감 있고 섬세한 ISFJ! 당신은 사람들을 도와주며 신뢰받는 존재로 인정받는 것을 중요하게 여겨요."
    }
}

# Streamlit 앱 설정
st.title("\U0001F4C8 MBTI 직업 & 파트너 매칭")
st.write("당신의 MBTI를 선택하면 추천 직업과 잘 맞는 사람을 알려드릴게요! \U0001F3AF")

# MBTI 선택 드롭다운 메뉴
mbti_options = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요! ", mbti_options)

# 선택한 MBTI에 따른 결과 표시
if selected_mbti:
    st.subheader(f"\U0001F4A1 {selected_mbti}의 추천 직업과 이상적인 파트너")
    st.write(f"**추천 직업:** {mbti_data[selected_mbti]['job']}")
    st.write(f"**잘 맞는 파트너:** {mbti_data[selected_mbti]['partner']}")
    st.info(mbti_data[selected_mbti]['description'])
    st.success("당신의 성격 유형에 맞게 세상을 빛내주세요! \U0001F31F")

# 하단 문구
st.write("\U0001F4AB MBTI 성격 유형에 맞는 사람들과 더 나은 관계를 만들어 보세요!")
