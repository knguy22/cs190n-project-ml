from features import FINAL_MODEL
from sklearn.metrics import classification_report
import pandas as pd
import pickle

def main():
    df_test = pd.read_pickle('validation_2.pkl')
    with open('resolution_rf_all_FINAL_MODEL_FUZZY_time10_model.pkl', 'rb') as file:
        res_model = pickle.load(file)

    conditions = get_conditions(df_test)
    for cond in conditions:
        eval_cond(df_test, cond, res_model)

# follow 480 tree
# def get_conditions(df):
#     conds = [pd.Series([True] * len(df), index=df.index)]
#     conds.append(conds[-1] & (df['10_chunksizes_85'] > 321531.219))
#     conds.append(conds[-1] & (df['allprev_chunksizes_50'] > 17477.5))
#     conds.append(conds[-1] & (df['allprev_avg_chunksize'] <= 1276703.875))
#     conds.append(conds[-1] & (df['allprev_min_chunksize'] <= 5566.0))
#     conds.append(conds[-1] & (df['allprev_std_chunksize'] <= 546532.969))
#     return conds

# follow 240 tree
# def get_conditions(df):
#     conds = [pd.Series([True] * len(df), index=df.index)]
#     conds.append(conds[-1] & (df['10_chunksizes_85'] <= 321531.219))
#     conds.append(conds[-1] & (df['n_prev_up_chunk'] > 15.5))
#     conds.append(conds[-1] & (df['allprev_std_chunksize'] > 423413.844))
#     # conds.append(conds[-1] & (df['service_Video_throughput_down'] <= 610.264))
#     return conds

# 360
# def get_conditions(df):
#     conds = [pd.Series([True] * len(df), index=df.index)]
#     conds.append(conds[-1] & (df['10_chunksizes_85'] <= 321531.219))
#     conds.append(conds[-1] & (df['n_prev_up_chunk'] <= 15.5))
#     return conds

def get_conditions(df):
    conds = [pd.Series([True] * len(df), index=df.index)]
    # conds.append(conds[-1] & (df['10_chunksizes_85'] > 321531.219))
    # conds.append(conds[-1] & (df['allprev_chunksizes_50'] > 17477.5))
    # conds.append(conds[-1] & (df['allprev_max_chunksize'] <= 1935595.5))
    conds.append(conds[-1] & (df['allprev_max_chunksize'] <= 1276703.875))
    # conds.append(conds[-1] & (df['service_Video_throughput_down'] <= 610.264))
    return conds

def eval_cond(df_test, cond, model):
    df_test = filter(df_test, cond)
    features_test = df_test[FINAL_MODEL]
    expected_test_res = df_test['resolution']

    y_pred = model.predict(features_test)
    print(df_test.shape)
    print(classification_report(expected_test_res, y_pred, zero_division=0))
    print()

def filter(df, cond):
    return df[cond]

main()