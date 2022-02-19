#include <iostream>
int a = 0;
void main() {
	using namespace std;
	while (true) {
		a++;
		//cout << a;
		//cout << "\n";
		if (a == 10000000000000000) {
			cout << a;
			break;
		}
	}
}