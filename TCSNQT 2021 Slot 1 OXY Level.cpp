#include <iostream>

using namespace std;

int main() {

      int oxygen[9];

      for ( int i = 0 ; i < 9 ; i++){
        int oxyVal;
        cin >> oxyVal;

        if (oxyVal <=0 || oxyVal > 100){
          continue;
        }

        oxygen[i] = oxyVal;
      }

      //Our oxygen values are ready 
      //0, 3, 6 - 1st trainees
      //1, 4, 7 -  2nd trainee 
      //2, 5, 8 - 3rd trainee

      int t1_avg = (oxygen[0] + oxygen[3] + oxygen[6]) /3;
      int t2_avg = (oxygen[1] + oxygen[4] + oxygen[7]) /3;
      int t3_avg = (oxygen[2] + oxygen[5] + oxygen[8]) /3;

      int max_val = 0;
      //compare to get max 
      if ( t1_avg > t2_avg){
          if (t1_avg > t3_avg)
              max_val = t1_avg;
          else {
            max_val = t3_avg ; 
          }
      }else{
        if (t2_avg > t3_avg)
            max_val = t2_avg;
        else
          max_val = t3_avg ; 
      }

      if ( max_val < 70 ){
        cout << "All trainees are unfit.";
        return 0 ;
      }

      //Trainee names 
      if (t1_avg == max_val)
        cout << "Trainee Number : 1" << endl;
      if (t2_avg == max_val)
        cout << "Trainee Number : 2"<< endl;
      if (t3_avg == max_val)
        cout << "Trainee Number : 3"<< endl;

      cout << "Highest Oxygen Level : " <<max_val;

      return 0;



  }
