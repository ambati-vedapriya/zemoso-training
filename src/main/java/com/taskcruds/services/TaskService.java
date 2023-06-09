package com.taskcruds.services;



import com.taskcruds.dtos.TaskDto;

import java.util.List;
public interface TaskService {
    TaskDto save(TaskDto task);

    List<TaskDto> findAllTasks();

    TaskDto updateTask(TaskDto task, int id);

    String deleteTaskById(int id);
}
