package com.springboot.Assingmentboot.repos;

import com.springboot.Assingmentboot.entity.Author;
import org.springframework.data.jpa.repository.JpaRepository;


public interface AuthorRepository extends JpaRepository <Author, Long>{
}
