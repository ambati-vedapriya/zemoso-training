package com.springboot.Assingmentboot.entity;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AuthorTest {
    @Test
    public void testGettersAndSetters() {

        Author author = new Author();


        author.setId(1L);
        author.setName("John Doe");
        author.setEmail("johndoe@example.com");


        Assertions.assertEquals(1L, author.getId());
        Assertions.assertEquals("John Doe", author.getName());
        Assertions.assertEquals("johndoe@example.com", author.getEmail());
    }
    @Test
    public void testEmptyConstructor() {
        // Create an instance of Author using the empty constructor
        Author author = new Author();

        // Check if the object is not null
        Assertions.assertNotNull(author);

        // Check if the initial values are null or empty strings
        Assertions.assertNull(author.getId());
        Assertions.assertNull(author.getName());
        Assertions.assertNull(author.getEmail());
    }


}