#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

vector<string> split_string(string);
double findMedian(int start,vector<int> arr,int d)
{
    vector<int> a(d,0);
    for(int i=start;i<d;i++)
    {
        a[i] = arr[i];
    }
    int n=d;
    sort(a.begin(),a.end());
    if (n % 2 != 0) 
        return (double) a[start+(n / 2)]; 
  
    return (double)(a[start + ((n - 1) / 2)] + a[start + (n / 2)]) / 2.0; 
}

// Complete the activityNotifications function below.
int activityNotifications(vector<int> expenditure, int f) {
    int start=0;
    int fcount=0;
    int d=f;
           while(d<expenditure.size())
        {
            int temp = expenditure[d];
            double med = findMedian(start,expenditure,d);
            cout << temp << "  " << med << endl;
            if((double)temp>=2*med)
            {
                fcount++;
            }
            start++;d++;
        }
        return fcount;
    }

int main()
{
    int m,n;
    cin >> m >> n;
    vector<int> arr;
    for(int i=0;i<m;i++)
    {
	    cin >> arr[i];
	}
    int result = activityNotifications(arr,n);
    cout << result << endl;
}
