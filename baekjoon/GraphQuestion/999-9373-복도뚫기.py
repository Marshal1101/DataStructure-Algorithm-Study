import sys


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        W = int(input())
        N = int(input())
        horizon_min = W
        sensers = []
        
        for _ in range(N):
            x, y, r = map(int, input().split())
            sensers.append((x, y, r ))
            if 0 < x - r < horizon_min:
                horizon_min = x - r
            if x + r < W and W - (x+r) < horizon_min:
                horizon_min = W - x - r
            dist_min = sys.maxsize
            for px, py, pr in sensers:
                dist = ((x - px)**2 + (y - py)**2)**(1/2) - r - pr
                dist_min = dist if dist < dist_min else dist_min
