import numpy as np
import pandas as pd


def build_histogram(sample, equidistand=True, bins=None):
    k = bins
    n = len(sample)
    M = None
    if k is None:
        if n <= 100:
            k = int(np.sqrt(n))
        else:
            k = 1 + int(3.322 * np.log10(n))

    hist = pd.DataFrame(columns=['Ai', 'Bi', 'v', 'hi', 'fi', 'mid', 'nums'])
    x_1, x_n = sample[0] - 0.00001, sample[-1] + 0.00001
    h = (x_n - x_1) / k

    def get_new_A_equdist(i):
        return x_1 + (i - 1) * h

    def get_new_A_not_equdist(i, prev_segment):

        if i == 1:
            return x_1
        left_border, right_border = prev_segment, None
        segment = intervals / k
        if i == 2:
            left_border = 0
        right_border = left_border + segment
        diff_part = right_border - int(right_border)
        index_for_B = int(right_border)
        B = (sample[index_for_B + 1] - sample[index_for_B]) * diff_part + sample[index_for_B]

        return B, right_border

    if equidistand:


        iter = 0
        saved_for_next = 0
        for i in range(1, k + 1):
            A = get_new_A_equdist(i)
            B = get_new_A_equdist(i + 1)
            mid = (B + A) / 2

            v = saved_for_next  # frequency
            saved_for_next = 0
            nums = []
            while (iter < n) and (sample[iter] <= B):
                nums.append(sample[iter])
                if sample[iter] == B:
                    v += 0.5
                    saved_for_next += 0.5
                else:
                    v += 1
                iter += 1

            if iter == n-1:
                v += saved_for_next

            fi = v / n
            hist.loc[i] = [A, B, v, h, fi, mid, nums]

        return hist

    else:
        if bins > n - 1:
            if n <= 100:
                k = int(np.sqrt(n))
            else:
                k = 1 + int(3.322 * np.log10(n))
        intervals = n-1
        segments = intervals / k
        prev_segment = None
        A, B = None, None
        iter = 0
        for i in range(1, k + 1):
            if i == 1:
                A = get_new_A_not_equdist(1, None)
            else:
                A = B
            if i == k:
                B = x_n
            else:
                B, prev_segment = get_new_A_not_equdist(i+1, prev_segment)

            h = B - A
            mid = (A + B) / 2
            v = 0
            nums = []
            while (iter < n) and (sample[iter] < B):
                nums.append(sample[iter])
                v += 1
                iter += 1

            fi = v / n
            hist.loc[i] = [A, B, v, h, fi, mid, nums]
            print(hist)

        return hist


if __name__ == '__main__':
    hist = build_histogram([1, 2, 8, 10, 11, 12], equidistand=False, bins=2)



