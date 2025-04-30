#include <iostream>

int main(){
    int count;
    std::cout << "enter: ";
    
    std::cin >> count;

    for(int i = 0; i < count; i++ ){
        std::cout << i << '\n';
    }

    return 0;
}