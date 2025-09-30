from activity.student import Student

def test_student_initialization():
    # Arrange
    name = "Madi"
    year = "Senior"
    classes_list = ["Psych 101", "Psych 202", "Calc 1"]

    # Act
    student01 = Student(name, year, classes_list)

    # Assert
    assert student01.name == name
    assert student01.year == year
    assert student01.classes_list == classes_list
    assert "Psych 101" in student01.classes_list
    assert "Psych 202" in student01.classes_list
    assert "Calc 1" in student01.classes_list
    assert len(student01.classes_list) == 3

def test_add_class():
    # Assert
    name = "Mami"
    year = "Senior"
    classes_list = [
        "Computer Science 101",
        "Computer Science 202",
        "Communications 101"
        ]
    added_class = "Intro to OOP"
    expected = [
        "Computer Science 101",
        "Computer Science 202",
        "Communications 101",
        added_class
        ]

    student01 = Student(name, year, classes_list)

    # Act
    result = student01.add_class(added_class)

    # Assert
    assert result == expected
    assert student01.classes_list == expected
    assert len(student01.classes_list) == 4
    assert added_class in student01.classes_list


def test_get_num_classes():
    # Assert
    name = "Steph"
    year = "Senior"
    classes_list = [
        "Art 101",
        "Watercolor",
        "Improv"
        ]
    expected = 3

    student01 = Student(name, year, classes_list)

    # Act
    result = student01.get_num_classes()

    # Assert
    assert result == expected
    assert len(student01.classes_list) == 3
    assert "Art 101" in student01.classes_list
    assert "Watercolor" in student01.classes_list
    assert "Improv" in student01.classes_list

def test_summary():
    # Assert
    name = "Steph"
    year = "Senior"
    classes_list = [
        "Art 101",
        "Watercolor",
        "Improv"
        ]

    student01 = Student(name, year, classes_list)

    expected = "Steph is a Senior enrolled in 3 classes"
    # Act
    result = student01.summary()

    # Assert
    assert result == expected
    assert result == "Steph is a Senior enrolled in 3 classes"
