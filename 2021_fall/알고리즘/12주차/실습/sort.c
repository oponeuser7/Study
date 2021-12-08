#include <stdio.h>
#include <stdlib.h>

void solve(char ans[], char graph[][26], char pre[], char check[]) {
	char* ansPtr = ans;
	char* queue = malloc(200);
	char* front = queue;
	char* rear = front;
	for(int i=0; i<26; i++) {
		if(pre[i]==0 && check[i]) {
			*rear = i;
			rear++;
		}
	}
	while(front!=rear) {
		char temp = *front;
		front++;
		*ansPtr = (char)temp+65;
		ansPtr++;
		for(int i=0; i<26; i++) {
			if(graph[temp][i]) {
				pre[i]--;
				if(pre[i]<=0) {
					*rear = i;
					rear++;
				}
			}
		}
	}
}

int main() {
	int n, m;
	char a, b;
	scanf("%d %d", &n, &m);
	char graph[26][26] = {0, };
	char pre[26] = {0, };
	char check[26] = {0, };
	for(int i=0; i<m; i++) {
		scanf("%c %c", &a, &b);
		graph[a-65][b-65] = 1;
		pre[b-65]++;
		check[a-65] = 1;
		check[b-65] = 1;
		getchar();
	}
	char* ans = malloc(n);
	solve(ans, graph, pre, check);
	for(int i=0; i<n; i++) {
		printf("%c ", *ans);
		ans++;
	}
	return 0;
}
	

