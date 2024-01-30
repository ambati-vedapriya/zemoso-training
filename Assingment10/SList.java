package com.Assingments.Assingment10;

public class SList {

        Node head=null;
        public SListIterator iterator(){
            return new SListIterator(this);
        }

        public String toString(SListIterator s){
            Node temp=s.head;
            StringBuilder sb=new StringBuilder();
            while(temp!=null){
                sb.append(temp.data);
                temp=temp.next;
                if(temp!=null){
                    sb.append("->");
                }
            }
            return sb.toString();
        }
    }


