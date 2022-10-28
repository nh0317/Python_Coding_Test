#include <stdio.h>
int main()
{
	int N, ten = 10, sum = 0, num=10,count=0;
	scanf("%d", &N);
	num = N;
	while (1)
	{
		if (num / 10 > 0) {
			num = num / 10;
			count++;
		}
		else break;
	}

	for (int j = 1; j <= N; j++) {
		if (j % (ten) == 3)
			sum++;
		if (j % (ten) == 6)
			sum++;
		if (j % (ten) == 9)
			sum++;
	}

	for (int i = 1; i <= count; i++)
	{
		for (int j = 1; j <= N; j++) {
			if (j / ten %10 == 3)
				sum++;
			if (j / (ten) % 10 == 6)
				sum++;
			if (j / (ten) % 10 == 9)
				sum++;
		}
		ten *= 10;
	}

	printf("%d", sum);
	return 0;
}