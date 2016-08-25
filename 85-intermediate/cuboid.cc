#include <iostream>
using namespace std;

class Cuboid {
    
private:
    int _length;
    int _height;
    int _depth;

public:

    Cuboid(int l, int h, int d) {
        set_length(l);
        set_height(h);
        set_depth(d);
    }
    
    void set_length(int l) {
        _length = l;
    }
    
    void set_height(int h) {
        _height = h;
    }
    
    void set_depth(int d) {
        _depth = d;
    }
    
    int length() {
        return _length;
    }
    
    int height() {
        return _height;
    }
    
    int depth() {
        return _depth;
    }
    
    void print() {
        
        // Print top
        for (int i = 0; i < depth(); i++) {
            cout << std::string((depth() - i), ' ');
            cout << std::string(length(), ':');
            cout << '/';
            cout << std::string(i, '+') << endl;
        }
        
        // Print front view
        for (int i = 0; i < height() - depth(); i++) {
            cout << std::string((length()), '#');
            cout << std::string((depth()), '+') << endl;
        }
        
        // Print bottom
        for (int i = 0; i < depth(); i++) {
            cout << std::string((length()), '#');
            cout << std::string((depth() - 1 - i), '+') << endl;
        }
    }
    
};

int main() {
    int l, h, d;
    cin >> l >> h >> d;
    Cuboid cube(l, h, d);
    cube.print();
    return 0;
}