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


template <class T>
class Node {
public:
    T data;
    T key;
    Node<T> *parent;
    Node<T> *left;
    Node<T> *right;
    color color;
};


template <class T>
class RBTree {
public:
    Node<T> *root;

//    Node* null_node;

    Node<T> * getNullNode(Node<T> * parent);

    bool isNull(Node<T> *x);

    RBTree();

    void preOrder(Node<T> * node);
    void inOrderLeft(Node<T> * node);
    void inOrderRight(Node<T> * node);
    void postOrder(Node<T> * node);



    void leftRotate(Node<T> *x);
    void rightRotate(Node<T> *x);
    void insert(T key);
    void insertNode(Node<T> *x);
    void insertFixUp(Node<T> *x);



    void transplant(Node<T> *u, Node<T> *v);
    Node<T>* tree_min(Node<T> *x);
    Node<T>* tree_max(Node<T> *x);
    Node<T>* search(Node<T> * root, T key);


    void remove_one(Node<T> *z);
    void deleteFixUp(Node<T> *x);

    void remove(T key);

    void swapColor(Node<T> *x);
    color getColor(Node<T> *x);


    Node<T> * getNewNode(T data);

};


#endif //REB_BLACK_TREE_RBTREE_H
