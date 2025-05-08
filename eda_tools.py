import pandas as pd
from typing import Union, List, Dict # group_agg에서 필요

# pd.to_datetime 재사용 함수화
def dt_extract(
    df: pd.DataFrame, 
    col: str, # 컬럼 타입이 Object 등 다른 타입이어도 상관 X, col의 인자로 직접적으로 컬럼을 가져오는 것이 아니라, col 인자 문자열로 함수 내부에서 특정 컬럼에 접근할 것이기 때문임.
    attr: str,
    new_col: str
) -> pd.DataFrame: 
    # """
    # 데이터프레임의 특정 컬럼을 datetime 타입으로 변환 후 연도, 월, 일 데이터를 추출해 새로운 컬럼을 만드는 함수
    # col: datetime으로 변환할 컬럼 / attr: dt에서 추출할 데이터 / new_col: 생성할 컬럼 이름 
    # """
    df = df.copy()
    df[col] = pd.to_datetime(df[col])
    df[new_col] = getattr(df[col].dt, attr) # getattr(object, name[, default]) - 객체의 프로퍼티에 동적 접근 가능 / dt의 year, month, day 등 여러 프로퍼티에 필요에 따라 동적으로 접근해야함.

    return df

# 함수 문제점 : datetime으로 변환 후 특정 프로퍼티를 추출하는 케이스가 아닌 경우. 
# year, month, day 모두 추출 필요하거나 / 컬럼 자체를 datetime 변환만 한 후 셀끼리 datetime 단위의 연산 진행할 때


def group_agg(
    df: pd.DataFrame,
    by: Union[str, List[str]],
    agg_dict: Dict[str, Union[str, List[str]]], # dictionary 키 밸류 값 구분에 :가 아니라 , 사용
    reset_index: bool = False
) -> pd.DataFrame:
    # """
    # 그룹화 및 다중 프로퍼티에 대한 연산을 실행하는 함수.
    # by: 그룹화할 컬럼 / agg_dict: key - 연산할 컬럼, value - 컬럼에 진행할 연산방식 / reset_index: True/False로 작동
    # """
    result = df.groupby(by).agg(agg_dict)
    if reset_index:
        result = result.reset_index()
    return result
