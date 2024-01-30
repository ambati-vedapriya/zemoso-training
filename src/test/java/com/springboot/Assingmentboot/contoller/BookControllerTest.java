package com.springboot.Assingmentboot.contoller;

import com.springboot.Assingmentboot.entity.Author;
import com.springboot.Assingmentboot.entity.Book;
import com.springboot.Assingmentboot.repos.AuthorRepository;
import com.springboot.Assingmentboot.repos.BookRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.*;

class BookControllerTest {
    @Mock
    private BookRepository bookRepository;

    @Mock
    private AuthorRepository authorRepository;
    @Mock
    private BindingResult bindingResult;

    @InjectMocks
    private BookController bookController;
    @Mock
    private Model model;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        bookController = new BookController();
        bookController.setBookRepository(bookRepository);
        bookController.setAuthorRepository(authorRepository);
    }





    @Test
    void showBooks() {
        String viewName =bookController.showCreateForm(model);

        assertEquals("book/create", viewName);
        verify(model).addAttribute(eq("book"), any(Book.class));
    }

    @Test
    void showCreateForm() {
        String viewName = bookController.showCreateForm(model);

        assertEquals("book/create", viewName);
        verify(model).addAttribute(eq("book"), any(Book.class));
    }

    @Test
    void createBook() {
        Book book = new Book();
        BindingResult result = mock(BindingResult.class);
        when(result.hasErrors()).thenReturn(true);

        // Act
        String viewName = bookController.createBook(book, result, model);

        // Assert
        assertEquals("book/create", viewName);
        verify(model).addAttribute("authors", authorRepository.findAll());
    }

    @Test
    void showEditForm() {
        // Arrange
        Long id = 1L;
        Book book = new Book();
        when(bookRepository.findById(id)).thenReturn(Optional.of(book));

        // Act
        String viewName = bookController.showEditForm(id, model);

        // Assert
        assertEquals("book/edit", viewName);
        verify(model).addAttribute("book", book);
        verify(model).addAttribute("authors", authorRepository.findAll());
    }

    @Test
    void updateBook() {
        // Arrange
        Long id = 1L;
        Book book = new Book();
        BindingResult result = mock(BindingResult.class);
        when(result.hasErrors()).thenReturn(false);

        // Act
        String redirectUrl = bookController.updateBook(id, book, result, model);

        // Assert
        assertEquals("redirect:/books", redirectUrl);
        verify(bookRepository).save(book);

    }

    @Test
    void deleteBook() {
        Long id = 1L;

        String viewName = bookController.deleteBook(id);

        assertEquals("redirect:/books", viewName);
        verify(bookRepository).deleteById(id);
    }
    @Test
    void testUpdateBook_withInvalidBook() {
        // Arrange
        Long id = 1L;
        Book book = Mockito.mock(Book.class); // Create a mock object
        when(bindingResult.hasErrors()).thenReturn(true);

        // Act
        String viewName = bookController.updateBook(id, book, bindingResult, model);

        // Assert
        assertEquals("book/edit", viewName);
        verify(book).setId(id); // Verify interactions on the mock object
        verify(model).addAttribute("authors", authorRepository.findAll());
    }

    @Test
    void testShowEditForm_withInvalidId() {
        // Arrange
        Long id = 1L;
        when(bookRepository.findById(id)).thenReturn(Optional.empty());

        // Act and Assert
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            bookController.showEditForm(id, model);
        });

        assertEquals("Invalid book Id: " + id, exception.getMessage());
    }
    @Test
    void testCreateBook_withInvalidBook() {
        // Arrange
        Book book = new Book();
        when(bindingResult.hasErrors()).thenReturn(true);

        // Act
        String viewName = bookController.createBook(book, bindingResult, model);

        // Assert
        assertEquals("book/create", viewName);
        verify(model).addAttribute("authors", authorRepository.findAll());
    }

    @Test
    void testCreateBook_withValidBook() {
        // Arrange
        Book book = new Book();

        // Act
        String viewName = bookController.createBook(book, bindingResult, model);

        // Assert
        assertEquals("redirect:/books", viewName);
        verify(bookRepository).save(book);
    }





}