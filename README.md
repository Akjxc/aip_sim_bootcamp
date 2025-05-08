# AIP_SIM_BOOTCAMP

# Palantir AIP 학습 커리큘럼 v3 (현실 생존형 버전)

## 개요

- **목표**: 실제 AIP 접근 없이도 Ontology, Workflow, Agent 개념 체득 및 실습 중심 학습 진행
- **기간**: 약 12주
- **전략**: 실습은 최소한으로, 개념 체험 중심 / 당직 여부에 따른 유연 학습

---

## Phase 0: Palantir AIP 개념 뇌에 심기 (1주)

- **목표**: AIP 구조와 철학 이해
- **활동**
    - [build.palantir.com](http://build.palantir.com/) 문서 탐색
    - [https://www.palantir.com/docs](https://www.palantir.com/docs) → 여기가 유의미한듯
    - AIP/Foundry 데모 영상 시청
    - 블로그 및 소개 자료 정리
- **성과물**
    - 핵심 키워드 5개 요약 (Ontology, Workflow, Agent 등)
    - UI 흐름 노트

---

## Phase 1: Python & Pandas 복습 (1주) - (완료)

- **목표**: 데이터 전처리 감각 회복
- **활동**
    - Kaggle Pandas mini-course 실습
    - 결측치, 그룹화, 인코딩 등 실전 위주 처리
- **성과물**
    - 전처리 실습 노트북 1개
    - EDA 함수 1~2개 정리

---

## Phase 1.5: 데이터 시각화 퀵패스 (2~3일) - (진행중)

- **목표**: 시각화의 쓰임새 체감
- **활동**
    - Kaggle Data Visualization mini course 실습 - (완료)
    - Titanic 등으로 질문형 분석 후 시각화
- **성과물**
    - 시각화 예제 5개 + 한줄 해석
    - EDA notebook 1개

---

## Phase 2: 머신러닝 기본기 체험 (2주)

- **목표**: 모델링 흐름 이해
- **활동**
    - Scikit-learn 사용 (로지스틱/랜덤포레스트)
    - 학습 → 예측 → 평가 → 시각화(Optional)
- **성과물**
    - ML 실습 노트북 2개
    - 주요 개념 요약 정리 (과적합, 지표 등)

---

## Phase 3: AIP 구조 체험 미니 시뮬레이션 (3주)

- **목표**: AIP 구조 개념의 간이 구현
- **활동**
    - pandas/json 기반 Ontology 설계
    - LangChain Tool + Agent 구성
    - Streamlit으로 간단 UI 구축
- **선택 모듈 (고급)**
    - **LlamaIndex 적용 (RAG 기반 질의응답)**
    - **Ontology JSON 구조 설계 및 정의 작성**
- **성과물**
    - AIP 미니 시뮬레이션 앱 (입력 → 응답 흐름)
    - 구조 설명 Markdown 문서

---

## Phase 4: 실무형 AIP 스타일 프로젝트 (3~4주)

- **목표**: 실전형 시뮬레이션 프로젝트 구현
- **활동**
    - Kaggle 데이터 기반 문제 정의
    - 데이터 → 모델링 → 결과 → Agent → UI 흐름 구현
    - Streamlit + LangChain 통합
    - 문서화 + 기능 설명
- **선택 모듈 (고급)**
    - **Palantir 데모 UI 벤치마킹**
    - **유사 워크플로우 흐름 구성**
- **성과물**
    - 완성된 프로젝트 앱
    - 사용법/구조 요약 문서

---

## Phase X: 아낌없이 주는 문서 (0.5주 병행)

- **활동**
    - 전체 개념/코드 요약 정리 (Notion or GitHub)
    - 면접용 스크립트 작성 (Agent 설계, Ontology 활용 등)
- **성과물**
    - 마크다운 요약 문서
    - 사용 사례 기반 설명 정리

---

## 추천 학습 루틴 (상황 기반)

| 컨디션 | 추천 학습 |
| --- | --- |
| 당직 날 | 문서 탐색, 블로그 정리, 영상 시청 |
| 비당직 날 | 실습 및 프로젝트 구현 중심 |
| 중간 컨디션 | 시각화, 코드 리팩터링, 아이디어 정리 |

---

## 선택 모듈 요약 (시간 여유 시 추가)

| 모듈 | 설명 | 기간 |
| --- | --- | --- |
| LlamaIndex | 문서 기반 질의응답 RAG 흐름 체험 | 2~3일 |
| Ontology 설계 | 간단 JSON 모델링 + 관계 정의 | 1일 |
| AIP UI 흐름 리버스 엔지니어링 | 데모 UI 분석 후 유사 흐름 Streamlit 구현 | 1~2일 |

---

## 최종 목표

- AIP의 개념과 구조를 스스로 설명할 수 있다.
- LangChain, Streamlit 등으로 유사 구조를 직접 만들어봤다.
- 데이터 처리, 모델링, 흐름 설계까지 연결한 경험을 문서화했다.
