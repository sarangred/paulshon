import streamlit as st
import pandas as pd
import os

# 설명문 추가
st.write("""
# 생성형 AI와 인간의 창작에 관한 설문조사
아래의 표는 Q방법론(주관성연구)의   Q 표본 분류표입니다.   
""")

# 이미지 추가
image_path = "C:/Users/saran/Desktop/your_image.png"
st.image(image_path, caption="Q분류표", use_column_width=True)

st.write("""
Q 표본 분류표를 보시면 -4는 "강한 비동의"를 나타내고, 4는 "강한 동의"를 의미합니다. 
각 숫자에 해당하는 의견을 선택하여 설문에 참여해주세요. 
예를 들어, -4를 선택하면 "강한 불동의", 0을 선택하면 "중립"을 의미합니다. 
""")

# 진술문 리스트
statements = [
       "예술가는 AI의 도움을 받아 새로운 시각과 영감을 얻을 수 있으며, 이는 창의성을 촉진할 수 있다",
    "AI기술과 인간 예술의 융합은 인간의 고유한 창의성을 더 발전시킬 수 있다.",
    "AI 예술은 예술가와 함께 협력하여 예술의 다양성을 향상시킬 수 있다",
    "생성형 AI를 통해 예술가의 노력과 창의성을 반영하면서 관객들에게 새로운 예술 경험을 제공할 수 있다.",
    "예술가와 AI의 협력은 예술과 기술분야 혁신과 발전에 긍정적인 영향을 미칠 수 있다",
    "생성형 AI를 활용하여 학생들이 창의적으로 생각하고 예술적인 표현을 할 수 있는 기회를 제공할 수 있을 것으로 기대된다",
    "생성형 AI도구를 사용한적은 있지만 직접적인 도움이 되진 않았다",
    "AI를 통한 창작물은 빠르게 생성되지만, 그 안에는 인간의 감성과 경험이 담겨 있지 않을 수 있다",
    "AI 예술보다는 인간 예술가의 개성과 경험이 예술작품의 진정한 가치를 결정한다",
    "AI 예술은 예술가의 창의성을 보완할 뿐만 아니라 새로운 예술 형태를 개척할 수 있는 가능성을 제시한다",
    "예술은 인간의 감정과 이야기를 표현하는 것이며, AI가 그것을 대체할 수 없다",
    "생성형 AI가 만든 작품과 인간의 작품은 차이는 있고, 인간의 창작을 뛰어 넘을 수 없다",
    "AI를 사용해 예술 작품을 만든 사람들을 예술가로 받아들이는 것은 안된다",
    "생성형 AI에서 프롬프트(텍스트를 사용한)로 만드는 작품은 예술이 아니다",
    "예술가와 AI의 공존은 없고 예술 분야 창작자들의 직업을 잃을 것이다.",
    "AI에 의한 빠른 작업이 상업 예술 작품의 가치 감소를 일으킬 것이다",
    "생성형 AI을 통한 기존 예술가들의 기법을 답습하는 것은 창작에 대한 심각한 침해이다",
    "생성형 AI로 만든 예술 작품을 구매할 의향이 있다",
    "AI의 발전은 예술 창작을 돕는 훌륭한 도구이고, 기회가 주어진다면 생성형 AI도구를 작품에 사용하고 싶다",
    "생성형 AI를 사용할 수 있지만, 디자이너로써 회사에서 사용하고 싶지는 않다.",
    "생성형 AI를 사용시 배경디자인 같은 반복적인 작업에 사용하는것은 효율적이다",
    "생성형AI와 로봇이 공연하는 음악공연을 가고 싶다",
    "생성형 AI로 만든 미술 전시회에 가서 직접 작품을 구매하고 싶다",
    "생성형 AI를 활용한 예술 교육은 학생들에게 창의성과 기술적 역량을 함께 강화하는 기회가 될 수 있다",
    "생성형 AI을 통한 예술 창작이 전통적인 예술가의 기법을 답습하는것은 상관없다",
    "생성형 AI를 활용하여 다양한 시각과 경험을 제공함으로써 학생들의 창의성을 증진시킬 수 있을 것으로 기대된다",
    "생성형 AI가 예술 교육에 미치는 영향은 신중히 고려되어야 하며, 인간 예술가의 역할과 가치를 지키는 데 중점을 둘 필요가 있다",
    "생성형 AI와 인간 예술가의 창조 과정을 비교하고, 예술교육이  두 가지 접근 방식의 장단점을 이해시키는데 융합하는데 중점을 둘 필요가 있다",
    "AI는 예술가의 창의성을 보완하고 새로운 예술 분야의 직업을 창출하는 데 기여할 것이다.",
    "생성형 AI는 아직 초기 단계이므로 인간의 예술에 미치는 영향은 미미하다",
    "AI가 생성한 이미지에 대한 소유권에 대한 시비는 작품 시장의 미래에 영향을 줄 수 있는 중요한 문제이다"
]

# 강도 선택 제한
limits = {-4: 2, -3: 3, -2: 4, -1: 4, 0: 5, 1: 4, 2: 4, 3: 3, 4: 2}

# Streamlit 앱 시작
def main():
    st.title("생성형 AI와 인간의 창작에 관한 설문조사")

    # 사용자 정보 입력 받기
    email = st.text_input("이메일 주소를 입력하세요:")
    age = st.text_input("나이대를 입력하세요:")
    gender = st.radio("성별을 입력하세요:", ("남성", "여성"))
    occupation = st.radio("창작자인가요? 혹은 일반 직업군인가요?:", ("창작자", "일반 직업군"))
    occupation_specific = st.text_input("본인의 직업은 무엇인가요?:")
    ai_usage = st.radio("생성형 AI를 사용한 적이 있나요?:", ("있음", "없음"))

    # 디렉토리 경로
    save_directory = "C:/Users/Public/Documents/"

    responses = {}  # 사용자의 응답을 저장할 딕셔너리

    # 각 진술문에 대한 체크박스 생성
    for statement in statements:
        st.subheader(statement)
        response_selected = False
        for strength in range(-4, 5):
            if limits[strength] > 0:
                checkbox_label = f"{strength} (강한 비동의)" if strength == -4 else f"{strength} (강한 동의)" if strength == 4 else f"{strength} (중립)" if strength == 0 else str(
                    strength)
                checkbox_key = f"{statement}_{strength}"
                checkbox_value = st.checkbox(checkbox_label, key=checkbox_key)
                if checkbox_value:
                    responses[statement] = strength
                    limits[strength] -= 1
                    response_selected = True
                    break  # 하나의 강도가 선택되면 반복 중단
        if not response_selected:
            responses[statement] = "응답 없음"  # 응답이 없는 경우 처리

    if st.button("설문 제출"):
        # 설문 결과를 판다스 데이터프레임으로 변환
        df_responses = pd.DataFrame(list(responses.items()), columns=['진술문', '응답'])
        df_responses['이메일 주소'] = email
        df_responses['나이대'] = age
        df_responses['성별'] = gender
        df_responses['직업'] = occupation
        df_responses['직업(세부)'] = occupation_specific
        df_responses['생성형 AI 사용 여부'] = ai_usage

        # 엑셀 파일로 저장
        excel_file_path = os.path.join(save_directory, "설문_결과.xlsx")
        df_responses.to_excel(excel_file_path, index=False)
        st.success(f"설문 결과가 성공적으로 저장되었습니다: {excel_file_path}")

if __name__ == "__main__":
    main()
