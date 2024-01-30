package com.Assingments.Assingment10;

public class SListIterator {

        SList sList;
        Node head;
        public SListIterator(SList sList) {
            this.sList = sList;
        }

        public void insert(int val){
            if(head==null){
                head=new Node(val);
            }
            else{
                Node temp=new Node(val);
                temp.next=head;
                head=temp;
            }
        }

        public void remove(int val){
            Node temp=head;
            Node prev=null;

            if(temp!=null && temp.data==val){
                head=temp.next;
                return;
            }
            while (temp!=null && temp.data!=val){
                prev=temp;
                temp=temp.next;
            }

            if(temp==null) return;
            prev.next=temp.next;
        }
    }


