//
// Created by Vladislav Kremenevskiy on 5/20/21.
//

#include <iostream>

#ifndef REB_BLACK_TREE_RBTREE_H
#define REB_BLACK_TREE_RBTREE_H


enum color{
    RED,
    BLACK
};


//template <class T>
class Node {
public:
    int data;
    int key;
    Node *parent;
    Node *left;
    Node *right;
    color color;
};


//template <class T>
class RBTree {
public:
    Node *root;

//    Node* null_node;

    Node * getNullNode(Node * parent);

    bool isNull(Node *x);

    RBTree();

    void preOrder(Node * node);
    void inOrderLeft(Node * node);
    void inOrderRight(Node * node);
    void postOrder(Node * node);



    void leftRotate(Node *x);
    void rightRotate(Node *x);
    void insert(int key);
    void insertNode(Node *x);
    void insertFixUp(Node *x);



    void transplant(Node *u, Node *v);
    Node* tree_min(Node *x);
    Node* tree_max(Node *x);
    Node* search(Node * root, int key);


    void remove_one(Node *z);
    void deleteFixUp(Node *x);

    void remove(int key);

    void swapColor(Node *x);
    color getColor(Node *x);


    Node * getNewNode(int data);

};


#endif //REB_BLACK_TREE_RBTREE_H
