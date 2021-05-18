export default function updateStudentGradeByCity(students, city, newGrades) {
  const atLocation = students.filter((student) => student.location === city);
  return atLocation.map((student) => {
    const grades = newGrades.filter((item) => item.studentId === student.id);
    const grade = grades.length > 0 ? grades[0].grade : 'N/A';
    return {
      ...student,
      grade,
    };
  });
}
