#include <iostream>
#include <vector>

int main() {
    std::vector<long int> doubles;
    
    for (int x = 1; x < 10000000; ++x) {
        doubles.push_back(x * 2);
    }
    
    // Printing all elements (note: this will print 10 million numbers!)
    for (const auto& num : doubles) {
        std::cout << num << " ";
    }
    
    return 0;
}