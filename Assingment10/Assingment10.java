/*Generics, Arrays and Containers

Create a generic, singly linked list class called SList, which, to keep things simple, does not implement the List interface.

Each Link object in the list should contain a reference to the next element in the list, but not the previous one (LinkedList, in contrast, is a doubly linked list, which means it maintains links in both directions).

Create your own SListIterator which, again for simplicity, does not implement ListIterator. The only method in SList other than toString( ) should be iterator( ), which produces an SListIterator.

The only way to insert and remove elements from an SList is through SListIterator. Write code to demonstrate SList.
*/
package com.Assingments.Assingment10;

public class Assingment10 {

        public static void main(String args[]) {
            SList sList = new SList();
            SListIterator sListIterator = sList.iterator();
            sListIterator.insert(1);
            sListIterator.insert(2);
            sListIterator.insert(3);
            sListIterator.remove(2);
            System.out.println(sList.toString(sListIterator));
        }
    }


