#include <iostream>
using namespace std;

int main(){

    float a,b,hasil;
    char operator_matematika;

    cout << "Selamat datang di program kalkulator sederhana c++ \n \n";

    //memasukan input angka dari user
    cout << "Masukan nilai pertama : ";
    cin >> a;
    cout << "Pilihlah Operator ( + , - , * , / ) : ";
    cin >> operator_matematika;
    cout << "Masukan nilai kedua : ";
    cin >> b;

    if (operator_matematika == '+')
    {
        hasil = a + b;
    }
    else if (operator_matematika == '-')
    {
        hasil = a - b;
    }
    else if (operator_matematika == '*')
    {
        hasil = a * b;
    }
    else if (operator_matematika == '/')
    {
        hasil = a / b;
    }
    cout << "\nHasil perhitungan " << a << operator_matematika << b << " = " << hasil << endl;

    cin.get();
    return 0;
}