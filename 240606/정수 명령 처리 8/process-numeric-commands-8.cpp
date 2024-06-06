#include <iostream>
#include <string>
using namespace std;

class Node {
private:
    int data;
    Node* prev;
    Node* next;

public:
    Node(int data) : data(data), prev(nullptr), next(nullptr) {}
    int getData() { return data; }
    Node* getNext() { return next; }
    Node* getPrev() { return prev; }
    void setNext(Node* node) { next = node; }
    void setPrev(Node* node) { prev = node; }
};

class DoublyList {
private:
    Node head;
    int listSize;

public:
    DoublyList() : head(0), listSize(0) {}

    Node* getHead();
    bool isEmpty();
    int size();
    int getEntry(int pos);
    void insert(int pos, const int data);
    Node* rmv(int pos);
};

Node* DoublyList::getHead() {
    return head.getNext();
}

bool DoublyList::isEmpty() {
    return listSize == 0;
}

int DoublyList::size() {
    return listSize;
}

int DoublyList::getEntry(int pos) {
    Node* current = getHead();
    for (int i = 0; i < pos; i++)
        current = current->getNext();

    return current->getData();
}

void DoublyList::insert(int pos, const int data) {
    Node* newNode = new Node(data);
    Node* prev = &head;
    for (int i = 0; i <= pos - 1; i++)
        prev = prev -> getNext();
    newNode -> setPrev(prev);
    newNode -> setNext(prev -> getNext());
    if (prev -> getNext() != nullptr) (prev -> getNext())-> setPrev(newNode);
    prev -> setNext(newNode);

    ++listSize;
}

Node* DoublyList::rmv(int pos) {
    Node* removedNode = nullptr;
    Node* prev = &head;
    for (int i = 0; i <= pos - 1; i++)
        prev = prev -> getNext();
    
    removedNode = prev -> getNext();
    if (prev != nullptr) prev -> setNext(removedNode -> getNext());
    if (prev -> getNext() != nullptr) (prev -> getNext()) -> setPrev(prev);
    removedNode -> setNext(nullptr);
    removedNode -> setPrev(nullptr);

    --listSize;
    
    return removedNode;
}

int main()
{
    int n, x;
    string s;
    DoublyList list;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> s;
        if (s == "push_back") {
            cin >> x;
            list.insert(list.size(), x);
        }
        else if (s == "push_front") {
            cin >> x;
            list.insert(0, x);
        }
        else if (s == "pop_back") cout << list.rmv(list.size() - 1) -> getData() << endl;
    
        else if (s == "pop_front") cout << list.rmv(0) -> getData() << endl;
        
        else if (s == "size") cout << list.size() << endl;

        else if (s == "empty") cout << (int) list.isEmpty() << endl;

        else if (s == "front") cout << list.getEntry(0) << endl;

        else if (s == "back") cout << list.getEntry(list.size() - 1) << endl;
    }
    return 0;
}