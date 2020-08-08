from bisect import bisect_left

P = 10 ** 9 + 7


def main():
    T = int(input())
    for _test_case in range(T):
        N, M, K = map(int, input().split())
        A = list(map(int, input().split()))
        assert len(A) == N
        print(count(A, K, M) % P)


def count(arr, limit, arr_copies):
    sums = [0]
    for x in arr:
        sums.append(x + sums[-1])
    total = sums[-1]

    num_copies, remainder = divmod(limit, total)
    if num_copies >= arr_copies:
        n = arr_copies * len(arr)
        return n * (n + 1) // 2

    result = 0
    for j in range(1, len(sums)):
        sum_j = sums[j]
        num_copies_j = num_copies
        if remainder >= sum_j:
            num_copies_j += 1

        assert num_copies_j * total + sum_j > limit
        assert (num_copies_j - 1) * total + sum_j <= limit

        if num_copies_j > 0:
            add = num_copies_j * (j * 2 + (num_copies_j - 1) * len(arr)) / 2
            assert add.is_integer()
            result += int(add)

        i = bisect_left(sums, num_copies_j * total + sum_j - limit)
        assert 0 < i <= len(arr)

        result += (arr_copies - num_copies_j) * (num_copies_j * len(arr) + j - i)
    return result


main()