#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;

    int minA, maxA;
    int minB, maxB;

    for (int i = 0; i < a.length(); ++i)
    {
        if (a[i] == '6')
            a[i] = '5';
    }
    minA = stoi(a);
    for (int i = 0; i < a.length(); ++i)
    {
        if (a[i] == '5')
            a[i] = '6';
    }
    maxA = stoi(a);

    for (int i = 0; i < b.length(); ++i)
    {
        if (b[i] == '6')
            b[i] = '5';
    }
    minB = stoi(b);
    for (int i = 0; i < b.length(); ++i)
    {
        if (b[i] == '5')
            b[i] = '6';
    }
    maxB = stoi(b);

    cout << minA + minB << ' ' << maxA + maxB;
    return 0;
}