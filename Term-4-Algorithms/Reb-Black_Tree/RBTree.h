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

    static bool isNull(Node<T> *x);

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
    static Node<T>* tree_min(Node<T> *x);
    static Node<T>* tree_max(Node<T> *x);
    Node<T>* search(Node<T> * root, T key);


    void remove_one(Node<T> *z);
    void deleteFixUp(Node<T> *x);

    void remove(T key);

    void swapColor(Node<T> *x);
    color getColor(Node<T> *x);


    Node<T> * getNewNode(T data);

    class iterator {
    public:
        Node<T> * ptr;

        iterator() {
            ptr = nullptr;
        }

        iterator(Node<T> *x) {
            ptr = x;
        }


        bool operator == (const iterator & it) const{
            if (isNull(this->ptr) && isNull(it.ptr)){
                return true ;
            }
            return this->ptr == it.ptr;
        }


        bool operator != (const iterator & it) const {
            if (isNull(this->ptr) && isNull(it.ptr)){
                return false;
            }
            return this->ptr != it.ptr;
        }


        T& value() {
            return this->ptr->data;
        }


        iterator &operator++() {
            if (!isNull(ptr->right)) {
                ptr = tree_min(ptr->right);
                return *this;
            }
            Node<T> *y = ptr->parent;
            while (!isNull(y) && ptr == y->right) {
                ptr = y;
                y = y->parent;
            }
            ptr = y;
            return *this;

        }


        iterator operator++(int) {

            iterator temp(ptr);

            if (!isNull(ptr->right)) {
                ptr = tree_min(ptr->right);
                return *this;
            }
            Node<T> *y = ptr->parent;
            while (!isNull(y) && ptr == y->right) {
                ptr = y;
                y = y->parent;
            }
            ptr = y;
            return temp;
        }


        iterator &operator--() {
            if (isNull(ptr->left)) {
                ptr = tree_max(ptr->left);
                return *this;
            }
            Node<T> *y = ptr->parent;
            while(!isNull(y) && ptr == y->left) {
                ptr = y;
                y = y->parent;
            }
            ptr = y;
            return *this;
        }


        iterator operator--(int) {

            iterator temp(ptr);
            if (isNull(ptr->left)) {
                ptr = tree_max(ptr->left);
                return *this;
            }
            Node<T> *y = ptr->parent;
            while(!isNull(y) && ptr == y->left) {
                ptr = y;
                y = y->parent;
            }
            ptr = y;
            return temp;
        }
    };


    iterator begin() {
        Node<T> *vrt = root;
        while(vrt && !isNull(vrt->left)){
            vrt = vrt->left;
        }

        return iterator(vrt);
    }


    iterator find(T key) {
        Node<T> * searched = search(this->root, key);
        if (!isNull(searched)) {
            return iterator(searched);
        }
        return end();
    }


    iterator last() {
        Node<T> *vrt = root;
        while(vrt && !isNull(vrt->right)) {
            vrt = vrt->right;
        }
        return iterator(vrt);
    }


    iterator end() {
        return iterator(tree_max(root)->right);
    }
};


#endif //REB_BLACK_TREE_RBTREE_H
