#include <iostream>

using namespace std;

int main() {
  int weight;

  cin >> weight;

  if (weight < 0){
    cout << "INVALID INPUT";
  }else if (weight > 7000){
    cout <<"OVERLOADED!!!";
  }else{
    
      /*I forgot this in video but there is a case for 0 weight also */
      
      if (weight == 0 ){
        cout << "Time Estimated : 0 minutes";
      }
      else if (weight < 2000){
        cout << "Time Estimated : 25 minutes";
      }else if (weight < 4001){
        cout << "Time Estimated : 35 minutes";
      }else{
        cout <<"Time Estimated : 45 minutes";
      }

  }

}
