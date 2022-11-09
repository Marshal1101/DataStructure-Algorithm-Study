#include <iostream>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <climits>
#define FASTIO cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
#define MAX 1000001
#define LL long long
#define INF 1e9

using namespace std;
int N;
LL MAP[MAX];
vector<int> SegTree;
LL answer = 0;

// Inversion Counting

void Init() {
	int Tree_Height = (int)ceil(log2(N));
	int Tree_Size = (1 << (Tree_Height + 1));
	SegTree.resize(Tree_Size);
}

void Update_SegTree(int Node, int S, int E, LL Val, LL Diff) {
	if (S == E) {
		SegTree[Node] += Diff;
		return;
	}
	int M = (S + E) / 2;
	if (Val <= M) {
		Update_SegTree(Node * 2, S, M, Val, Diff);
	}
	else {
		Update_SegTree(Node * 2 + 1, M + 1, E, Val, Diff);
	}
	SegTree[Node] = SegTree[Node * 2] + SegTree[Node * 2 + 1];
}

LL Find_Value(int Node, int S, int E, int Left, int Right) {
	if ((S > Right) || (Left > E)) {
		return 0;
	}
	if ((Left <= S) && (E <= Right)) {
		return SegTree[Node];
	}
	int M = (S + E) / 2;
	return Find_Value(Node * 2, S, M, Left, Right) + Find_Value(Node * 2 + 1, M + 1, E, Left, Right);
}

void Find_Answer() {
	cin >> N;
	Init();
	for (int i = 1; i <= N; i++) {
		int X;
		cin >> X;
		answer += (X - 1) - Find_Value(1, 1, N, 1, X - 1);
		Update_SegTree(1, 1, N, X, 1);
	}
	cout << answer << "\n";
}

int main() {
	FASTIO
	Find_Answer();

	return 0;
}