package com.taskcruds.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

/*
Build a RESTful API using Spring Boot for a simple task management application.
The application should allow users to perform CRUD operations (Create, Read, Update, Delete) on tasks.
 Each task should have a title, description, due date, and status (e.g., "pending," "completed," "in progress").
 Implement the necessary endpoints and functionality to handle these operations.
 */
@Entity
@Table
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Task {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int  id;
        private  String title;
        private String description;
        private String dueDate;
        private String status;
}
