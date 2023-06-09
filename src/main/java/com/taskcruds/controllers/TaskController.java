package com.taskcruds.controllers;


import com.taskcruds.dtos.TaskDto;
import com.taskcruds.services.TaskService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/task")
public class TaskController {
    @Autowired
    private TaskService taskService;
    @PostMapping("/")
    public ResponseEntity<TaskDto> addTheTask(@RequestBody TaskDto task){
        TaskDto tasks=taskService.save(task);
        return ResponseEntity.status(HttpStatus.CREATED).body(tasks);
    }
    @GetMapping("/")
    public ResponseEntity<List<TaskDto>>  getAllTask(){
        return ResponseEntity.status(HttpStatus.FOUND).body(taskService.findAllTasks());
    }

    @PatchMapping("/{id}")
    public ResponseEntity<TaskDto> patchTask(@RequestBody TaskDto task,@PathVariable int id){
        return ResponseEntity.status(HttpStatus.OK).body(taskService.updateTask(task,id));
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteTask(@PathVariable int id){
        return ResponseEntity.status(HttpStatus.FORBIDDEN).body(taskService.deleteTaskById(id));
    }
}
