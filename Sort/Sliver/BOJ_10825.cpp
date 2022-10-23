#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
class Student
{
public:
	string name;
	int kor;
	int eng;
	int math;

	Student(string name, int kor, int eng, int math)
	{
		this->name = name;
		this->kor = kor;
		this->eng = eng;
		this->math = math;
	}

	bool operator <(Student& other)
	{
		if (this->kor == other.kor && this->eng == other.eng && this->math == other.math)
			return this->name < other.name;
		if (this->kor == other.kor && this->eng == other.eng)
			return this->math > other.math;
		if (this->kor == other.kor)
			return this->eng < other.eng;

		return this->kor > other.kor;
	}
};

vector <Student> s;

int main()
{
	cin >> n;
	while (n--)
	{
		string str;
		int k, e, m;
		cin >> str >> k >> e >> m;

		s.push_back(Student(str, k, e, m));
	}

	sort(s.begin(), s.end());

	for (int i = 0; i < s.size(); ++i)
		cout << s[i].name << '\n';

	return 0;
}