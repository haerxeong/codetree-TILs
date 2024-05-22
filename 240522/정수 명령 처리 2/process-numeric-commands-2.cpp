#include <iostream>
#include <string>

using namespace std;

class Queue {
private:
    int q[5];
    int front, rear;

public:
    Queue();
    ~Queue();

    void push(int a);
    int pop();
    int size();
    bool empty();
    int _front();
};

Queue::Queue() : q{}, front(-1), rear(-1) {}

Queue::~Queue() {}

void Queue::push(int a) {
    if (rear == 4) {
        cout << "Queue is full" << endl;
        return;
    }
    if (empty()) {
        front = 0;
    }
    q[++rear] = a;
}

int Queue::pop() {
    if (empty()) {
        cout << "Queue is empty" << endl;
        return -1;
    }
    int value = q[front];
    if (front == rear) {
        front = rear = -1; // Reset queue if it becomes empty
    } else {
        front++;
    }
    return value;
}

int Queue::size() {
    if (empty()) return 0;
    return rear - front + 1;
}

bool Queue::empty() {
    return front == -1;
}

int Queue::_front() {
    if (empty()) {
        cout << "Queue is empty" << endl;
        return -1;
    }
    return q[front];
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
        } else if (input == "pop") {
            cout << q.pop() << endl;
        } else if (input == "size") {
            cout << q.size() << endl;
        } else if (input == "empty") {
            cout << (int)q.empty() << endl;
        } else if (input == "front") {
            cout << q._front() << endl;
        }
    }

    return 0;
}