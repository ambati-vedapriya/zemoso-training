package com.taskcruds.dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TaskDto {
    private int  id;
    private  String title;
    private String description;
    private String dueDate;
    private String status;
}
