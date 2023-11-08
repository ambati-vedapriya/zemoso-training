package com.springboot.Assingmentboot.entity;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


class BookTest {
    @Test
    public void testGettersAndSetters() {

        Author author = new Author();
        author.setId(1L);
        author.setName("John Doe");
        author.setEmail("johndoe@example.com");


        Book book = new Book();
        book.setId(1L);
        book.setTitle("Sample Book");
        book.setAuthor(author);


        Assertions.assertEquals(1L, book.getId());
        Assertions.assertEquals("Sample Book", book.getTitle());
        Assertions.assertEquals(author, book.getAuthor());
    }
    @Test
    public void testEmptyConstructor() {
        // Create an instance of Book using the empty constructor
        Book book = new Book();

        // Check if the object is not null
        Assertions.assertNotNull(book);

        // Check if the initial values are null or empty strings
        Assertions.assertNull(book.getId());
        Assertions.assertNull(book.getTitle());
        Assertions.assertNull(book.getAuthor());
    }

}