#include <iostream>
#include <string>

using namespace std;

class Queue {
private:
    int q[10];
    int front, rear;

public:
    Queue();
    void push(int a);
    int pop();
    int size();
    bool empty();
    int _front();
};

Queue::Queue() : q{}, front(-1), rear(-1) {}

void Queue::push(int a) {
    q[++rear] = a;
}

int Queue::pop() {
    return q[++front];
}

int Queue::size() {
    return rear - front;
}

bool Queue::empty() {
    return front == rear;
}

int Queue::_front() {
    return q[front + 1];
}

int main() {
    Queue q;
    int n, x;
    string input;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> input;
        if (input == "push") {
            cin >> x;
            q.push(x);
        } 
        else if (input == "pop") {
            cout << q.pop() << endl;
        } 
        else if (input == "size") {
            cout << q.size() << endl;
        } 
        else if (input == "empty") {
            cout << (int)q.empty() << endl;
        } 
        else if (input == "front") {
            cout << q._front() << endl;
        }
    }
    return 0;
}