export default function getStudentIdsSum(students) {
  return students.reduce((accumltr, student) => accumltr + student.id, 0);
}
