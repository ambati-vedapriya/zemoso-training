package com.taskcruds.modelmapper;

;
import com.taskcruds.dtos.TaskDto;
import com.taskcruds.entity.Task;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Component;

@Component
public class TaskModalMapper {
    private ModelMapper mapper=new ModelMapper();
    public Task dtoToEntity(TaskDto taskDto){
        return mapper.map(taskDto,Task.class);
    }
    public TaskDto entityToDto(Task task){
        return mapper.map(task,TaskDto.class);
    }
}
