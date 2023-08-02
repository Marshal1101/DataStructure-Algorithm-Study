def cake(ax, ay, az, bx, by, bz):
    return (az + bx, ay * by, ax + bz)

def main():
    ax, ay, az = map(int, input().split())
    cx, cy, cz = map(int, input().split())
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if cake(ax, ay, az, i, j, k) == (cx, cy, cz):
                    print(i, j, k)
                    return

if __name__ == '__main__':
    main()


# a,b,c = map(int,input().split())
# n,m,l = map(int,input().split())

# print(n-c,int(m/b),l-a)