def generate_schedule(n, m):
    # Choose a length `l` that is always the same for all shows, which can be `m`.
    l = max(min((m - n), m // n + 1) * n, 2)
    t = l * m // n
    # Output the length of all shows
    print(l)
    arr = [0] * n

    j = 0
    
    # Create a schedule for the given number of singers `n` and show length `l`
    for i in range(m):
        a = min(l, t - arr[j])
        arr[j] += a
        k = j
        if a < l:
            j += 1
            b = min(l - a, t - arr[j])
            arr[j] += b
        else:
            b = 0

        # We schedule each singer to perform for the full length `l`
        print(f"{a} {k+1} {b} {j+1}")

def main():
    import sys
    t = int(input())

    for _ in range(t):
        data = input().split()
        n = int(data[0])
        m = int(data[1])

        generate_schedule(n, m)


if __name__ == "__main__":
    main()

# SEKAI{t1nyURL_th1s:_6d696b75766d}