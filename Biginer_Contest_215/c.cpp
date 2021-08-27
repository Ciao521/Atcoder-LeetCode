/*何らかの順列を与えると、
辞書順で次の順列を求める next_permutation 
というアルゴリズムが存在します。
*/
#include<bits/stdc++.h>

using namespace std;

int main(){
  string s;
  int k;
  cin >> s >> k;
  sort(s.begin(),s.end());
  while(k>1){
    next_permutation(s.begin(),s.end());
    k--;
  }
  cout << s << '\n';
  return 0;
}
