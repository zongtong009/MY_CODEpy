import numpy as np


def solve_question(trials):
    # range to search in
    probability_range = np.array([0.0, 1.0])
    while True:
        # prob. to see car in 10 minutes
        probability_10min = probability_range.mean()  # =0.5单值
        # .mean() 平均值

        # simulate three 10-minute intervals
        events = np.random.rand(trials, 3) < probability_10min
        # ＜0.5的bool值
        events = np.sum(events, axis=1) > 0   # 有1为1，即或运算
        # prob. to see car in 30 minutes
        probability_30min = np.mean(events)
        i = 0 if probability_30min < .95 else 1
        probability_range[i] = probability_10min
        if abs(probability_30min - .95) < 1e-4:
            return probability_10min


solve_question(5)


# def main():
#     solve_question(10**6)


# if __name__ == "__main__":
#     main()
