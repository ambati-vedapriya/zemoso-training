package com.springboot.Assingmentboot.repos;

import com.springboot.Assingmentboot.entity.Book;
import org.springframework.data.jpa.repository.JpaRepository;



public interface BookRepository extends JpaRepository<Book, Long> {

}
