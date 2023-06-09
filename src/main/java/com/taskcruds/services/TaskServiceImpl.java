package com.taskcruds.services;


import com.taskcruds.dtos.TaskDto;
import com.taskcruds.entity.Task;
import com.taskcruds.exception.TaskNotFoundException;
import com.taskcruds.modelmapper.TaskModalMapper;
import com.taskcruds.repository.TaskRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class TaskServiceImpl implements TaskService{
    @Autowired
    private TaskRepository taskRepository;
    TaskModalMapper taskModalMapper;

    public TaskServiceImpl(TaskModalMapper taskModalMapper) {
        this.taskModalMapper = taskModalMapper;
    }

    @Override
    public TaskDto save(TaskDto task) {
        return taskModalMapper.entityToDto(taskRepository.save(taskModalMapper.dtoToEntity(task)));
    }



        @Override
        public List<TaskDto> findAllTasks() {
            return taskRepository.findAll().stream().map(taskModalMapper::entityToDto).collect(Collectors.toList());
        }

        @Override
        public TaskDto updateTask(TaskDto task, int id) {
            Task oldTask=taskRepository.findById(id).orElseThrow(()->new TaskNotFoundException("No Task with Id"));
            if(oldTask!=null){
                if(task.getDescription()!=null){
                    oldTask.setDescription(task.getDescription());
                }
                if(task.getTitle()!=null){
                    oldTask.setTitle(task.getTitle());
                }
                if(task.getStatus()!=null){
                    oldTask.setStatus(task.getStatus());
                }
                if(task.getDueDate()!=null){
                    oldTask.setDueDate(task.getDueDate());
                }
            }
            return taskModalMapper.entityToDto(taskRepository.save(oldTask));
        }



    @Override
    public String deleteTaskById(int id) {
        Task task=taskRepository.findById(id).orElseThrow(()-> new TaskNotFoundException("No Task with this id"));
        if(task!=null){
            taskRepository.delete(task);
        }
        return "Deleted task with id "+id;
    }


}
