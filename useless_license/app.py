
import streamlit as st
import random
import html
from datetime import datetime

# ==========================================
# 1. 페이지 설정
# ==========================================
st.set_page_config(
    page_title="쓸모없는 자격증 발급소",
    page_icon="🏆",
    layout="centered"
)

# ==========================================
# 2. 전체 디자인
# ==========================================
st.markdown("""
<style>
.stApp {
    background-color: #FFF8EA;
    color: #593B29;
}

div.stButton > button {
    background-color: white;
    color: #593B29;
    border: 2px solid #D9B995;
    border-radius: 15px;
    min-height: 60px;
    font-size: 17px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #F8E2C9;
    border-color: #C77A43;
    color: #593B29;
}

div[data-testid="stProgress"] > div > div {
    background-color: #C77A43;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. 자격증 8종
# ==========================================
certificates = {
    "집먼지진드기 1급": {
        "emoji": "🛏️",
        "description": "침대와 한 몸이 된 당신! 이불 밖은 위험하다는 신념으로 살아가는 진정한 침대 수호자입니다."
    },
    "역마살 만렙": {
        "emoji": "✈️",
        "description": "집에 가만히 있으면 몸이 근질근질! 새로운 장소를 찾아 떠나는 타고난 방랑자입니다."
    },
    "발등튀김 장인": {
        "emoji": "🔥",
        "description": "마감이 코앞에 와야 능력이 발휘되는 타입! 위기를 기회로 만드는 벼락치기의 달인입니다."
    },
    "배달앱 미아": {
        "emoji": "🍔",
        "description": "메뉴를 고르는 데 하루가 걸리는 당신! 결국 늘 먹던 메뉴로 돌아오는 선택의 미아입니다."
    },
    "디지털 노숙자": {
        "emoji": "📱",
        "description": "휴대폰과 한시도 떨어질 수 없는 당신! 온라인 세상에 상주하는 디지털 생활 전문가입니다."
    },
    "텅장 관리 전문가": {
        "emoji": "💸",
        "description": "돈이 들어오는 속도보다 나가는 속도가 빠른 당신! 소비에 진심인 경제 활동 전문가입니다."
    },
    "작심삼일 문화재": {
        "emoji": "📝",
        "description": "계획을 세울 때는 누구보다 열정적인 당신! 시작은 창대하지만 마무리는 다음 기회에 맡깁니다."
    },
    "행동력 결핍 전문가": {
        "emoji": "🦥",
        "description": "해야 할 일은 알지만 몸이 움직이지 않는 당신! 최소한의 움직임으로 하루를 살아가는 전문가입니다."
    }
}


# ==========================================
# 4. 밸런스 게임 질문 24개
# ==========================================
questions = [
    {
        "question": "주말에 아무 일정이 없다면?",
        "A": "하루 종일 침대에서 뒹굴기",
        "B": "일단 밖으로 나가서 돌아다니기",
        "A_type": "집먼지진드기 1급",
        "B_type": "역마살 만렙"
    },
    {
        "question": "과제 제출 마감일이 다가온다면?",
        "A": "미리미리 끝내놓기",
        "B": "마감 직전에 초인적인 집중력 발휘하기",
        "A_type": "작심삼일 문화재",
        "B_type": "발등튀김 장인"
    },
    {
        "question": "배달 음식을 시키려고 앱을 켰다!",
        "A": "5분 안에 메뉴 결정하기",
        "B": "한 시간 동안 고민하다가 결국 못 고르기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "배달앱 미아"
    },
    {
        "question": "월급이나 용돈이 들어왔다!",
        "A": "바로 사고 싶었던 물건 구매하기",
        "B": "최대한 아껴서 저축하기",
        "A_type": "텅장 관리 전문가",
        "B_type": "작심삼일 문화재"
    },
    {
        "question": "친구가 갑자기 만나자고 한다면?",
        "A": "귀찮으니까 집에 있겠다고 하기",
        "B": "좋아! 바로 나갈 준비하기",
        "A_type": "집먼지진드기 1급",
        "B_type": "역마살 만렙"
    },
    {
        "question": "시험 공부를 시작해야 한다!",
        "A": "일주일 전부터 조금씩 공부하기",
        "B": "시험 전날 밤부터 시작하기",
        "A_type": "작심삼일 문화재",
        "B_type": "발등튀김 장인"
    },
    {
        "question": "여행을 떠날 때 나는?",
        "A": "숙소에서 쉬는 시간이 제일 좋다",
        "B": "하루 종일 돌아다녀야 직성이 풀린다",
        "A_type": "집먼지진드기 1급",
        "B_type": "역마살 만렙"
    },
    {
        "question": "친구와 배달 메뉴를 정해야 한다!",
        "A": "아무거나 빨리 정해서 먹기",
        "B": "리뷰와 메뉴를 끝없이 비교하기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "배달앱 미아"
    },
    {
        "question": "쇼핑몰에서 마음에 드는 물건을 발견했다!",
        "A": "일단 장바구니에 담고 참기",
        "B": "고민은 배송만 늦출 뿐, 바로 결제하기",
        "A_type": "작심삼일 문화재",
        "B_type": "텅장 관리 전문가"
    },
    {
        "question": "해야 할 집안일이 쌓여 있다!",
        "A": "생각났을 때 바로 처리하기",
        "B": "계속 미루다가 마감 직전에 처리하기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "발등튀김 장인"
    },
    {
        "question": "맛집을 발견했다!",
        "A": "집에서 편하게 배달시켜 먹기",
        "B": "직접 찾아가서 먹기",
        "A_type": "집먼지진드기 1급",
        "B_type": "역마살 만렙"
    },
    {
        "question": "휴대폰으로 영상을 보기 시작했다!",
        "A": "하나만 보고 휴대폰 내려놓기",
        "B": "관련 영상까지 계속 찾아보기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "디지털 노숙자"
    },
    {
        "question": "이번 달 소비 계획을 세운다면?",
        "A": "예산을 정하고 지키기",
        "B": "일단 사고 나중에 생각하기",
        "A_type": "작심삼일 문화재",
        "B_type": "텅장 관리 전문가"
    },
    {
        "question": "새로운 취미가 생겼다!",
        "A": "계획부터 꼼꼼하게 세우기",
        "B": "일단 시작하고 생각하기",
        "A_type": "작심삼일 문화재",
        "B_type": "역마살 만렙"
    },
    {
        "question": "휴대폰을 어디에 뒀는지 모르겠다!",
        "A": "주변을 찾아보고 천천히 확인하기",
        "B": "휴대폰으로 내 휴대폰 위치부터 찾으려 하기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "디지털 노숙자"
    },
    {
        "question": "갑자기 여행을 가자고 한다!",
        "A": "집에서 쉬는 게 최고라고 거절하기",
        "B": "일단 가자고 하고 여행 계획 세우기",
        "A_type": "집먼지진드기 1급",
        "B_type": "역마살 만렙"
    },
    {
        "question": "온라인 쇼핑 중 마음에 드는 물건을 발견했다!",
        "A": "며칠 더 고민하고 구매하기",
        "B": "지금 바로 결제하기",
        "A_type": "작심삼일 문화재",
        "B_type": "텅장 관리 전문가"
    },
    {
        "question": "해야 할 일이 있는데 너무 귀찮다!",
        "A": "일단 바로 시작하기",
        "B": "조금만 더 미루기",
        "A_type": "발등튀김 장인",
        "B_type": "행동력 결핍 전문가"
    },
    {
        "question": "새로운 맛집을 찾아보고 있다!",
        "A": "늘 먹던 익숙한 메뉴 주문하기",
        "B": "새로운 메뉴를 찾아 직접 방문하기",
        "A_type": "배달앱 미아",
        "B_type": "역마살 만렙"
    },
    {
        "question": "휴대폰 배터리가 5% 남았다!",
        "A": "바로 충전기를 찾아 충전하기",
        "B": "배터리가 꺼질 때까지 계속 사용하기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "디지털 노숙자"
    },
    {
        "question": "배달 음식을 고르는 상황!",
        "A": "늘 먹던 익숙한 메뉴 선택하기",
        "B": "새로운 메뉴를 계속 탐색하기",
        "A_type": "행동력 결핍 전문가",
        "B_type": "배달앱 미아"
    },
    {
        "question": "새해 목표를 세웠다!",
        "A": "달력에 계획을 꼼꼼하게 적기",
        "B": "일단 의욕적으로 시작하고 나중에 생각하기",
        "A_type": "작심삼일 문화재",
        "B_type": "발등튀김 장인"
    },
    {
        "question": "친구가 맛있는 디저트를 먹자고 한다!",
        "A": "돈 아끼려고 집에서 쉬기",
        "B": "일단 나가서 맛있는 거 먹기",
        "A_type": "집먼지진드기 1급",
        "B_type": "텅장 관리 전문가"
    },
    {
        "question": "휴대폰을 잠깐 확인하려고 켰는데...",
        "A": "확인할 것만 보고 바로 끄기",
        "B": "정신 차려 보니 한 시간이 지나 있음",
        "A_type": "행동력 결핍 전문가",
        "B_type": "디지털 노숙자"
    }
]


# ==========================================
# 5. 세션 상태 초기화
# ==========================================
defaults = {
    "started": False,
    "finished": False,
    "user_name": "",
    "selected_questions": [],
    "current_question": 0,
    "scores": {name: 0 for name in certificates},
    "result": None,
    "certificate_number": None,
    "certificate_date": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==========================================
# 6. 메인 타이틀
# ==========================================
st.markdown(
    "<div style='text-align:center; font-size:55px;'>🏆</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align:center; color:#593B29;'>쓸모없는 자격증 발급소</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#A65B35; font-weight:bold;'>쓸모는 없어도 자격은 확실하게!</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#806B5B;'>당신도 몰랐던 숨겨진 재능을 인증해 드립니다.</p>",
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# 7. 시작 화면
# ==========================================
if not st.session_state.started:

    with st.container(border=True):
        st.markdown(
            "<h2 style='text-align:center;'>🎮 인생 본성 테스트</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;'>24개의 질문 중 12개가 랜덤으로 출제됩니다.</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;'>솔직하게 선택하고 나만의 자격증을 받아보세요!</p>",
            unsafe_allow_html=True
        )

        st.caption("※ 본 자격증은 취업 및 실생활에 아무런 도움이 되지 않습니다.")

    st.write("")

    name = st.text_input(
        "자격증에 들어갈 이름을 입력하세요.",
        placeholder="예: 홍길동"
    )

    if st.button("자격증 발급받으러 가기 🚀", use_container_width=True):

        if not name.strip():
            st.warning("이름을 입력해 주세요!")

        else:
            st.session_state.user_name = name.strip()
            st.session_state.selected_questions = random.sample(questions, 12)
            st.session_state.current_question = 0
            st.session_state.scores = {category: 0 for category in certificates}
            st.session_state.result = None
            st.session_state.started = True
            st.session_state.finished = False

            st.rerun()


# ==========================================
# 8. 밸런스 게임 화면
# ==========================================
elif st.session_state.started and not st.session_state.finished:

    current = st.session_state.current_question
    total = len(st.session_state.selected_questions)
    question = st.session_state.selected_questions[current]

    st.progress((current + 1) / total)

    st.caption(f"QUESTION {current + 1} / {total}")

    with st.container(border=True):
        st.markdown(
            f"<h2 style='text-align:center;'>{html.escape(question['question'])}</h2>",
            unsafe_allow_html=True
        )

    st.write("")

    if st.button(
        "🅰️  " + question["A"],
        key=f"A_{current}",
        use_container_width=True
    ):
        selected_type = question["A_type"]
        st.session_state.scores[selected_type] += 1

        if current + 1 == total:
            st.session_state.finished = True
        else:
            st.session_state.current_question += 1

        st.rerun()

    st.write("")

    if st.button(
        "🅱️  " + question["B"],
        key=f"B_{current}",
        use_container_width=True
    ):
        selected_type = question["B_type"]
        st.session_state.scores[selected_type] += 1

        if current + 1 == total:
            st.session_state.finished = True
        else:
            st.session_state.current_question += 1

        st.rerun()

    st.caption("솔직하게 선택할수록 나에게 맞는 자격증이 발급됩니다!")


# ==========================================
# 9. 결과 화면
# ==========================================
elif st.session_state.finished:

    # 결과 최초 한 번만 선정
    if st.session_state.result is None:

        max_score = max(st.session_state.scores.values())

        winners = [
            name
            for name, score in st.session_state.scores.items()
            if score == max_score
        ]

        st.session_state.result = random.choice(winners)

        now = datetime.now()
        st.session_state.certificate_date = now.strftime("%Y년 %m월 %d일")
        st.session_state.certificate_number = now.strftime("%Y%m%d%H%M%S")

    result = st.session_state.result
    result_info = certificates[result]

    user_name = html.escape(st.session_state.user_name)
    result_name = html.escape(result)
    result_description = html.escape(result_info["description"])
    result_emoji = result_info["emoji"]

    today = st.session_state.certificate_date
    certificate_number = st.session_state.certificate_number

    st.balloons()

    st.markdown("## 🎉 테스트 완료!")
    st.caption("당신의 숨겨진 본성이 밝혀졌습니다.")

    st.write("")

    # ======================================
    # 10. 가로형 A4 자격증 디자인
    # ======================================
    certificate_html = f"""
    <div style="
        width:100%;
        box-sizing:border-box;
        background:#FFFCF3;
        padding:12px;
        border:3px solid #B58A55;
        color:#49351F;
        font-family:Arial, sans-serif;
        box-shadow:0 4px 14px rgba(90,60,30,0.12);
    ">
        <div style="
            border:1.5px solid #B58A55;
            padding:25px 28px;
            min-height:390px;
            box-sizing:border-box;
            position:relative;
        ">

            <div style="text-align:center; color:#79552F;">
                <div style="font-size:25px;">🏛️</div>
                <div style="
                    font-size:19px;
                    font-weight:bold;
                    letter-spacing:2px;
                ">
                    쓸모없는 자격증 발급소
                </div>
                <div style="font-size:10px; letter-spacing:3px; margin-top:4px;">
                    CERTIFICATE ISSUING OFFICE
                </div>
            </div>

            <div style="
                height:1px;
                background:#B58A55;
                margin:17px 0;
            "></div>

            <div style="text-align:center;">
                <div style="
                    font-size:34px;
                    font-weight:bold;
                    letter-spacing:12px;
                    color:#49351F;
                    margin:15px 0 5px 0;
                ">
                    자 격 증
                </div>
                <div style="
                    font-size:10px;
                    color:#987B58;
                    letter-spacing:3px;
                ">
                    CERTIFICATE OF USELESS TALENT
                </div>
            </div>

            <div style="text-align:center; margin-top:27px;">
                <div style="font-size:12px; color:#987B58;">
                    성 명
                </div>
                <div style="
                    font-size:25px;
                    font-weight:bold;
                    margin-top:7px;
                    color:#49351F;
                ">
                    {user_name}
                </div>
            </div>

            <div style="text-align:center; margin-top:23px;">
                <div style="font-size:12px; color:#987B58;">
                    취 득 자 격
                </div>
                <div style="
                    font-size:27px;
                    font-weight:bold;
                    color:#A65B35;
                    margin-top:9px;
                ">
                    {result_emoji} {result_name}
                </div>
                <div style="
                    font-size:13px;
                    line-height:1.8;
                    color:#604C36;
                    margin-top:10px;
                ">
                    {result_description}
                </div>
            </div>

            <div style="
                text-align:center;
                font-size:12px;
                color:#79552F;
                margin-top:25px;
            ">
                위 사람은 본 테스트를 통해 해당 자격을 취득하였으므로
                이에 증명서를 발급합니다.
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:flex-end;
                margin-top:25px;
            ">
                <div style="font-size:11px; color:#79552F; line-height:1.8;">
                    <div>발급일: {today}</div>
                    <div>발급번호: {certificate_number}</div>
                </div>

                <div style="
                    width:68px;
                    height:68px;
                    border:3px double #B64B3C;
                    border-radius:50%;
                    color:#B64B3C;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    text-align:center;
                    font-size:12px;
                    font-weight:bold;
                    transform:rotate(-12deg);
                    box-sizing:border-box;
                ">
                    발급<br>완료
                </div>
            </div>

            <div style="
                text-align:center;
                margin-top:15px;
                border-top:1px solid #D8C3A3;
                padding-top:12px;
                font-size:13px;
                color:#79552F;
                font-weight:bold;
                letter-spacing:2px;
            ">
                쓸모없는 자격증 발급소장
            </div>

        </div>
    </div>
    """

    # st.html은 HTML을 코드가 아닌 실제 화면으로 렌더링
    st.html(certificate_html)

    st.write("")

    # ======================================
    # 11. 점수 결과
    # ======================================
    st.markdown("### 📊 나의 테스트 결과")

    sorted_scores = sorted(
        st.session_state.scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for category, score in sorted_scores:

        if score > 0:
            emoji = certificates[category]["emoji"]

            st.write(f"**{emoji} {category}**")
            st.progress(score / 12)
            st.caption(f"{score}점")

    st.write("")

    # ======================================
    # 12. 다시 테스트하기
    # ======================================
    if st.button("🔄 다시 테스트하기", use_container_width=True):

        st.session_state.started = False
        st.session_state.finished = False
        st.session_state.user_name = ""
        st.session_state.selected_questions = []
        st.session_state.current_question = 0
        st.session_state.result = None
        st.session_state.certificate_number = None
        st.session_state.certificate_date = None

        st.session_state.scores = {
            name: 0 for name in certificates
        }

        st.rerun()

    st.caption(
        "본 자격증은 재미를 위한 가상 자격증이며, 실제 국가공인 자격증과는 관련이 없습니다."
    )
