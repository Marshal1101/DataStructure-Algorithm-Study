N = int(input())
# l = 4n - 3
def makestar(N):
    ans = ""
    for k in range(N-1):
        ans += "* "*k + "*" * (4*(N-k)-3) + " *"*k
        ans += "\n"
        ans += "* "*(k+1) + " "*(4*(N-1-k)-3) + " *"*(k+1)
        ans += "\n"

    ans += "* "*(N-1) + "*" + " *"*(N-1) + "\n"

    for k in range(N-2, -1, -1):
        ans += "* "*(k+1) + " "*(4*(N-1-k)-3) + " *"*(k+1)
        ans += "\n"
        ans += "* "*k + "*" * (4*(N-k)-3) + " *"*k
        ans += "\n"

    print(ans)


makestar(N)