# queue_down_to_zero_2

You are given `Q` queries. Each query consists of a single number `N`. You can perform any of the `2` operations on `N` in each move:

1: If we take 2 integers `a` and `b` where `N = a x b for a <> 1, b <> 1`, , then we can change `N = max(a, b)`

2: Decrease the value of `N` by `1`.

Determine the minimum number of moves required to reduce the value of `N` to `0`.

## Constraints

1 <= Q <= 10^3
0 <= N <= 10^6
