//
// Created by Vladislav Kremenevskiy on 5/20/21.
//

#include "RBTree.h"


Node *RBTree::getNewNode(int data) {
    Node * newNode = new Node;
    newNode->color = RED;
    newNode->data = data;
    newNode->key = data;
    newNode->right = newNode->left = nullptr;
    newNode->parent = nullptr;
    return newNode;
}


bool RBTree::isNull(Node *x) {
    if (x->right == nullptr && x->left == nullptr) {
        return true;
    }
    return false;
}

Node *RBTree::getNullNode(Node *parent) {
    Node *newNullNode = new Node;
    newNullNode->color = BLACK;
    newNullNode->data = newNullNode->key = 0;
    newNullNode->right = newNullNode->left = nullptr;
    newNullNode->parent = parent;
    return newNullNode;
}


color RBTree::getColor(Node *x) {
    if (isNull(x))
        return BLACK;

    if (x->color == BLACK)
        return BLACK;

    return RED;
}


RBTree::RBTree() {
//    null_node->color = BLACK;
//    null_node->left = null_node->right = nullptr;
//    null_node->key = null_node->data = 0;
    root = getNullNode(nullptr);

}


void RBTree::preOrder(Node *node) {
    if (!isNull(node)){
        std::cout << node->data << ' ';
        preOrder(node->left);
        preOrder(node->left);
    }
}


void RBTree::inOrderLeft(Node *node) {
    if (!isNull(node)) {
        inOrderLeft(node->left);
        std::cout << node->data << ' ';
        inOrderLeft(node->right);
    }
}


void RBTree::inOrderRight(Node *node) {
    if (!isNull(node)) {
        inOrderRight(node->right);
        std::cout << node->data << ' ';
        inOrderRight(node->left);
    }
}


void RBTree::postOrder(Node *node) {
    if (!isNull(node)) {
        postOrder(node->left);
        postOrder(node->right);
        std::cout << node->data << ' ';
    }
}


void RBTree::leftRotate(Node *x) {
    Node *y = x->right;
    x->right = y->left;

    if (!isNull(y->left)){
        y->left->parent = x;
    }

    y->parent = x->parent;

    if (isNull(x->parent)) {
        root = y;
    }
    else if (x == x->parent->left){
        x->parent->left = y;
    }
    else {
        x->parent->right = y;
    }
    y->left = x;
    x->parent = y;
}

void RBTree::rightRotate(Node *x) {
    Node *y = x->left;
    x->left = y->right;

    if (!isNull(y->right)) {
        y->right->parent = x;
    }


    y->parent = x->parent;
    if (isNull(x->parent)) {
        root = y;
    }
    else if (x == x->parent->right){
        x->parent->right = y;
    }
    else {
        x->parent->left = y;
    }
    y->right = x;
    x->parent = y;
}


void RBTree::insertFixUp(Node *z) {
    if (!z->parent){
        z->color = BLACK;
        return;
    }
    while(!isNull(z->parent) && getColor(z->parent) == RED) {
        if (z->parent == z->parent->parent->left) {
            Node *uncle = z->parent->parent->right;


            // uncle is red
            if (getColor(uncle) == RED) {
                z->parent->color = BLACK;
                uncle->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            }
            else{ // uncle is black
                if (z == z->parent->right) { // make them to one line
                    z = z->parent;
                    leftRotate(z);
                }
                // rotate to make height less
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                rightRotate(z->parent->parent);
            }
        }
        else{
            Node *uncle = z->parent->parent->left;

            if (getColor(uncle) == RED) {
                z->parent->color = BLACK;
                uncle->color = BLACK;
                z->parent->parent->color = RED;
                z = z->parent->parent;
            }
            else {
                if (z == z->parent->left){
                    z = z->parent;
                    rightRotate(z);
                }
                z->parent->color = BLACK;
                z->parent->parent->color = RED;
                leftRotate(z->parent->parent);
            }
        }
    }
    root->color = BLACK;
}


void RBTree::insertNode(Node *z) {
    Node * y = getNullNode(nullptr);
    Node * x = root;
    while(!isNull(x)) {
        y = x;
        if (z->key < x->key) {
            x = x->left;
        }
        else{
            x = x->right;
        }
    }
    z->parent = y;

    if (isNull(y)) {
        root = z;
    }
    else if (z->key < y->key){
        y->left = z;
    }
    else {
        y->right = z;
    }

    z->left = z->right = getNullNode(z);

    z->color = RED;

    insertFixUp(z);
}


Node* RBTree::search(Node *start_root, int key) {
    while(!isNull(start_root) && key != start_root->data) {
        if (key < start_root->data)
            start_root = start_root->left;
        else
            start_root = start_root->right;
    }
    return start_root;
}


Node* RBTree::tree_min(Node *x) {
    while(!isNull(x->left)) {
        x = x->left;
    }
    return x;
}


Node* RBTree::tree_max(Node *x) {
    while(!isNull(x->right)) {
        x = x->right;
    }
    return x;
}


void RBTree::transplant(Node *u, Node *v) {
    if (isNull(u->parent))
        root = v;
    else if (u == u->parent->left)
        u->parent->left = v;
    else
        u->parent->right = v;

    v->parent = u->parent;
}


void RBTree::remove_one(Node *z) {
    Node *y = z;
    color y_original_color = y->color;
    Node *x;
    if (isNull(z->left)) {
        x = z->right;
        transplant(z, z->right);
    }
    else if (isNull(z->right)) {
        x = z->left;
        transplant(z, z->left);
    }
    else {
        y = tree_min(z->right);
        y_original_color = y->color;
        x = y->right;

        if (y->parent == z) {
            x->parent = y;
        }
        else {
            transplant(y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        transplant(z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    if (y_original_color == BLACK){
        deleteFixUp(x);
    }
}



void RBTree::deleteFixUp(Node *x) {
    while(x != root && getColor(x) == BLACK) {

        // если x слева
        if (x == x->parent->left) {
            Node * sibling = x->parent->right;

            if (getColor(sibling) == RED) {
                sibling->color = BLACK;
                sibling->parent->color = RED;
                leftRotate(x->parent);
                sibling = x->parent->right;
            }
            if (isNull(sibling)) {
                x = x->parent;
            }
            else if (getColor(sibling->left) == BLACK && getColor(sibling->right) == BLACK) {
                sibling->color = RED;
                x = x->parent;
            }
            else {
                if (getColor(sibling->right) == BLACK) {

                    sibling->color = RED;
                    sibling->left->color = BLACK;
                    rightRotate(sibling);
                    sibling = x->parent->right;
                }
                sibling->color = x->parent->color;
                x->parent->color = BLACK;
                sibling->right->color = BLACK;
                leftRotate(x->parent);
                break;
            }
        }
        // если x справа
        else if (x == x->parent->right) {
            Node * sibling = x->parent->left;

            if (getColor(sibling) == RED) {
                sibling->color = BLACK;
                sibling->parent->color = RED;
                rightRotate(x->parent);
                sibling = x->parent->left;
            }


            if (isNull(sibling)) {
                x = x->parent;
            }
            else if (getColor(sibling->left) == BLACK && getColor(sibling->right) == BLACK) {
                sibling->color = RED;
                x = x->parent;
            }
            else {
                if (getColor(sibling->left) == BLACK) {
                    sibling->color = RED;
                    sibling->right->color = BLACK;
                    leftRotate(sibling);
                    sibling = x->parent->left;
                }
                sibling->color = x->parent->color;
                x->parent->color = BLACK;
                sibling->left->color = BLACK;
                rightRotate(x->parent);
                break;
            }
        }
    }
}



void RBTree::remove(int key) {
    Node * searched = search(root, key);
    if (!isNull(searched)) {
        remove_one(searched);

    }
}


void RBTree::insert(int key) {
    Node * newNode = getNewNode(key);
    insertNode(newNode);
}







