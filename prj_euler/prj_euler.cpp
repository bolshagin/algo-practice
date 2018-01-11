#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <time.h>

using namespace std;

int getMultiples(int n)
{
	/* Problem 1. Find the sum of all the multiples of 3 or 5 below 1000 */
	int sum = 0;
	for (int i = 0; i <= n; i++)
	{
		if ((i % 3 == 0) || (i % 5 == 0))
		{
			sum = sum + i;
		}
	}
	return sum;
}
bool isPalindrome(string str)
{
	/* Return true if string is a palindrome */
	int n = str.length();
	for (int i = 0; i < n / 2; ++i)
	{
		if ((str[i]) != (str[n - i - 1]))
			return false;
	}
	return true;
}
bool isPrime(int n)
{
	if (n == 1)
		return false;
	for (int i = 2; i <= sqrt(n); i++)
		if (n % i == 0)
			return false;
	return true;
}
int sumSquareDifference(double n)
{
	/* Problem 6. Function find the difference between the sum of the squares 
	   of the first N natural numbers and the square of the sum */

	double sumSq = 0;

	int k = 2;
	double coeff = n / 2;
	double sqSum = ((1 + n) / 2) * n;

	for (int iter = 1; iter <= coeff; iter++)
	{
		sumSq = sumSq + 2 * (k - 1) * k;
		k = k + 2;
	}
	
	sumSq = coeff + sumSq;
	cout << fixed << "Difference = " << sqSum * sqSum - sumSq << endl;

	return 0;
}
void find10001Prime()
{
	/* Problem 7. Function find the 10 001st prime number */
	const int N = 1000000;
	int limit = 1001;
	bool prime[N];

	std::cout << "Finds 10001st prime number" << std::endl;

	for (int i = 0; i < N; i++)
		prime[i] = true;

	prime[0] = false;
	int count = 0;

	for (int iter = 2; iter < N; iter++)
	{
		if (prime[iter])
		{
			count++;
			for (unsigned long int j = iter * iter; j < N; j += iter)
				prime[j] = false;
			if (count == limit)
				cout << iter << " is 10001st prime number" << endl;
		}
	}
}
void large13Product()
{
	/* Problem 8. Find the thirteen adjacent digits in the 
	1000-digit number that have the greatest product. */
	string s;
	ifstream file;
	file.open("number.txt");
	getline(file, s);

	vector<int> number(13);
	uint64_t maxProduct = 1;
	uint64_t max = 1;
	uint16_t iter = 0;

	clock_t tStart = clock();
	for (iter = 0; iter <= number.size() - 1; iter++)
	{
		number[iter] = s[iter] - '0';
		maxProduct *= number[iter];
	}

	for (uint16_t i = iter; i <= s.size() - 1; i++)
	{
		number.push_back(s[i] - '0');
		number.erase(number.begin());
		max = 1;
		for (iter = 0; iter <= number.size() - 1; iter++)
			max *= number[iter];
		if (max > maxProduct)
			maxProduct = max;
	}

	cout << "Time: " << (double)(clock() - tStart) / CLOCKS_PER_SEC << " s." << endl;
	cout << "Max of product's: " << maxProduct << endl;
}
void pythagoreanTriple()
{
	/* Problem 9. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc. */
	
	int t = 1000;
	int a = 0, b = 0, c = 0;
	for (int n = 1; n < sqrt(t / 2); n++)
		for (int m = n + 1; m < sqrt(t / 2); m++)
		{
			a = m * m - n * n;
			b = 2 * m*n;
			c = m * m + n * n;
			if (a + b + c == 1000)
			{
				cout << "Pythagorean Triple a = " << a << " b = " << b << " c = " << c << endl;
				cout << "a*b*c = " << a * b * c << endl;
			}
		}

}
void sumPrimeBelow2m()
{
	/* Problem 10. Sum of all the primes below two million. */
	
	int limit = 2000000;
	unsigned long long int sum = 0;
	for (int i = 1; i <= limit; i++)
		if (isPrime(i))
			sum = sum + i;
	cout << "Sum of all the primes below 2 million: " << sum << endl;
}

int main(int argc, _TCHAR* argv[])
{
	return 0;
}