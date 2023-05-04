/*Assignment on Stream Api

Make a Student class having fields id,name,age,gender,engDepartment,year of enrollment ,perTillDate

Add following student in list ;

1.new Student(111, "Jiya Brein", 17, "Female", "Computer Science", 2018, 70.8)
2.new Student(122, "Paul Niksui", 18, "Male", "Mechanical", 2016, 50.2)
3 new Student(133, "Martin Theron", 17, "Male", "Electronic", 2017, 90.3)
4.new Student(144, "Murali Gowda", 18, "Male", “Electrical”, 2018, 80)
5.new Student(155, "Nima Roy", 19, "Female", "Textile", 2016, 70)
6.new Student(166, "Iqbal Hussain", 18, "Male", "Security", 2016, 70)
7.new Student(177, "Manu Sharma", 16, "Male", "Chemical", 2018, 70)
8.new Student(188, "Wang Liu", 20, "Male", "Computer Science", 2015, 80);
9.new Student(199, "Amelia Zoe", 18, "Female", "Computer Science", 2016, 85);
10.new Student(200, "Jaden Dough", 18, "Male", "Security", 2015, 82);
11.new Student(211, "Jasna Kaur", 20, "Female", "Electronic", 2019, 83);
12.new Student(222, "Nitin Joshi", 19, "Male", "Textile", 2016, 60.4);
13.new Student(233, "Jyothi Reddy", 16, "Female", "Computer Science", 2015, 45.6);
14.new Student(244, "Nicolus Den", 16, "Male", "Electronic", 2017, 95.8);
15.new Student(255, "Ali Baig", 17, "Male", "Electronic", 2018, 88.4);
16.new Student(266, "Sanvi Pandey", 17, "Female", “Electric”, 2019, 72.4);
17.new Student(277, "Anuj Chettiar", 18, "Male", "Computer Science", 2017, 57.5);

Use stream api on above list of employees find*/
package com.Assingments.Assingment12;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Comparator;
import java.util.stream.Collectors;


public class Main {


    public static void main(String[] args) {
        List<Student> students = Arrays.asList(
                new Student(111, "Jiya Brein", 17, "Female", "Computer Science", 2018, 70.8),
                new Student(122, "Paul Niksui", 18, "Male", "Mechanical", 2016, 50.2),
                new Student(133, "Martin Theron", 17, "Male", "Electronic", 2017, 90.3),
                new Student(144, "Murali Gowda", 18, "Male", "Electrical", 2018, 80),
                new Student(155, "Nima Roy", 19, "Female", "Textile", 2016, 70),
                new Student(166, "Iqbal Hussain", 18, "Male", "Security", 2016, 70),
                new Student(177, "Manu Sharma", 16, "Male", "Chemical", 2018, 70),
                new Student(188, "Wang Liu", 20, "Male", "Computer Science", 2015, 80),
                new Student(199, "Amelia Zoe", 18, "Female", "Computer Science", 2016, 85),
                new Student(200, "Jaden Dough", 18, "Male", "Security", 2015, 82),
                new Student(211, "Jasna Kaur", 20, "Female", "Electronic", 2019, 83),
                new Student(222, "Nitin Joshi", 19, "Male", "Textile", 2016, 60.4),
                new Student(233, "Jyothi Reddy", 16, "Female", "Computer Science", 2015, 45.6),
                new Student(244, "Nicolus Den", 16, "Male", "Electronic", 2017, 95.8),
                new Student(255, "Ali Baig", 17, "Male", "Electronic", 2018, 88.4),
                new Student(266, "Sanvi Pandey", 17, "Female", "Electric", 2019, 72.4),
                new Student(277, "Anuj Chettiar", 18, "Male", "Computer Science", 2017, 57.5)
        );

        // 1. Print the name of all departments in the college
        System.out.println("Departments in the college:");
        students.stream()
                .map(Student::getEngDepartment)
                .distinct()
                .forEach(System.out::println);
        System.out.println(" ");

        // 2. Get the names of all students who have enrolled after 2018
        List<String> names = students.stream()
                .filter(s -> s.getYearOfEnrollment() > 2018)
                .map(Student::getName)
                .collect(Collectors.toList());

        System.out.println("Names of students who have enrolled after 2018:");
        names.forEach(System.out::println);
        System.out.println(" ");



        //3. Get the details of all male student in the computer sci department

        List<Student> computerScienceMaleStudents = students.stream()
                .filter(student -> student.getEngDepartment().equalsIgnoreCase("Computer Science"))
                .filter(student -> student.getGender().equalsIgnoreCase("Male"))
                .collect(Collectors.toList());

        computerScienceMaleStudents.forEach(System.out::println);
        System.out.println(" ");

        //4. How many male and female student are there ? (HINT:use Collectors.groupingBy() for grouping based on gender)

        Map<String, Long> countByGender = students.stream()
                .collect(Collectors.groupingBy(Student::getGender, Collectors.counting()));

        long maleCount = countByGender.getOrDefault("Male", 0L);
        long femaleCount = countByGender.getOrDefault("Female", 0L);

        System.out.println("Male count: " + maleCount);
        System.out.println("Female count: " + femaleCount);
        System.out.println(" ");



        //5.What is the average age of male and female students?

        double avgMaleAge = students.stream()
                .filter(s -> s.getGender().equals("Male"))
                .mapToInt(Student::getAge)
                .average()
                .orElse(Double.NaN);

        double avgFemaleAge = students.stream()
                .filter(s -> s.getGender().equals("Female"))
                .mapToInt(Student::getAge)
                .average()
                .orElse(Double.NaN);

        System.out.println("Average age of male students: " + avgMaleAge);
        System.out.println("Average age of female students: " + avgFemaleAge);
        System.out.println(" ");

        //6.Get the details of highest student having highest percentage ?

        Optional<Student> studentWithHighestPercentage = students.stream()
                .collect(Collectors.maxBy(Comparator.comparingDouble(Student::getPerTillDate)));

        if (studentWithHighestPercentage.isPresent()) {
            System.out.println("Student with highest percentage: " + studentWithHighestPercentage.get());
        } else {
            System.out.println("No students found");
        }
        System.out.println(" ");




        //7.Count the number of students in each department? (Hint :use Collectors.groupingBy())

        Map<String, Long> countByDepartment = students.stream()
                .collect(Collectors.groupingBy(Student::getEngDepartment, Collectors.counting()));

        System.out.println("Count of students by department:");
        System.out.println(countByDepartment);
        System.out.println(" ");


       // 8. What is the average percentage achieved in each department?
        Map<String, Double> avgPercentageByDept = students.stream()
                .collect(Collectors.groupingBy(Student::getEngDepartment, Collectors.averagingDouble(Student::getPerTillDate)));

        System.out.println("Average percentage achieved in each department:");
        System.out.println(avgPercentageByDept);
        System.out.println(" ");



        //9.Get the details of youngest male student in the Electronic department?(Hint :Use Collectors.minBy)
        Optional<Student> youngestMaleInElectronic = students.stream()
                .filter(s -> s.getEngDepartment().equals("Electronic"))
                .filter(s -> s.getGender().equals("Male"))
                .collect(Collectors.minBy(Comparator.comparingInt(Student::getAge)));

        if (youngestMaleInElectronic.isPresent()) {
            System.out.println("Youngest Male Student in Electronic Department: " + youngestMaleInElectronic.get());
        } else {
            System.out.println("No male students found in the Electronic department.");
        }
        System.out.println(" ");



        //10.How many male and female students are there in the computer science department?
        Map<String, Long> genderCountInCS = students.stream()
                .filter(s -> s.getEngDepartment().equals("Computer Science"))
                .collect(Collectors.groupingBy(Student::getGender, Collectors.counting()));

        System.out.println("Male Count in Computer Science: " + genderCountInCS.getOrDefault("Male", 0L));
        System.out.println("Female Count in Computer Science: " + genderCountInCS.getOrDefault("Female", 0L));
        System.out.println(" ");






    }
}
