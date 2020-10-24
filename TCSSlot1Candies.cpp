#include <iostream>

using namespace std;

int main() {
  int candiesOrder;
  int N = 10;
  int K = 5;

  cin >> candiesOrder;

  //for invalid input 
  if (candiesOrder <=0 || candiesOrder > N){
    cout << "INVALID INPUT" <<endl;
    cout << "NUMBER OF CANDIES AVAILABLE: "<<N;
    return 0;
  }

  // int candiesSold = candiesOrder;

  cout << "Number of candies sold: " << candiesOrder <<endl;
  
  if ((N - candiesOrder) <= K){
    cout << "NUMBER OF CANDIES AVAILABLE: "<<N;
  }
  else{
    cout << "NUMBER OF CANDIES AVAILABLE: "<<N - candiesOrder;
  }

  return 0;




}