package com.springboot.Assingmentboot.contoller;

import com.springboot.Assingmentboot.entity.Author;
import com.springboot.Assingmentboot.repos.AuthorRepository;
import com.springboot.Assingmentboot.repos.BookRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;

import java.util.ArrayList;

import java.util.List;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.*;

class AuthorControllerTest {
    @Mock
    private AuthorRepository authorRepository;

    @Mock
    private Model model;

    @Mock
    private BindingResult bindingResult;

    @InjectMocks
    private AuthorController authorController;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void showAuthors() {
        List<Author> authors = new ArrayList<>();
        authors.add(new Author());
        when(authorRepository.findAll()).thenReturn(authors);

        String viewName = authorController.showAuthors(model);

        assertEquals("author/list", viewName);
        verify(model).addAttribute(eq("authors"), anyList());
    }

    @Test
    void showCreateForm() {
        String viewName = authorController.showCreateForm(model);

        assertEquals("author/create", viewName);
        verify(model).addAttribute(eq("author"), any(Author.class));
    }

    @Test
    void createAuthor() {
        Author author = new Author();
        when(bindingResult.hasErrors()).thenReturn(false);

        String viewName = authorController.createAuthor(author, bindingResult);

        assertEquals("redirect:/authors", viewName);
        verify(authorRepository).save(author);
    }

    @Test
    void showEditForm() {
        Long id = 1L;
        Author author = new Author();
        when(authorRepository.findById(id)).thenReturn(java.util.Optional.of(author));

        String viewName = authorController.showEditForm(id, model);

        assertEquals("author/edit", viewName);
        verify(model).addAttribute(eq("author"), eq(author));
    }

    @Test
    void updateAuthor() {
        Long id = 1L;
        Author author = new Author();
        when(bindingResult.hasErrors()).thenReturn(false);

        String viewName = authorController.updateAuthor(id, author, bindingResult);

        assertEquals("redirect:/authors", viewName);
        author.setId(id);  // Fix: Set the ID directly on the author object
        verify(authorRepository).save(author);



    }


    @Test
    void deleteAuthor() {
        Long id = 1L;

        String viewName = authorController.deleteAuthor(id);

        assertEquals("redirect:/authors", viewName);
        verify(authorRepository).deleteById(id);
    }

    @Test
    void testCreateAuthor_withValidAuthor() {
        // Arrange
        Author author = new Author();

        // Act
        String viewName = authorController.createAuthor(author, bindingResult);

        // Assert
        assertEquals("redirect:/authors", viewName);
        verify(authorRepository).save(author);
    }

    @Test
    void testCreateAuthor_withInvalidAuthor() {
        // Arrange
        Author author = new Author();
        when(bindingResult.hasErrors()).thenReturn(true);

        // Act
        String viewName = authorController.createAuthor(author, bindingResult);

        // Assert
        assertEquals("author/create", viewName);
        verify(authorRepository, never()).save(author);
    }
    @Test
    void testShowEditForm_withInvalidId() {
        // Arrange
        Long id = 1L;
        when(authorRepository.findById(anyLong())).thenReturn(Optional.empty());

        // Act & Assert
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> authorController.showEditForm(id, model));
        assertEquals("Invalid author Id: " + id, exception.getMessage());
        verify(model, never()).addAttribute(eq("author"), any(Author.class));
    }
    @Test
    void testUpdateAuthor_withInvalidAuthor() {
        // Arrange
        Long id = 1L;
        Author author = Mockito.mock(Author.class);  // Create a mock object
        when(bindingResult.hasErrors()).thenReturn(true);

        // Act
        String viewName = authorController.updateAuthor(id, author, bindingResult);

        // Assert
        assertEquals("author/edit", viewName);
        verify(author).setId(id);  // Verify behavior on the mock object
        verify(authorRepository, never()).save(author);
    }




}